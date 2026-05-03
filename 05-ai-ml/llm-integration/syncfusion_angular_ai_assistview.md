---
rating: ⭐⭐
title: syncfusion-angular-ai-assistview
url: https://skills.sh/syncfusion/angular-ui-components-skills/syncfusion-angular-ai-assistview
---

# syncfusion-angular-ai-assistview

skills/syncfusion/angular-ui-components-skills/syncfusion-angular-ai-assistview
syncfusion-angular-ai-assistview
Installation
$ npx skills add https://github.com/syncfusion/angular-ui-components-skills --skill syncfusion-angular-ai-assistview
SKILL.md
Syncfusion Angular AI AssistView Component
Component Overview

The Syncfusion AI AssistView is a powerful Angular component that provides a ready-to-use interface for building conversational AI applications.

Key Capabilities:

Conversation Management - Manage prompt-response pairs with history, persistence, and markdown rendering
AI Service Integration - Connect to OpenAI, Gemini, Ollama, Lite-LLM, and MCP providers with streaming support
Speech Features - Built-in speech-to-text with 11 configurable properties and 4 events
Toolbar System - Four toolbar types (header, prompt, response, footer) with custom actions and tag directives
View Management - Multiple views with programmatic activeView control and dynamic switching
Events & Interactions - Typed event arguments (PromptRequestEventArgs, PromptChangedEventArgs, StopRespondingEventArgs)
File Attachments - Support for file uploads with type/size restrictions and attachment click events
Templates - Customize prompts, responses, suggestions, and banners with flexible templates
Methods - Programmatically add/update responses, execute prompts, and control component behavior
Globalization - Full RTL support and localization for 12+ languages with locale-based formatting
Customizable UI - Height, width, CSS classes, HTML attributes, and theme customization
Documentation and Navigation Guide
Getting Started

📄 Read: references/getting-started.md

Installation and dependency setup
Angular environment configuration
Basic component initialization
CSS imports and theme configuration
First working example
Core Features & Conversation Management

📄 Read: references/assist-view-basics.md

Setting prompt text and placeholders
Managing prompt-response collections
Markdown response rendering
Configuring prompt suggestions
Customizing user and assistant avatars
UI controls (clear button, scroll-to-bottom)
Component configuration (height, width, showHeader, cssClass, htmlAttributes)
State persistence with enablePersistence
Globalization and localization (locale property with 12+ languages)
RTL support with enableRtl for Arabic, Hebrew, Persian, Urdu
Appearance & Styling

📄 Read: references/appearance-customization.md

Setting component width and height
Applying custom CSS classes
Theme customization
Responsive design patterns
Multiple Views & Custom Content

📄 Read: references/custom-views.md

Adding custom view models
View types (Assist and Custom)
View configuration and naming
Managing multiple views within one component
Programmatic view switching with activeView property
Dynamic view navigation patterns
View history and breadcrumb navigation
Workflow-based view switching
Conditional view display based on user roles
Programmatic Control & Methods

📄 Read: references/methods-and-actions.md

Adding prompt responses (string and object
Complete event arguments reference section
PromptRequestEventArgs with 6 properties (prompt, attachedFiles, promptSuggestions, cancel, etc.)
PromptChangedEventArgs with 5 properties (value, previousValue, element, event)
StopRespondingEventArgs for canceling responses
AttachmentClickEventArgs with FileInfo interface
Production-ready examples with all event types formats)
Executing prompts dynamically
Response handling patterns
Programmatic interaction
Complete documentation for all 4 toolbar types
Header Toolbar (toolbarSettings) - Global actions and navigation
Prompt Toolbar (promptToolbarSettings) - Actions on user prompts
Response Toolbar (responseToolbarSettings) - Actions on AI responses
Footer Toolbar (footerToolbarSettings) - Input area customization
ToolbarItemModel interface with 10 properties
ToolbarItemClickedEventArgs with dataIndex handling
Tag directive approach: <e-toolbarsettings>, <e-toolbaritem>
Property binding approach for dynamic toolbar items
Common patterns, best practices, and troubleshootingest, promptChanged)
File upload events (beforeAttachmentUpload, attachmentUploadSuccess)
Event handling patterns and best practices
File Attachments

📄 Read: references/file-attachments.md

File attachment configuration
Upload handling and validation
File size and type restrictions
Attachment display and management
Toolbar Configuration

📄 Read: references/toolbar-items.md

Toolbar customization
Built-in speech-to-text with speechToTextSettings (recommended approach)
SpeechToTextSettingsModel with 11 configurable properties
ButtonSettingsModel and TooltipSettingsModel interfaces
4 speech events: onStart, onStop, transcriptChanged, onError
Event arguments: StartListeningEventArgs, StopListeningEventArgs, TranscriptChangedEventArgs, ErrorEventArgs
Language support with 10+ language codes (en-US, es-ES, fr-FR, de-DE, ja-JP, etc.)
Interim results handling with allowInterimResults
Custom Web Speech API implementation (alternative approach)
Text-to-speech setup and configuration
Browser compatibility and error handling
Templates & Custom Rendering

📄 Read: references/templates.md

Template system overview
Prompt templates
Response templates
Custom template creation
AI Service Integration

📄 Read: references/ai-integrations.md

Azure OpenAI integration setup
Gemini integration
Lite-LLM integration
Model Context Protocol (MCP) integration
Ollama integration
Security best practices and API management
Speech Features

📄 Read: references/speech-features.md

Speech-to-text setup and configuration
Text-to-speech setup and configuration
Audio handling
Browser compatibility considerations
Quick Start Example

Here's a minimal working example to get started:

import { Component } from '@angular/core';
import { AIAssistViewModule } from '@syncfusion/ej2-angular-interactive-chat';

@Component({
  imports: [AIAssistViewModule],
  standalone: true,
  selector: 'app-root',
  template: `
    <div ejs-aiassistview 
      id='aiAssistView'
      [promptSuggestions]="suggestions"
      (promptRequest)="onPromptRequest($event)">
    </div>
  `,
  styles: [`
    :host ::ng-deep #aiAssistView {
      height: 100vh;
    }
  `]
})
export class AppComponent {
  suggestions = [
    'What is Angular?',
    'How to create components?',
    'Explain dependency injection'
  ];

  onPromptRequest(args: any) {
    // Handle prompt and provide response
    setTimeout(() => {
      const response = 'This is a sample response from your AI service.';
      // Add response using component method
    }, 1000);
  }
}

Common Patterns
Pattern 1: Basic Conversation Flow
Initialize component with suggestions
User enters prompt
promptRequest event fires
Call your AI service
Use addPromptResponse() to display result
Conversation history maintained automatically
Pattern 2: AI Service Integration with Streaming
Enable streaming with [enableStreaming]="true"
Configure AI provider credentials (OpenAI, Gemini, etc.)
In promptRequest event, call provider API with streaming
Use ReadableStream for chunked responses
Handle stopRespondingClick event for cancellation
Update UI with addPromptResponse() incrementally
Pattern 3: Custom View Management with activeView
Define multiple view types (Assist, Custom)
Use [activeView]="currentIndex" to control display
Switch between views programmatically based on user action
Track view history for back/forward navigation
Each view can have different configuration
Maintain separate state per view
Pattern 4: Complete Toolbar Configuration
Configure header toolbar for global actions (new chat, export, settings)
Set up prompt toolbar for user prompt actions (edit, copy, retry)
Add response toolbar for AI response actions (copy, regenerate, like/dislike)
Configure footer toolbar for input actions (formatting, attachments)
Use tag directive or property binding approach
Handle itemClicked events with dataIndex for context
Pattern 5: Speech-Enabled Interface
Configure speechToTextSettings with language and options
Enable allowInterimResults for real-time transcription
Handle speech events: onStart, onStop, transcriptChanged, onError
Automatically submit recognized text as prompts
Provide visual feedback during listening state
Pattern 6: Event-Driven Actions with Typed Arguments
Use PromptRequestEventArgs to access prompt, attachedFiles, and cancel flag
Use PromptChangedEventArgs for real-time input validation
Handle StopRespondingEventArgs to cancel long-running requests
Use beforeAttachmentUpload for file validation 5
Common Patterns
Pattern 1: Basic Conversation Flowstreaming responses, multi-language support, and toolbar actions
Code Assistant: Create coding helpers with syntax highlighting, code regeneration, and like/dislike feedback
Voice-Enabled Assistant: Implement hands-free interfaces with built-in speech-to-text in 10+ languages
Content Writer Assistant: Implement writing tools with grammar checking, real-time suggestions, and response streaming
Data Analysis Tool: Create interfaces with multiple views (query, results, visualization) and view switching
Learning Platform: Build educational assistants with RTL support for Arabic/Hebrew learners and persistent conversation history
Multi-language Support: Implement interfaces with locale configuration for 12+ languages and RTL text direction
Accessibility Assistant: Provide reading aid with speech features, keyboard navigation, and ARIA attributes
Workflow Applications: Build step-by-step wizards with programmatic view control and conditional navigation
Real-time AI Services: Integrate streaming AI providers with abort functionality and visual streaming indicatorser input | | promptSuggestions | string[] | [] | Provide quick starting prompts | | prompts | object[] | [] | Initialize conversation history | | showClearButton | boolean | false | Show button to clear input | | enableScrollToBottom | boolean | true | Show scroll-to-bottom indicator |
Layout & Appearance
Property	Type	Default	When to Use
width	string | number	'100%'	Set container width
height	string | number	'100%'	Set container height
cssClass	string	''	Apply custom CSS styling and themes
showHeader	boolean	true	Control header visibility
htmlAttributes	object	{}	Add custom HTML attributes (aria-, data-, etc.)
Streaming & Features
Property	Type	Default	When to Use
enableStreaming	boolean	false	Enable real-time streaming responses
speechToTextSettings	SpeechToTextSettingsModel	null	Configure built-in speech recognition
activeView	number	0	Programmatically switch between views
Globalization
Property	Type	Default	When to Use
locale	string	'en-US'	Set language/culture (en-US, es-ES, fr-FR, de-DE, ja-JP, ar-SA, etc.)
enableRtl	boolean	false	Enable right-to-left text direction (Arabic, Hebrew, Persian, Urdu)
enablePersistence	boolean	false	Save component state between page reloads
Toolbar Configuration
Property	Type	Default	When to Use
toolbarSettings	ToolbarSettingsModel	null	Configure header toolbar (global actions)
promptToolbarSettings	PromptToolbarSettingsModel	null	Configure prompt toolbar (edit, copy, retry)
responseToolbarSettings	ResponseToolbarSettingsModel	null	Configure response toolbar (copy, regenerate, like/dislike)
footerToolbarSettings	FooterToolbarSettingsModel	null	Configure footer toolbar (formatting, attachments)
Pattern 3: Custom View Management
Define multiple view types (Assist, Custom)
Switch between views based on user action
Each view can have different configuration
Maintain separate state per view
Pattern 4: Event-Driven Actions
Listen to promptChanged for input validation
Handle beforeAttachmentUpload for file validation
Use attachmentUploadSuccess for post-upload actions
Leverage created event for initialization
Key Properties
Property	Type	Default	When to Use
prompt	string	''	Pre-fill prompt text
promptPlaceholder	string	'Type prompt for assistance...'	Guide user input
promptSuggestions	string[]	[]	Provide quick starting prompts
prompts	object[]	[]	Initialize conversation history
width	string	'100%'	Set container width
height	string	'100%'	Set container height
cssClass	string	''	Apply custom CSS styling
showClearButton	boolean	false	Show button to clear input
enableScrollToBottom	boolean	true	Show scroll-to-bottom indicator
Common Use Cases
Customer Support Chatbot: Build customer service interfaces with knowledge base integration
Code Assistant: Create coding helpers with AI that can review and suggest code
Content Writer Assistant: Implement writing tools with grammar and style suggestions
Data Analysis Tool: Create interfaces for users to query and analyze data through natural language
Learning Platform: Build educational assistants that answer student questions
Internal Knowledge Bot: Create enterprise assistants for company documentation and FAQs
Multi-language Support: Implement translation and localization features
Accessibility Assistant: Provide reading aid or instruction assistance
Weekly Installs
49
Repository
syncfusion/angu…s-skills
First Seen
Mar 25, 2026
Security Audits
Gen Agent Trust HubPass
SnykWarn