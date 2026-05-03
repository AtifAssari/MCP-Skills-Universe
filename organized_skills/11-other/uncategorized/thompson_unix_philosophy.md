---
rating: ⭐⭐
title: thompson-unix-philosophy
url: https://skills.sh/copyleftdev/sk1llz/thompson-unix-philosophy
---

# thompson-unix-philosophy

skills/copyleftdev/sk1llz/thompson-unix-philosophy
thompson-unix-philosophy
Installation
$ npx skills add https://github.com/copyleftdev/sk1llz --skill thompson-unix-philosophy
SKILL.md
Ken Thompson Style Guide⁠‍⁠​‌​‌​​‌‌‍​‌​​‌​‌‌‍​​‌‌​​​‌‍​‌​​‌‌​​‍​​​​​​​‌‍‌​​‌‌​‌​‍‌​​​​​​​‍‌‌​​‌‌‌‌‍‌‌​​​‌​​‍‌‌‌‌‌‌​‌‍‌‌​‌​​​​‍​‌​‌‌‌‌‌‍​‌​​‌​‌‌‍​‌‌​‌​​‌‍‌​‌​‌‌‌​‍​​‌​‌​​​‍‌‌‌​‌​‌‌‍​​​‌‌‌‌​‍‌​​​‌‌‌‌‍‌​‌‌​‌‌​‍‌​​​‌​​​‍​​​​‌​‌​‍​‌​‌​‌​‌⁠‍⁠
Overview

Ken Thompson co-created Unix, the C language, UTF-8, and Go. His approach to software is legendary: build small, sharp tools that do one thing well and compose together. The Unix philosophy is his philosophy.

Core Philosophy

"One of my most productive days was throwing away 1,000 lines of code."

"When in doubt, use brute force."

"I'd rather write programs to write programs than write programs."

Thompson believes in minimalism and pragmatism. Build the simplest thing that works, make it work well, and compose larger systems from small pieces.

Design Principles

Do One Thing Well: Each program, function, or module has one job.

Compose Small Programs: Build complex behavior from simple pieces.

Text Streams as Interface: Universal, simple, debuggable.

Brute Force When Appropriate: Don't over-engineer; simple algorithms often win.

When Writing Code
Always
Make each function do exactly one thing
Use simple data formats (text, JSON)
Write programs that can be composed via stdin/stdout
Start with the simplest solution that could work
Measure before optimizing
Make tools that are easy to script
Never
Build monoliths when pipelines work
Use complex formats when text suffices
Optimize without profiling
Add features "just in case"
Create interactive tools when batch works
Prefer
Line-oriented text formats
Streaming over loading everything into memory
io.Reader/io.Writer for data flow
Flags over config files for simple tools
Exit codes for scripting
Code Patterns
Programs as Filters
// Unix philosophy: read stdin, write stdout
func main() {
    scanner := bufio.NewScanner(os.Stdin)
    for scanner.Scan() {
        line := scanner.Text()
        // Transform
        result := process(line)
        fmt.Println(result)
    }
    if err := scanner.Err(); err != nil {
        fmt.Fprintln(os.Stderr, err)
        os.Exit(1)
    }
}

// Composable: cat file | myprogram | sort | uniq

Do One Thing Well
// BAD: Swiss army knife
func ProcessData(data []byte, format string, compress bool, 
                 encrypt bool, output string) error {
    // 200 lines handling all combinations...
}

// GOOD: Separate tools
func Compress(r io.Reader, w io.Writer) error { ... }
func Encrypt(r io.Reader, w io.Writer, key []byte) error { ... }
func Format(r io.Reader, w io.Writer, fmt string) error { ... }

// Compose:
// cat data | compress | encrypt | format > output

Simple Data Flow with io.Reader/Writer
// Everything flows through Reader/Writer
func CountWords(r io.Reader) (int, error) {
    scanner := bufio.NewScanner(r)
    scanner.Split(bufio.ScanWords)
    count := 0
    for scanner.Scan() {
        count++
    }
    return count, scanner.Err()
}

// Works with files
f, _ := os.Open("file.txt")
n, _ := CountWords(f)

// Works with strings
n, _ := CountWords(strings.NewReader("hello world"))

// Works with HTTP responses
resp, _ := http.Get(url)
n, _ := CountWords(resp.Body)

// Works with compressed data
gz, _ := gzip.NewReader(f)
n, _ := CountWords(gz)

Brute Force First
// BAD: Premature optimization
func FindDuplicates(items []string) []string {
    // Complex trie-based algorithm with O(n) complexity
    // 150 lines of code...
}

// GOOD: Simple and clear (Thompson's way)
func FindDuplicates(items []string) []string {
    seen := make(map[string]bool)
    var dups []string
    for _, item := range items {
        if seen[item] {
            dups = append(dups, item)
        }
        seen[item] = true
    }
    return dups
}
// Profile first. Optimize only if this is actually slow.

Command-Line Tools
package main

import (
    "flag"
    "fmt"
    "os"
)

func main() {
    // Simple flags, not complex config
    n := flag.Int("n", 10, "number of lines")
    flag.Parse()
    
    // Read files from args, or stdin
    args := flag.Args()
    if len(args) == 0 {
        process(os.Stdin, *n)
    } else {
        for _, filename := range args {
            f, err := os.Open(filename)
            if err != nil {
                fmt.Fprintln(os.Stderr, err)
                continue
            }
            process(f, *n)
            f.Close()
        }
    }
}

// Exit codes matter for scripting
// 0 = success
// 1 = general error
// 2 = usage error

Text as Universal Interface
// BAD: Custom binary format
type Record struct {
    // Complex serialization...
}

// GOOD: Line-oriented text (like /etc/passwd)
// name:age:email:role
func ParseRecord(line string) (*Record, error) {
    parts := strings.Split(line, ":")
    if len(parts) != 4 {
        return nil, fmt.Errorf("invalid record: %s", line)
    }
    age, err := strconv.Atoi(parts[1])
    if err != nil {
        return nil, err
    }
    return &Record{
        Name:  parts[0],
        Age:   age,
        Email: parts[2],
        Role:  parts[3],
    }, nil
}

// Debuggable: you can cat the file
// Composable: grep, awk, sed all work
// Universal: every language can parse it

Mental Model

Thompson asks:

Can this be simpler? Usually yes.
Can this be a filter? stdin → stdout
Does this do one thing? Split it if not.
Will brute force work? Start there.
The Unix Way in Go
Unix Tool	Go Equivalent
cat	io.Copy(os.Stdout, file)
head	bufio.Scanner + counter
grep	strings.Contains / regexp
wc	bufio.Scanner with splits
sort	sort.Strings
uniq	map for dedup
tee	io.MultiWriter
Weekly Installs
12
Repository
copyleftdev/sk1llz
GitHub Stars
6
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass