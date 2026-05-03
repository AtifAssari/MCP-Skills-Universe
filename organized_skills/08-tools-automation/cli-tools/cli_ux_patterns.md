---
rating: ⭐⭐⭐
title: cli-ux-patterns
url: https://skills.sh/geoffjay/claude-plugins/cli-ux-patterns
---

# cli-ux-patterns

skills/geoffjay/claude-plugins/cli-ux-patterns
cli-ux-patterns
Installation
$ npx skills add https://github.com/geoffjay/claude-plugins --skill cli-ux-patterns
SKILL.md
CLI UX Patterns Skill

Best practices and patterns for creating delightful command-line user experiences.

Error Message Patterns
The Three Parts of Good Error Messages
What went wrong - Clear description of the error
Why it matters - Context about the operation
How to fix it - Actionable suggestions
bail!(
    "Failed to read config file: {}\n\n\
     The application needs a valid configuration to start.\n\n\
     To fix this:\n\
     1. Create a config file: myapp init\n\
     2. Or specify a different path: --config /path/to/config.toml\n\
     3. Check file permissions: ls -l {}",
    path.display(),
    path.display()
);

Using miette for Rich Diagnostics
#[derive(Error, Debug, Diagnostic)]
#[error("Configuration error")]
#[diagnostic(
    code(config::invalid),
    url("https://docs.example.com/config"),
    help("Check the syntax of your configuration file")
)]
struct ConfigError {
    #[source_code]
    src: String,

    #[label("invalid value here")]
    span: SourceSpan,
}

Color Usage Patterns
Semantic Colors
Red - Errors, failures, destructive actions
Yellow - Warnings, cautions
Green - Success, completion, safe operations
Blue - Information, hints, links
Cyan - Highlights, emphasis
Dim/Gray - Less important info, metadata
use owo_colors::OwoColorize;

// Status indicators with colors
println!("{} Build succeeded", "✓".green().bold());
println!("{} Warning: using default", "⚠".yellow().bold());
println!("{} Error: file not found", "✗".red().bold());
println!("{} Info: processing 10 files", "ℹ".blue().bold());

Respecting NO_COLOR
use owo_colors::{OwoColorize, Stream};

fn print_status(message: &str, is_error: bool) {
    let stream = if is_error { Stream::Stderr } else { Stream::Stdout };

    if is_error {
        eprintln!("{}", message.if_supports_color(stream, |text| text.red()));
    } else {
        println!("{}", message.if_supports_color(stream, |text| text.green()));
    }
}

Progress Indication Patterns
When to Use Progress Bars
File downloads/uploads
Bulk processing with known count
Multi-step processes
Any operation > 2 seconds with known total
use indicatif::{ProgressBar, ProgressStyle};

let pb = ProgressBar::new(items.len() as u64);
pb.set_style(
    ProgressStyle::default_bar()
        .template("{spinner:.green} [{bar:40}] {pos}/{len} {msg}")?
        .progress_chars("=>-")
);

for item in items {
    pb.set_message(format!("Processing {}", item.name));
    process(item)?;
    pb.inc(1);
}

pb.finish_with_message("Complete!");

When to Use Spinners
Unknown duration operations
Waiting for external resources
Operations < 2 seconds
Indeterminate progress
let spinner = ProgressBar::new_spinner();
spinner.set_style(
    ProgressStyle::default_spinner()
        .template("{spinner:.green} {msg}")?
);

spinner.set_message("Connecting to server...");
// Do work
spinner.finish_with_message("Connected!");

Interactive Prompt Patterns
When to Prompt vs When to Fail

Prompt when:

Optional information for better UX
Choosing from known options
Confirmation for destructive operations
First-time setup/initialization

Fail with error when:

Required information
Non-interactive environment (CI/CD)
Piped input/output
--yes flag provided
use dialoguer::Confirm;

fn delete_resource(name: &str, force: bool) -> Result<()> {
    if !force && atty::is(atty::Stream::Stdin) {
        let confirmed = Confirm::new()
            .with_prompt(format!("Delete {}? This cannot be undone", name))
            .default(false)
            .interact()?;

        if !confirmed {
            println!("Cancelled");
            return Ok(());
        }
    }

    // Perform deletion
    Ok(())
}

Smart Defaults
use dialoguer::Input;

fn get_project_name(current_dir: &Path) -> Result<String> {
    let default = current_dir
        .file_name()
        .and_then(|n| n.to_str())
        .unwrap_or("my-project");

    Input::new()
        .with_prompt("Project name")
        .default(default.to_string())
        .interact_text()
}

Output Formatting Patterns
Human-Readable vs Machine-Readable
#[derive(Parser)]
struct Cli {
    #[arg(long)]
    json: bool,

    #[arg(short, long)]
    verbose: bool,
}

fn print_results(results: &[Item], cli: &Cli) {
    if cli.json {
        // Machine-readable
        println!("{}", serde_json::to_string_pretty(&results).unwrap());
    } else {
        // Human-readable
        for item in results {
            println!("{} {} - {}",
                if item.active { "✓".green() } else { "✗".red() },
                item.name.bold(),
                item.description.dimmed()
            );
        }
    }
}

Table Output
use comfy_table::{Table, Cell, Color};

fn print_table(items: &[Item]) {
    let mut table = Table::new();
    table.set_header(vec!["Name", "Status", "Created"]);

    for item in items {
        let status_color = if item.active { Color::Green } else { Color::Red };
        table.add_row(vec![
            Cell::new(&item.name),
            Cell::new(&item.status).fg(status_color),
            Cell::new(&item.created),
        ]);
    }

    println!("{table}");
}

Verbosity Patterns
Progressive Disclosure
fn log_message(level: u8, quiet: bool, message: &str) {
    match (level, quiet) {
        (_, true) => {}, // Quiet mode: no output
        (0, false) => {}, // Default: only errors
        (1, false) => println!("{}", message), // -v: basic info
        (2, false) => println!("INFO: {}", message), // -vv: detailed
        _ => println!("[DEBUG] {}", message), // -vvv: everything
    }
}

Quiet Mode
#[derive(Parser)]
struct Cli {
    #[arg(short, long)]
    quiet: bool,

    #[arg(short, long, action = ArgAction::Count, conflicts_with = "quiet")]
    verbose: u8,
}

Confirmation Patterns
Destructive Operations
// Always require confirmation for:
// - Deleting data
// - Overwriting files
// - Production deployments
// - Irreversible operations

fn deploy_to_production(force: bool) -> Result<()> {
    if !force {
        println!("{}", "WARNING: Deploying to PRODUCTION".red().bold());
        println!("This will affect live users.");

        let confirmed = Confirm::new()
            .with_prompt("Are you absolutely sure?")
            .default(false)
            .interact()?;

        if !confirmed {
            return Ok(());
        }
    }

    // Deploy
    Ok(())
}

Stdout vs Stderr
Best Practices
stdout - Program output, data, results
stderr - Errors, warnings, progress, diagnostics
// Correct usage
println!("result: {}", data); // stdout - actual output
eprintln!("Error: {}", error); // stderr - error message
eprintln!("Processing..."); // stderr - progress update

// This allows piping output while seeing progress:
// myapp process file.txt | other_command
// (progress messages don't interfere with piped data)

Accessibility Considerations
Screen Reader Friendly
// Always include text prefixes, not just symbols
fn print_status(level: Level, message: &str) {
    let (symbol, prefix) = match level {
        Level::Success => ("✓", "SUCCESS:"),
        Level::Error => ("✗", "ERROR:"),
        Level::Warning => ("⚠", "WARNING:"),
        Level::Info => ("ℹ", "INFO:"),
    };

    // Both symbol and text for accessibility
    println!("{} {} {}", symbol, prefix, message);
}

Color Blindness Considerations
Don't rely on color alone
Use symbols/icons with colors
Test with color blindness simulators
Provide text alternatives
The 12-Factor CLI Principles
Great help - Comprehensive, discoverable
Prefer flags to args - More explicit
Respect POSIX - Follow conventions
Use stdout for output - Enable piping
Use stderr for messaging - Keep output clean
Handle signals - Respond to Ctrl+C gracefully
Be quiet by default - User controls verbosity
Fail fast - Validate early
Support --help and --version - Always
Be explicit - Avoid surprising behavior
Be consistent - Follow patterns
Make it easy - Good defaults, clear errors
References
CLI Guidelines
12 Factor CLI Apps
NO_COLOR
Human-First CLI Design
Weekly Installs
26
Repository
geoffjay/claude-plugins
GitHub Stars
8
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass