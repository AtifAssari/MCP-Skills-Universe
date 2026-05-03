---
rating: ⭐⭐⭐
title: prompt-optimizer
url: https://skills.sh/smallnest/langgraphgo/prompt-optimizer
---

# prompt-optimizer

skills/smallnest/langgraphgo/prompt-optimizer
prompt-optimizer
Installation
$ npx skills add https://github.com/smallnest/langgraphgo --skill prompt-optimizer
SKILL.md
Prompt Optimizer

This skill analyzes user prompts and provides optimized versions that are clearer, more specific, and more actionable.

Purpose

Transform vague, incomplete, or ambiguous user requests into well-structured prompts that lead to better outcomes. By analyzing prompts against quality criteria and providing optimized versions, this skill helps users communicate their needs more effectively.

When to Use This Skill

Use this skill when user prompts exhibit one or more of these issues:

Clarity Issues
Vague language: "something", "thing", "stuff", "it", "this"
Ambiguous pronouns without clear referents
Multiple possible interpretations
Unclear desired outcome
Specificity Issues
Missing context about the problem domain
No technical specifications (language, framework, version)
Lack of examples when examples would help
Undefined scope or boundaries
Completeness Issues
Missing required information or inputs
No success criteria defined
Undefined behavior for edge cases
Missing constraints or requirements
Structure Issues
Disorganized information
Complex requests without clear structure
Mixing context with requests
No logical flow
Actionability Issues
No clear action verb or request
Passive voice making intent unclear
Confusing or conflicting instructions
Missing output format specification
Activation Triggers

Activate this skill when detecting:

Vague words: "something", "thing", "stuff", "it", "this", "that"
Quality indicators: "better", "good", "nice" (without criteria)
Incomplete requests: "help with...", "can you...", "fix..." (without details)
Overly broad requests: "build an app", "create a system"
Missing specifications in technical requests
Requests without clear success criteria
Analysis Workflow

Two modes available:

Mode 1: Interactive Questionnaire (Recommended for Complex Requests)

Use the AskUserQuestion tool to guide users through structured questions. This collaborative approach helps users clarify their needs step-by-step.

When to use: Medium to complex requests, or when user prefers guided interaction.

Mode 2: Direct Analysis (Fast)

Analyze the prompt and provide suggested improvements in one response.

When to use: Simple optimization needs, or when user wants quick results.

Default: Start with Mode 2 (Direct Analysis). If user requests interactive mode or if the request is very complex, switch to Mode 1.

Mode 2: Direct Analysis Workflow
Step 1: Receive and Read the Prompt

Carefully read the user's original prompt to understand their intent.

Step 2: Identify Issues

Systematically check for issues using references/optimization-principles.md:

Clarity Check:

Is the language specific and concrete?
Are all terms clearly defined?
Is there only one reasonable interpretation?

Specificity Check:

Is sufficient context provided?
Are technical requirements specified?
Are examples included when helpful?

Completeness Check:

Is all necessary information present?
Are success criteria defined?
Are edge cases considered?

Structure Check:

Is information organized logically?
Is the request easy to parse?
Is context separated from the task?

Actionability Check:

Is there a clear action requested?
Is the output format specified?
Are instructions unambiguous?
Step 3: Categorize Issues

List all identified issues by category:

Clarity problems: [list]
Specificity gaps: [list]
Completeness deficiencies: [list]
Structure issues: [list]
Actionability concerns: [list]
Step 4: Generate Optimized Prompt

Create an improved version following these principles:

Add Specificity:

Replace vague terms with concrete descriptions
Add missing technical specifications
Include relevant context

Improve Clarity:

Use clear, unambiguous language
Define all terms
Eliminate multiple interpretations

Ensure Completeness:

Add missing requirements
Define success criteria
Specify constraints

Enhance Structure:

Organize information logically
Use bullet points and sections
Separate context from task

Make Actionable:

Start with clear action verb
Specify output format
Provide concrete deliverables

Reference references/optimization-principles.md for patterns and examples.

Step 5: Present Analysis

Provide a structured response:

Original Prompt: Show the user's original request

Identified Issues: List specific problems found

Categorized by type
Brief explanation of each

Optimized Prompt: Provide improved version

Well-structured
Complete
Actionable

Key Improvements: Highlight main changes

What was added
What was clarified
Why it's better

Optional: Offer to refine further or proceed with the optimized prompt

Mode 1: Interactive Questionnaire Workflow
When User Requests Interactive Mode

If the user explicitly asks for interactive/questionnaire mode, or if the prompt has multiple complex issues, use this workflow.

Step 1: Quick Initial Analysis

Quickly identify the main categories of missing information:

Technical specifications needed?
Functional requirements unclear?
Design/styling preferences missing?
Scope or constraints undefined?
Step 2: Design Question Set

Based on the analysis, prepare 1-4 targeted questions using AskUserQuestion tool.

Question Structure:

Each question should have a clear header (max 12 chars)
Provide 2-4 specific options
Include descriptions explaining each option
Allow "Other" for custom input (automatically provided)

Question Categories:

For Code Requests:

Technology Stack (React, Vue, vanilla JS, etc.)
Type System (TypeScript, JavaScript)
Styling Approach (Tailwind, CSS Modules, styled-components, etc.)
Feature Requirements (specific functionality needed)

For Component Requests:

Component Type (Button, Form, Card, Modal, etc.)
Variants Needed (primary/secondary, sizes, states)
Props/API (what should it accept?)
Use Cases (how will it be used?)

For UI/Design Requests:

Platform (Web, Mobile, Desktop app)
Design Style (Modern, Minimal, Colorful, Corporate)
Responsive Needs (Mobile-first, Desktop-only, Adaptive)
Key Features (what must be included?)
Step 3: Use AskUserQuestion Tool

Call the AskUserQuestion tool with structured questions.

Important: Always include a final open-ended question that allows users to add custom requirements using the "Other" option.

AskUserQuestion({
  questions: [
    {
      question: "What technology stack should this use?",
      header: "Tech Stack",
      multiSelect: false,
      options: [
        {
          label: "React + TypeScript",
          description: "Modern React with full type safety"
        },
        {
          label: "React + JavaScript",
          description: "React without TypeScript"
        },
        {
          label: "Vue 3",
          description: "Vue 3 Composition API"
        },
        {
          label: "Vanilla JavaScript",
          description: "Plain JS without frameworks"
        }
      ]
    },
    {
      question: "What styling approach would you like?",
      header: "Styling",
      multiSelect: false,
      options: [
        {
          label: "Tailwind CSS",
          description: "Utility-first CSS framework"
        },
        {
          label: "CSS Modules",
          description: "Scoped CSS with modules"
        },
        {
          label: "styled-components",
          description: "CSS-in-JS solution"
        }
      ]
    },
    {
      question: "Which features are needed?",
      header: "Features",
      multiSelect: true,
      options: [
        {
          label: "Multiple variants",
          description: "Different color/style variants (primary, secondary, etc.)"
        },
        {
          label: "Size options",
          description: "Different sizes (sm, md, lg)"
        },
        {
          label: "Loading state",
          description: "Show spinner during async operations"
        },
        {
          label: "Disabled state",
          description: "Disabled/inactive state"
        }
      ]
    },
    {
      question: "Any additional requirements or constraints?",
      header: "Extra Needs",
      multiSelect: false,
      options: [
        {
          label: "No, that's all",
          description: "I don't need anything else"
        },
        {
          label: "Yes, let me specify",
          description: "I have additional requirements (use 'Other' to describe)"
        }
      ]
    }
  ]
})


Note: The "Other" option is automatically provided by AskUserQuestion tool, allowing users to input custom text for any question.

Step 4: Process Answers

After receiving user's answers:

Extract all selected options from each question
Handle "Other" responses if user provided custom input
Pay special attention to the "Extra Needs" question:
If user selected "Yes, let me specify" and provided text in "Other", include those requirements
If user selected "No, that's all", proceed without additional requirements
Combine all answers with original request
Step 5: Generate Optimized Prompt

Using the gathered information, create a complete, well-structured prompt:

## Optimized Prompt (Based on Your Answers)

[Combine original intent + user's answers into structured prompt]

**Technology**: [Answer 1]
**Styling**: [Answer 2]
**Features**: [Answer 3, Answer 4, ...]

[Full detailed requirements...]

Step 6: Confirm and Proceed

Ask user if the optimized prompt looks good, or if they want to adjust anything:

### Does this look good?

1. ✅ Yes, proceed with this specification
2. 🔄 Let me adjust some details
3. ➕ Add more requirements

Example Interactive Flow

User: "生成个按钮"

Prompt Optimizer (Interactive Mode):

我会通过几个问题来帮你明确需求。

[Calls AskUserQuestion with 4 targeted questions]

Question 1: 使用什么技术栈？
- React + TypeScript
- React + JavaScript
- Vue 3
- Other

Question 2: 使用什么样式方案？
- Tailwind CSS
- CSS Modules
- styled-components
- Other

Question 3: 需要哪些功能？(可多选)
- 多种变体 (primary, secondary, danger等)
- 多种尺寸 (sm, md, lg)
- Loading 状态
- Disabled 状态

Question 4: 还有其他需求或约束吗？
- 不需要，就这些
- 需要，让我补充 (可以在 "Other" 中输入)


Example 1 - User without extra needs: User selects: React + TypeScript, Tailwind CSS, [多种变体, Loading 状态], "不需要，就这些"

Prompt Optimizer:

## 优化后的需求

基于你的选择，这是完整的需求规格：

创建一个 React Button 组件，使用 TypeScript 和 Tailwind CSS。

技术栈：
- React + TypeScript
- Tailwind CSS 样式

功能需求：
- 支持多种变体：primary (蓝色), secondary (灰色), danger (红色)
- 支持 loading 状态（显示 spinner）
- Props 定义：
  - variant: 'primary' | 'secondary' | 'danger'
  - loading?: boolean
  - onClick?: () => void
  - children: React.ReactNode
  - className?: string

这样可以吗？
1. ✅ 可以，开始生成
2. 🔄 我想调整一下


Example 2 - User with extra needs: User selects: React + TypeScript, Tailwind CSS, [多种变体, Loading 状态], "Other: 需要支持图标，并且要有 fullWidth 选项让按钮占满整行"

Prompt Optimizer:

## 优化后的需求

基于你的选择，这是完整的需求规格：

创建一个 React Button 组件，使用 TypeScript 和 Tailwind CSS。

技术栈：
- React + TypeScript
- Tailwind CSS 样式

功能需求：
- 支持多种变体：primary (蓝色), secondary (灰色), danger (红色)
- 支持 loading 状态（显示 spinner）
- ✨ 支持图标显示（用户补充）
- ✨ 支持 fullWidth 选项让按钮占满整行（用户补充）

Props 定义：
  - variant: 'primary' | 'secondary' | 'danger'
  - loading?: boolean
  - icon?: React.ReactNode
  - iconPosition?: 'left' | 'right'
  - fullWidth?: boolean
  - onClick?: () => void
  - children: React.ReactNode
  - className?: string

这样可以吗？
1. ✅ 可以，开始生成
2. 🔄 我想调整一下

Output Format

Structure the output as follows:

## Prompt Analysis

### Original Prompt
[User's original request]

### Identified Issues

**Clarity**:
- [Issue 1]
- [Issue 2]

**Specificity**:
- [Issue 1]
- [Issue 2]

**Completeness**:
- [Issue 1]

[Other categories as applicable]

### Optimized Prompt

[Improved, well-structured version]

### Key Improvements
- ✅ [Improvement 1]
- ✅ [Improvement 2]
- ✅ [Improvement 3]

### Next Steps
Would you like me to:
1. Proceed with the optimized prompt?
2. Refine it further based on your feedback?
3. Focus on a specific aspect?

Example Workflows
Example 1: Vague Code Request

User: "Make a button"

Analysis:

Missing: language/framework
Missing: styling requirements
Missing: functionality details
Missing: props/API

Optimized:

Create a reusable Button component in React with TypeScript and Tailwind CSS.

Requirements:
- Support variants: primary, secondary, danger
- Support sizes: sm, md, lg
- Accept onClick handler and children
- Include loading and disabled states
- Proper TypeScript types for all props

Example usage:
<Button variant="primary" size="md" onClick={handleClick}>
  Click me
</Button>

Example 2: Incomplete Bug Report

User: "The app crashes"

Analysis:

Missing: where/when it crashes
Missing: error message
Missing: reproduction steps
Missing: expected behavior

Optimized:

Debug and fix the crash in the Shopping Cart component.

Current behavior:
- App crashes when clicking "Checkout" button
- Only when cart has more than 5 items
- Console error: "Cannot read property 'price' of undefined"

Location:
- File: src/components/ShoppingCart.tsx
- Started after recent pricing logic refactor

Expected behavior:
- Checkout button should work regardless of cart size
- Should navigate to checkout page

Steps to reproduce:
1. Add 6+ items to cart
2. Click "Checkout" button
3. Observe crash

Example 3: Broad Request

User: "Build a dashboard"

Analysis:

Too broad, no scope
Missing: what data to display
Missing: technical requirements
Missing: design requirements

Optimized:

Create a responsive analytics dashboard with the following requirements:

Data to Display:
- User statistics (total users, active users, new signups)
- Revenue metrics (daily, weekly, monthly)
- Traffic sources (chart showing breakdown)
- Recent activity feed

Technical Requirements:
- React with TypeScript
- Chart library: Chart.js or Recharts
- State management: Zustand
- Styling: Tailwind CSS
- Responsive design (mobile, tablet, desktop)

Features:
- Date range filter
- Data refresh button
- CSV export functionality
- Loading states for data fetching

Layout:
- Grid layout with stat cards at top
- Charts in middle section
- Activity feed on the side or bottom

Quality Criteria Reference

Consult references/optimization-principles.md for:

Prompt Quality Checklist - Systematic evaluation criteria
Common Prompt Patterns - Templates for different request types
Red Flags - Indicators of poor prompt quality
Optimization Strategies - Techniques by problem type
Full Examples - Before/after optimization examples
Special Cases
When the Prompt is Already Good

If the user's prompt is already clear, specific, and complete:

Acknowledge the quality of the prompt
Note what makes it effective
Proceed directly with the task
Don't over-optimize
When Clarification is Needed

If critical information is missing and cannot be reasonably assumed:

Identify what's missing
Ask targeted clarifying questions
Provide options when applicable
Suggest a framework for their answer
When Multiple Interpretations Exist

If the prompt is ambiguous:

Identify the different possible interpretations
Present them clearly to the user
Ask which interpretation is correct
Or suggest the most likely interpretation and ask for confirmation
When the Request is Too Broad

If the scope is unrealistic:

Break it down into phases or components
Suggest starting with a specific part
Provide a prioritized list
Recommend an MVP approach
Integration with Other Skills
Before Other Skills Activate

This skill can serve as a "pre-processor":

Optimize the prompt first
The optimized prompt then triggers appropriate skills
Other skills work with clearer requirements
Working with request-analyzer

When request-analyzer skill is available:

request-analyzer identifies when optimization is needed
prompt-optimizer performs the optimization
request-analyzer can then re-analyze the optimized prompt
Best Practices
Be helpful, not pedantic - Focus on meaningful improvements
Maintain user intent - Don't change what they're asking for
Add value - Only optimize when it genuinely helps
Be concise - Don't over-explain obvious changes
Stay respectful - Frame as helpful enhancement, not criticism
Offer options - When multiple valid interpretations exist
Know when to skip - If prompt is already good, proceed directly
Important Notes
Always preserve the user's core intent and goals
Don't make assumptions about technical choices unless necessary
Clearly mark assumptions when made
Offer to refine based on user feedback
Sometimes asking a clarifying question is better than assuming
Balance between thoroughness and practicality
The goal is better outcomes, not perfect prompts
Weekly Installs
28
Repository
smallnest/langgraphgo
GitHub Stars
240
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass