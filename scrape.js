const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

const BATCH_SIZE = 1000;
const PARALLEL_CONCURRENCY = 20; 
const BASE_DIR = path.join(__dirname, 'skills_library');
const trackerFile = path.join(__dirname, 'processed_urls.json');

if (!fs.existsSync(BASE_DIR)) fs.mkdirSync(BASE_DIR, { recursive: true });

let processedUrls = fs.existsSync(trackerFile) ? JSON.parse(fs.readFileSync(trackerFile)) : [];
let urlSet = new Set(processedUrls);

// Generate all combinations: aa, ab, ac... 00, 01...
const chars = "abcdefghijklmnopqrstuvwxyz0123456789".split("");
const searchCombos = [];
for (let i of chars) {
    for (let j of chars) {
        searchCombos.push(i + j);
    }
}

async function downloadSkill(browser, skill, batchFolder) {
    if (urlSet.has(skill.url)) return;
    const page = await browser.newPage();
    try {
        await page.setRequestInterception(true);
        page.on('request', (req) => {
            if (['image', 'font', 'stylesheet'].includes(req.resourceType())) req.abort();
            else req.continue();
        });
        await page.goto(skill.url, { waitUntil: 'domcontentloaded', timeout: 20000 });
        const content = await page.evaluate(() => document.querySelector('main, article, .markdown-body')?.innerText || "");
        const fileContent = `---\ntitle: ${skill.name}\nurl: ${skill.url}\n---\n\n# ${skill.name}\n\n${content}`;
        const safeName = skill.name.replace(/[^a-z0-9]/gi, '_').toLowerCase();
        fs.writeFileSync(path.join(batchFolder, `${safeName}.md`), fileContent);
        urlSet.add(skill.url);
        processedUrls.push(skill.url);
    } catch (e) {} finally { await page.close(); }
}

(async () => {
    const browser = await puppeteer.launch({ headless: true });
    const mainPage = await browser.newPage();
    await mainPage.goto('https://skills.sh', { waitUntil: 'networkidle2' });

    let lastBatchCount = Math.floor(urlSet.size / BATCH_SIZE);

    console.log(`🚀 Starting DEEP MINE (1,296 combinations)... Current Total: ${urlSet.size}`);

    for (const combo of searchCombos) {
        process.stdout.write(`\r⌨️ Testing Combo: "${combo}" | Total: ${urlSet.size} `);
        
        try {
            const searchInput = await mainPage.$('input[type="text"], input[type="search"]');
            if (searchInput) {
                await searchInput.click({ clickCount: 3 });
                await searchInput.press('Backspace');
                await searchInput.type(combo, { delay: 20 }); 
                await new Promise(r => setTimeout(r, 1200));
            }

            let lastDiscoveryTotal = 0;
            let consecutiveNoNew = 0;

            while (true) {
                await mainPage.evaluate(() => window.scrollBy(0, window.innerHeight * 15));
                await new Promise(r => setTimeout(r, 800));

                const visibleSkills = await mainPage.evaluate(() => {
                    return Array.from(document.querySelectorAll('h3.font-semibold.text-foreground')).map(n => ({
                        name: n.innerText.trim(),
                        url: n.closest('a')?.href
                    })).filter(s => s.url);
                });

                const newFound = visibleSkills.filter(s => !urlSet.has(s.url));

                if (newFound.length >= 10) {
                    const currentBatchNum = Math.floor(urlSet.size / BATCH_SIZE) + 1;
                    const batchFolder = path.join(BASE_DIR, `batch_${currentBatchNum}`);
                    if (!fs.existsSync(batchFolder)) fs.mkdirSync(batchFolder, { recursive: true });

                    for (let i = 0; i < newFound.length; i += PARALLEL_CONCURRENCY) {
                        const chunk = newFound.slice(i, i + PARALLEL_CONCURRENCY);
                        await Promise.all(chunk.map(skill => downloadSkill(browser, skill, batchFolder)));
                        fs.writeFileSync(trackerFile, JSON.stringify(Array.from(urlSet)));
                    }

                    if (Math.floor(urlSet.size / BATCH_SIZE) > lastBatchCount) {
                        lastBatchCount = Math.floor(urlSet.size / BATCH_SIZE);
                        exec(`say "Batch ${lastBatchCount} reached."`);
                    }
                }

                if (visibleSkills.length === lastDiscoveryTotal || newFound.length > 300) {
                    consecutiveNoNew++;
                    if (consecutiveNoNew > 2) break; // Move fast between combos
                } else {
                    consecutiveNoNew = 0;
                }
                lastDiscoveryTotal = visibleSkills.length;
            }
        } catch (err) { continue; }
    }
    await browser.close();
})();
