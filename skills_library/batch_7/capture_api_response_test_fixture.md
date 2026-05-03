---
title: capture-api-response-test-fixture
url: https://skills.sh/vercel/ai/capture-api-response-test-fixture
---

# capture-api-response-test-fixture

skills/vercel/ai/capture-api-response-test-fixture
capture-api-response-test-fixture
Installation
$ npx skills add https://github.com/vercel/ai --skill capture-api-response-test-fixture
Summary

Store and manage API response test fixtures for provider parsing validation.

Fixtures are organized in __fixtures__ subfolders within provider packages, using naming conventions documented in existing examples
Supports two testing patterns: generateText (log raw response to console and copy into fixture) and streamText (use includeRawChunks and saveRawChunks helper to capture streaming chunks)
Recommends storing true provider responses unless size constraints require semantic-preserving cuts
Includes example scripts in /examples/ai-functions for generating fixtures via pnpm tsx
SKILL.md
API Response Test Fixtures

For provider response parsing tests, we aim at storing test fixtures with the true responses from the providers (unless they are too large in which case some cutting that does not change semantics is advised).

The fixtures are stored in a __fixtures__ subfolder, e.g. packages/openai/src/responses/__fixtures__. See the file names in packages/openai/src/responses/__fixtures__ for naming conventions and packages/openai/src/responses/openai-responses-language-model.test.ts for how to set up test helpers.

You can use our examples under /examples/ai-functions to generate test fixtures.

generateText (doGenerate testing)

For generateText, log the raw response output to the console and copy it into a new test fixture.

import { openai } from '@ai-sdk/openai';
import { generateText } from 'ai';
import { run } from '../lib/run';

run(async () => {
  const result = await generateText({
    model: openai('gpt-5-nano'),
    prompt: 'Invent a new holiday and describe its traditions.',
  });

  console.log(JSON.stringify(result.response.body, null, 2));
});

streamText (doStream testing)

For streamText, you need to set includeRawChunks to true and use the special saveRawChunks helper. Run the script from the /example/ai-functions folder via pnpm tsx src/stream-text/script-name.ts. The result is then stored in the /examples/ai-functions/output folder. You can copy it to your fixtures folder and rename it.

import { openai } from '@ai-sdk/openai';
import { streamText } from 'ai';
import { run } from '../lib/run';
import { saveRawChunks } from '../lib/save-raw-chunks';

run(async () => {
  const result = streamText({
    model: openai('gpt-5-nano'),
    prompt: 'Invent a new holiday and describe its traditions.',
    includeRawChunks: true,
  });

  await saveRawChunks({ result, filename: 'openai-gpt-5-nano' });
});

Weekly Installs
668
Repository
vercel/ai
GitHub Stars
24.0K
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass