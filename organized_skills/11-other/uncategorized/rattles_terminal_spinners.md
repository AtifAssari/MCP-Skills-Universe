---
rating: ⭐⭐⭐
title: rattles-terminal-spinners
url: https://skills.sh/aradotso/trending-skills/rattles-terminal-spinners
---

# rattles-terminal-spinners

skills/aradotso/trending-skills/rattles-terminal-spinners
rattles-terminal-spinners
Installation
$ npx skills add https://github.com/aradotso/trending-skills --skill rattles-terminal-spinners
SKILL.md
Rattles Terminal Spinners

Skill by ara.so — Daily 2026 Skills collection.

Rattles is a minimal, zero-dependency Rust library for terminal spinners. It has no runtime or lifecycle — spinners are constructed directly in render loops with negligible cost. Supports no_std environments.

Installation
# Cargo.toml
[dependencies]
rattles = "0.1"  # with std (default)

# no_std
rattles = { version = "0.1", default-features = false }


Or via CLI:

cargo add rattles

# no_std variant
cargo add rattles --no-default-features

Core Concepts
Rattler: a spinner definition (frames + interval). Stateless and cheap to construct.
TickedRattler: stateful wrapper for tick-based driving (required in no_std).
Presets: built-in spinners organized by category.
rattle! macro: define custom spinners at compile time.
Basic Usage (std)
use std::{io::Write, time::Duration};
use rattles::presets::prelude as presets;

fn main() {
    let rattle = presets::dots();

    loop {
        print!("\r{}", rattle.current_frame());
        std::io::stdout().flush().unwrap();
        std::thread::sleep(Duration::from_millis(80));
    }
}


current_frame() uses the system clock internally — no state needed.

Preset Categories
use rattles::presets::{arrows, ascii, braille, emoji};
use rattles::presets::prelude as presets; // re-exports all presets

// Arrows
let s = arrows::arrow();
let s = arrows::arrow2();

// ASCII
let s = ascii::line();
let s = ascii::pipe();

// Braille
let s = braille::dots();
let s = braille::dots2();

// Emoji
let s = emoji::earth();
let s = emoji::clock();

// Prelude examples
let s = presets::waverows();
let s = presets::dots();

Rattler API
use rattles::presets::prelude as presets;
use std::time::Duration;

let rattle = presets::dots();

// Get frame based on system clock (std only)
let frame: &str = rattle.current_frame();

// Get frame at specific elapsed duration (std + no_std)
let frame = rattle.frame_at(Duration::from_millis(500));

// Get frame by index
let frame = rattle.frame(3);

// Change animation interval
let rattle = presets::dots().set_interval(Duration::from_millis(50));

// Reverse direction
let rattle = presets::waverows().reverse();

// Convert to tick-based (stateful)
let mut ticked = presets::dots().into_ticked();

TickedRattler (Stateful / no_std-friendly)
use rattles::presets::prelude as presets;

let mut rattle = presets::dots().into_ticked();

loop {
    rattle.tick();
    let frame = rattle.current_frame();
    // render frame...
}


TickedRattler must be stored (it holds state). Suitable for no_std contexts where the global clock is unavailable.

Index-Based Animation (no_std)
use rattles::presets::prelude as presets;

let rattle = presets::dots();
let mut i = 0usize;

loop {
    let frame = rattle.frame(i);
    i = i.wrapping_add(1);
    // render frame...
}

Time-Based Animation with External Clock (no_std)
use rattles::presets::prelude as presets;
use core::time::Duration;

let rattle = presets::dots();

// elapsed comes from your platform's timer
let elapsed: Duration = get_elapsed(); // your implementation
let frame = rattle.frame_at(elapsed);

Custom Spinners with rattle! Macro
use rattles::rattle;

rattle!(
    MySpinner,   // generated struct name
    my_spinner,  // generated constructor function name
    1,           // row count (width of spinner)
    120,         // interval in milliseconds
    ["⣾", "⣷", "⣯", "⣟", "⣻", "⣽"]  // keyframes
);

// Use it like any preset
let s = my_spinner();
println!("{}", s.current_frame());


Multi-row custom spinner:

rattle!(
    Wide,
    wide_spinner,
    3,   // 3 characters wide
    80,
    ["[   ]", "[=  ]", "[== ]", "[===]", "[ ==]", "[  =]"]
);

Ratatui Integration
// examples/ratatui.rs pattern
use rattles::presets::prelude as presets;
use ratatui::{
    backend::CrosstermBackend,
    widgets::Paragraph,
    Terminal,
};

fn ui(frame: &mut ratatui::Frame, rattle: &rattles::Rattler) {
    let spinner_text = rattle.current_frame();
    let paragraph = Paragraph::new(format!("{} Loading...", spinner_text));
    frame.render_widget(paragraph, frame.size());
}

fn main() -> std::io::Result<()> {
    let rattle = presets::dots();

    // standard ratatui event loop
    loop {
        terminal.draw(|f| ui(f, &rattle))?;
        std::thread::sleep(std::time::Duration::from_millis(16));

        // break on user input...
    }
    Ok(())
}


Since Rattler is stateless, pass it by reference anywhere — no Arc<Mutex<>> needed.

no_std Setup
[dependencies]
rattles = { version = "0.1", default-features = false }

#![no_std]
use rattles::presets::prelude as presets;

// Option 1: tick-based
let mut rattle = presets::dots().into_ticked();
rattle.tick();
let frame = rattle.current_frame();

// Option 2: index-based
let rattle = presets::dots();
let frame = rattle.frame(42);

// Option 3: duration-based (external clock)
let rattle = presets::dots();
let frame = rattle.frame_at(core::time::Duration::from_millis(840));

Common Patterns
Spinner with message
use rattles::presets::prelude as presets;
use std::{io::Write, time::Duration};

fn main() {
    let rattle = presets::dots();
    let message = "Fetching data...";

    loop {
        print!("\r{} {}", rattle.current_frame(), message);
        std::io::stdout().flush().unwrap();
        std::thread::sleep(Duration::from_millis(80));
    }
}

Async-compatible (tokio)
use rattles::presets::prelude as presets;
use tokio::time::{sleep, Duration};

#[tokio::main]
async fn main() {
    let rattle = presets::dots();

    let spinner = tokio::spawn(async move {
        loop {
            print!("\r{}", rattle.current_frame());
            std::io::stdout().flush().unwrap();
            sleep(Duration::from_millis(80)).await;
        }
    });

    // do your async work
    do_work().await;
    spinner.abort();
    println!("\rDone!     ");
}

Collecting all frames
let rattle = presets::dots();
let frames: Vec<&str> = (0..rattle.frame_count())
    .map(|i| rattle.frame(i))
    .collect();

Troubleshooting

Spinner not animating (stuck on first frame)

Ensure you're flushing stdout: std::io::stdout().flush().unwrap()
Use \r to overwrite the line, not \n
The sleep interval should match or be shorter than the spinner's interval

current_frame() not available in no_std

Use frame_at(duration), frame(index), or into_ticked() instead
Disable default features: rattles = { version = "...", default-features = false }

Custom spinner not compiling

Keyframes must be string literals in the rattle! macro array
Row count must match the visual width of each keyframe string

Spinner looks garbled in terminal

Some braille/emoji frames require a terminal with Unicode support
Test with ASCII presets (ascii::line()) to verify basic functionality first
Weekly Installs
270
Repository
aradotso/trending-skills
GitHub Stars
42
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass