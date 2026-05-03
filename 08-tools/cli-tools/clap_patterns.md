---
title: clap-patterns
url: https://skills.sh/geoffjay/claude-plugins/clap-patterns
---

# clap-patterns

skills/geoffjay/claude-plugins/clap-patterns
clap-patterns
Installation
$ npx skills add https://github.com/geoffjay/claude-plugins --skill clap-patterns
SKILL.md
Clap Patterns Skill

Common patterns and idioms for using Clap v4+ effectively in Rust CLI applications.

Derive API vs Builder API
When to Use Derive API
CLI structure known at compile time
Want type safety and compile-time validation
Prefer declarative style
Standard CLI patterns are sufficient
#[derive(Parser)]
#[command(version, about)]
struct Cli {
    #[arg(short, long)]
    input: PathBuf,
}

When to Use Builder API
CLI needs to be built dynamically at runtime
Building plugin systems
Arguments depend on configuration
Need maximum flexibility
fn build_cli() -> Command {
    Command::new("app")
        .arg(Arg::new("input").short('i'))
}

Common Patterns
Global Options with Subcommands
#[derive(Parser)]
struct Cli {
    #[arg(short, long, global = true, action = ArgAction::Count)]
    verbose: u8,

    #[command(subcommand)]
    command: Commands,
}

Argument Groups for Mutual Exclusivity
#[derive(Parser)]
#[command(group(
    ArgGroup::new("format")
        .required(true)
        .args(&["json", "yaml", "toml"])
))]
struct Cli {
    #[arg(long)]
    json: bool,
    #[arg(long)]
    yaml: bool,
    #[arg(long)]
    toml: bool,
}

Custom Value Parsers
fn parse_port(s: &str) -> Result<u16, String> {
    let port: u16 = s.parse()
        .map_err(|_| format!("`{s}` isn't a valid port"))?;
    if (1024..=65535).contains(&port) {
        Ok(port)
    } else {
        Err(format!("port not in range 1024-65535"))
    }
}

#[derive(Parser)]
struct Cli {
    #[arg(long, value_parser = parse_port)]
    port: u16,
}

Environment Variable Fallbacks
#[derive(Parser)]
struct Cli {
    #[arg(long, env = "API_TOKEN")]
    token: String,

    #[arg(long, env = "API_ENDPOINT", default_value = "https://api.example.com")]
    endpoint: String,
}

Flattening Shared Options
#[derive(Args)]
struct CommonOpts {
    #[arg(short, long)]
    verbose: bool,

    #[arg(short, long)]
    config: Option<PathBuf>,
}

#[derive(Parser)]
struct Cli {
    #[command(flatten)]
    common: CommonOpts,

    #[command(subcommand)]
    command: Commands,
}

Multiple Values
#[derive(Parser)]
struct Cli {
    /// Tags (can be specified multiple times)
    #[arg(short, long)]
    tag: Vec<String>,

    /// Files to process
    files: Vec<PathBuf>,
}
// Usage: myapp --tag rust --tag cli file1.txt file2.txt

Subcommand with Shared Arguments
#[derive(Parser)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    Build(BuildArgs),
    Test(TestArgs),
}

#[derive(Args)]
struct BuildArgs {
    #[command(flatten)]
    common: CommonOpts,

    #[arg(short, long)]
    release: bool,
}

Argument Counting (Verbosity Levels)
#[derive(Parser)]
struct Cli {
    /// Verbosity (-v, -vv, -vvv)
    #[arg(short, long, action = ArgAction::Count)]
    verbose: u8,
}
// Usage: -v (1), -vv (2), -vvv (3)

Help Template Customization
#[derive(Parser)]
#[command(
    after_help = "EXAMPLES:\n  \
        myapp --input file.txt\n  \
        myapp -i file.txt -vv\n\n\
        For more info: https://example.com"
)]
struct Cli {
    // ...
}

Value Hints
#[derive(Parser)]
struct Cli {
    #[arg(short, long, value_name = "FILE", value_hint = ValueHint::FilePath)]
    input: PathBuf,

    #[arg(short, long, value_name = "DIR", value_hint = ValueHint::DirPath)]
    output: PathBuf,

    #[arg(short, long, value_name = "URL", value_hint = ValueHint::Url)]
    endpoint: String,
}

Default Values with Functions
fn default_config_path() -> PathBuf {
    dirs::config_dir()
        .unwrap()
        .join("myapp")
        .join("config.toml")
}

#[derive(Parser)]
struct Cli {
    #[arg(long, default_value_os_t = default_config_path())]
    config: PathBuf,
}

Best Practices
Use value_name for clearer help text
Provide both short and long flags where appropriate
Add help text to all arguments
Use ValueEnum for fixed set of choices
Validate early with custom parsers
Support environment variables for sensitive data
Use argument groups for mutually exclusive options
Document with examples in after_help
Use semantic types (PathBuf, not String for paths)
Test CLI parsing with integration tests
References
Clap Documentation
Clap Derive Reference
Clap Examples
Weekly Installs
20
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