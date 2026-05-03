---
rating: ⭐⭐⭐
title: rust-errors
url: https://skills.sh/epicenterhq/epicenter/rust-errors
---

# rust-errors

skills/epicenterhq/epicenter/rust-errors
rust-errors
Installation
$ npx skills add https://github.com/epicenterhq/epicenter --skill rust-errors
SKILL.md
Rust to TypeScript Error Handling
Reference Repositories
Tauri — Desktop app framework (source of Rust-to-TypeScript error patterns)
When to Apply This Skill

Use this pattern when you need to:

Send Rust errors through Tauri commands to TypeScript clients.
Define Rust enums that serialize into discriminated union error shapes.
Validate unknown error payloads in TypeScript before switching on variants.
Keep cross-language error payloads consistent with name and message fields.
Avoid serde tagging patterns that produce nested, awkward TypeScript shapes.
Discriminated Union Pattern for Errors

When passing errors from Rust to TypeScript through Tauri commands, use internally-tagged enums to create discriminated unions that TypeScript can handle naturally.

Rust Error Definition
use serde::{Deserialize, Serialize};
use thiserror::Error;

#[derive(Error, Debug, Serialize, Deserialize)]
#[serde(tag = "name")]
pub enum TranscriptionError {
    #[error("Audio read error: {message}")]
    AudioReadError { message: String },

    #[error("GPU error: {message}")]
    GpuError { message: String },

    #[error("Model load error: {message}")]
    ModelLoadError { message: String },

    #[error("Transcription error: {message}")]
    TranscriptionError { message: String },
}

Key Rust Patterns
Use internally tagged enums: #[serde(tag = "name")] creates a discriminator field
Follow naming conventions: Enum variants should be PascalCase
Include structured data: Each variant can have fields like message: String
Single-variant enums are okay: Use when you want consistent error structure
// Single-variant enum for consistency
#[derive(Error, Debug, Serialize, Deserialize)]
#[serde(tag = "name")]
enum ArchiveExtractionError {
    #[error("Archive extraction failed: {message}")]
    ArchiveExtractionError { message: String },
}

TypeScript Error Handling
import { type } from 'arktype';

// Define the error type to match Rust serialization
const TranscriptionErrorType = type({
	name: "'AudioReadError' | 'GpuError' | 'ModelLoadError' | 'TranscriptionError'",
	message: 'string',
});

// Use in error handling
const result = await tryAsync({
	try: () => invoke('transcribe_audio_whisper', params),
	catch: (unknownError) => {
		const result = TranscriptionErrorType(unknownError);
		if (result instanceof type.errors) {
			// Handle unexpected error shape
			return WhisperingErr({
				title: 'Unexpected Error',
				description: extractErrorMessage(unknownError),
				action: { type: 'more-details', error: unknownError },
			});
		}

		const error = result;
		// Now we have properly typed discriminated union
		switch (error.name) {
			case 'ModelLoadError':
				return WhisperingErr({
					title: 'Model Loading Error',
					description: error.message,
					action: {
						type: 'more-details',
						error: new Error(error.message),
					},
				});

			case 'GpuError':
				return WhisperingErr({
					title: 'GPU Error',
					description: error.message,
					action: {
						type: 'link',
						label: 'Configure settings',
						href: '/settings/transcription',
					},
				});

			// Handle other cases...
		}
	},
});

Serialization Format

The Rust enum serializes to this TypeScript-friendly format:

// AudioReadError variant
{ "name": "AudioReadError", "message": "Failed to decode audio file" }

// GpuError variant
{ "name": "GpuError", "message": "GPU acceleration failed" }

Best Practices
Consistent error structure: All errors have the same shape with name and message
TypeScript type safety: Use runtime validation with arktype to ensure type safety
Exhaustive handling: Switch statements provide compile-time exhaustiveness checking
Don't use content attribute: Avoid #[serde(tag = "name", content = "data")] as it creates nested structures
Keep enums private when possible: Only make public if used across modules
Anti-Patterns to Avoid
// DON'T: External tagging (default behavior)
#[derive(Serialize)]
pub enum BadError {
    ModelLoadError { message: String }
}
// Produces: { "ModelLoadError": { "message": "..." } }

// DON'T: Adjacent tagging with content
#[derive(Serialize)]
#[serde(tag = "type", content = "data")]
pub enum BadError {
    ModelLoadError { message: String }
}
// Produces: { "type": "ModelLoadError", "data": { "message": "..." } }

// DON'T: Manual Serialize implementation when derive works
impl Serialize for MyError {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error> {
        // Unnecessary complexity
    }
}


This pattern ensures clean, type-safe error handling across the Rust-TypeScript boundary with minimal boilerplate and maximum type safety.

Weekly Installs
77
Repository
epicenterhq/epicenter
GitHub Stars
4.5K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass