---
title: vhs
url: https://skills.sh/pproenca/dot-skills/vhs
---

# vhs

skills/pproenca/dot-skills/vhs
vhs
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill vhs
SKILL.md
Charmbracelet VHS Best Practices

Comprehensive best practices guide for VHS terminal recordings, maintained by Charmbracelet. Contains 47 rules across 8 categories, prioritized by impact to guide creation of professional, portable, and optimized terminal demos.

When to Apply

Reference these guidelines when:

Writing new VHS tape files
Creating terminal demos for documentation
Setting up CI/CD for automated GIF generation
Optimizing recording file size and quality
Troubleshooting tape file issues
Reviewing tape files for best practices
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Configuration Structure	CRITICAL	config-
2	Dependency Management	CRITICAL	deps-
3	Command Syntax	HIGH	cmd-
4	Timing & Synchronization	HIGH	timing-
5	Output Optimization	MEDIUM-HIGH	output-
6	Visual Quality	MEDIUM	visual-
7	CI/Automation	MEDIUM	ci-
8	Advanced Patterns	LOW	advanced-
Quick Reference
1. Configuration Structure (CRITICAL)
config-settings-order - Place all settings before commands
config-output-first - Declare output at file start
config-shell-explicit - Explicitly set shell type
config-typing-speed-global - Set global TypingSpeed early
config-dimensions-explicit - Set explicit terminal dimensions
config-comments-document - Use comments to document tape structure
2. Dependency Management (CRITICAL)
deps-require-early - Use Require for dependency validation
deps-require-order - Place Require before settings
deps-require-all - Require all external commands
deps-system-requirements - Verify system dependencies
3. Command Syntax (HIGH)
cmd-type-syntax - Use correct Type command syntax
cmd-enter-explicit - Always follow Type with Enter
cmd-key-repeat - Use key repeat counts
cmd-ctrl-combinations - Use Ctrl combinations for terminal control
cmd-hide-show - Use Hide/Show for sensitive operations
cmd-env-variables - Use Env for environment variables
cmd-screenshot - Use Screenshot for static captures
cmd-multiline-type - Handle multiline commands properly
4. Timing & Synchronization (HIGH)
timing-sleep-after-enter - Add Sleep after commands for output
timing-wait-pattern - Use Wait for dynamic command completion
timing-type-speed-override - Override TypingSpeed for emphasis
timing-sleep-units - Use explicit time units
timing-final-sleep - End recordings with final Sleep
timing-natural-pauses - Add natural pauses between actions
timing-wait-timeout - Set appropriate Wait timeouts
timing-playback-speed - Use PlaybackSpeed for final adjustments
5. Output Optimization (MEDIUM-HIGH)
output-format-selection - Choose output format based on use case
output-framerate - Optimize framerate for file size
output-dimensions-optimize - Right-size terminal dimensions
output-loop-offset - Use LoopOffset for seamless loops
output-multiple-formats - Generate multiple output formats
output-relative-paths - Use relative paths for portability
6. Visual Quality (MEDIUM)
visual-font-readable - Choose readable font settings
visual-theme-selection - Select appropriate theme
visual-window-decoration - Add window decorations for polish
visual-spacing - Adjust letter and line spacing
visual-padding-margin - Use padding and margins effectively
visual-cursor-visibility - Ensure cursor visibility
7. CI/Automation (MEDIUM)
ci-github-action - Use official VHS GitHub Action
ci-auto-commit - Auto-commit generated assets
ci-golden-files - Use golden files for integration testing
ci-matrix-builds - Generate platform-specific demos
ci-caching - Cache VHS dependencies in CI
8. Advanced Patterns (LOW)
advanced-source-include - Use Source for reusable tape components
advanced-clipboard - Use Copy and Paste for complex input
advanced-recording-live - Record live sessions then edit
advanced-server-mode - Use server mode for remote access
How to Use

Read individual reference files for detailed explanations and code examples:

Section definitions - Category structure and impact levels
Rule template - Template for adding new rules
Reference Files
File	Description
AGENTS.md	Complete compiled guide with all rules
references/_sections.md	Category definitions and ordering
assets/templates/_template.md	Template for new rules
metadata.json	Version and reference information
Weekly Installs
165
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass