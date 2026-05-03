---
title: natural-language
url: https://skills.sh/dpearson2699/swift-ios-skills/natural-language
---

# natural-language

skills/dpearson2699/swift-ios-skills/natural-language
natural-language
Installation
$ npx skills add https://github.com/dpearson2699/swift-ios-skills --skill natural-language
SKILL.md
NaturalLanguage + Translation

Analyze natural language text for tokenization, part-of-speech tagging, named entity recognition, sentiment analysis, language identification, and word/sentence embeddings. Translate text between languages with the Translation framework. Targets Swift 6.3 / iOS 26+.

This skill covers two related frameworks: NaturalLanguage (NLTokenizer, NLTagger, NLEmbedding) for on-device text analysis, and Translation (TranslationSession, LanguageAvailability) for language translation.

Contents
Setup
Tokenization
Language Identification
Part-of-Speech Tagging
Named Entity Recognition
Sentiment Analysis
Text Embeddings
Translation
Common Mistakes
Review Checklist
References
Setup

Import NaturalLanguage for text analysis and Translation for language translation. No special entitlements or capabilities are required for NaturalLanguage. Translation requires iOS 17.4+ / macOS 14.4+.

import NaturalLanguage
import Translation


NaturalLanguage classes (NLTokenizer, NLTagger) are not thread-safe. Use each instance from one thread or dispatch queue at a time.

Tokenization

Segment text into words, sentences, or paragraphs with NLTokenizer.

import NaturalLanguage

func tokenizeWords(in text: String) -> [String] {
    let tokenizer = NLTokenizer(unit: .word)
    tokenizer.string = text

    let range = text.startIndex..<text.endIndex
    return tokenizer.tokens(for: range).map { String(text[$0]) }
}

Token Units
Unit	Description
.word	Individual words
.sentence	Sentences
.paragraph	Paragraphs
.document	Entire document
Enumerating with Attributes

Use enumerateTokens(in:using:) to detect numeric or emoji tokens.

let tokenizer = NLTokenizer(unit: .word)
tokenizer.string = text

tokenizer.enumerateTokens(in: text.startIndex..<text.endIndex) { range, attributes in
    if attributes.contains(.numeric) {
        print("Number: \(text[range])")
    }
    return true // continue enumeration
}

Language Identification

Detect the dominant language of a string with NLLanguageRecognizer.

func detectLanguage(for text: String) -> NLLanguage? {
    NLLanguageRecognizer.dominantLanguage(for: text)
}

// Multiple hypotheses with confidence scores
func languageHypotheses(for text: String, max: Int = 5) -> [NLLanguage: Double] {
    let recognizer = NLLanguageRecognizer()
    recognizer.processString(text)
    return recognizer.languageHypotheses(withMaximum: max)
}


Constrain the recognizer to expected languages for better accuracy on short text.

let recognizer = NLLanguageRecognizer()
recognizer.languageConstraints = [.english, .french, .spanish]
recognizer.processString(text)
let detected = recognizer.dominantLanguage

Part-of-Speech Tagging

Identify nouns, verbs, adjectives, and other lexical classes with NLTagger.

func tagPartsOfSpeech(in text: String) -> [(String, NLTag)] {
    let tagger = NLTagger(tagSchemes: [.lexicalClass])
    tagger.string = text

    var results: [(String, NLTag)] = []
    let range = text.startIndex..<text.endIndex
    let options: NLTagger.Options = [.omitPunctuation, .omitWhitespace]

    tagger.enumerateTags(in: range, unit: .word, scheme: .lexicalClass, options: options) { tag, tokenRange in
        if let tag {
            results.append((String(text[tokenRange]), tag))
        }
        return true
    }
    return results
}

Common Tag Schemes
Scheme	Output
.lexicalClass	Part of speech (noun, verb, adjective)
.nameType	Named entity type (person, place, organization)
.nameTypeOrLexicalClass	Combined NER + POS
.lemma	Base form of a word
.language	Per-token language
.sentimentScore	Sentiment polarity score
Named Entity Recognition

Extract people, places, and organizations.

func extractEntities(from text: String) -> [(String, NLTag)] {
    let tagger = NLTagger(tagSchemes: [.nameType])
    tagger.string = text

    var entities: [(String, NLTag)] = []
    let options: NLTagger.Options = [.omitPunctuation, .omitWhitespace, .joinNames]

    tagger.enumerateTags(
        in: text.startIndex..<text.endIndex,
        unit: .word,
        scheme: .nameType,
        options: options
    ) { tag, tokenRange in
        if let tag, tag != .other {
            entities.append((String(text[tokenRange]), tag))
        }
        return true
    }
    return entities
}
// NLTag values: .personalName, .placeName, .organizationName

Sentiment Analysis

Score text sentiment from -1.0 (negative) to +1.0 (positive).

func sentimentScore(for text: String) -> Double? {
    let tagger = NLTagger(tagSchemes: [.sentimentScore])
    tagger.string = text

    let (tag, _) = tagger.tag(
        at: text.startIndex,
        unit: .paragraph,
        scheme: .sentimentScore
    )
    return tag.flatMap { Double($0.rawValue) }
}

Text Embeddings

Measure semantic similarity between words or sentences with NLEmbedding.

func wordSimilarity(_ word1: String, _ word2: String) -> Double? {
    guard let embedding = NLEmbedding.wordEmbedding(for: .english) else { return nil }
    return embedding.distance(between: word1, and: word2, distanceType: .cosine)
}

func findSimilarWords(to word: String, count: Int = 5) -> [(String, Double)] {
    guard let embedding = NLEmbedding.wordEmbedding(for: .english) else { return [] }
    return embedding.neighbors(for: word, maximumCount: count, distanceType: .cosine)
}


Sentence embeddings compare entire sentences.

func sentenceSimilarity(_ s1: String, _ s2: String) -> Double? {
    guard let embedding = NLEmbedding.sentenceEmbedding(for: .english) else { return nil }
    return embedding.distance(between: s1, and: s2, distanceType: .cosine)
}

Translation
System Translation Overlay

Show the built-in translation UI with .translationPresentation().

import SwiftUI
import Translation

struct TranslatableView: View {
    @State private var showTranslation = false
    let text = "Hello, how are you?"

    var body: some View {
        Button { showTranslation = true } label: {
            Text(text)
        }
        .buttonStyle(.plain)
        .translationPresentation(
            isPresented: $showTranslation,
            text: text
        )
    }
}

Programmatic Translation

Use .translationTask() for programmatic translations within a view context.

struct TranslatingView: View {
    @State private var translatedText = ""
    @State private var configuration: TranslationSession.Configuration?

    var body: some View {
        VStack {
            Text(translatedText)
            Button("Translate") {
                configuration = .init(source: Locale.Language(identifier: "en"),
                                      target: Locale.Language(identifier: "es"))
            }
        }
        .translationTask(configuration) { session in
            let response = try await session.translate("Hello, world!")
            translatedText = response.targetText
        }
    }
}

Batch Translation

Translate multiple strings in a single session.

.translationTask(configuration) { session in
    let requests = texts.enumerated().map { index, text in
        TranslationSession.Request(sourceText: text,
                                    clientIdentifier: "\(index)")
    }
    let responses = try await session.translations(from: requests)
    for response in responses {
        print("\(response.sourceText) -> \(response.targetText)")
    }
}

Checking Language Availability
let availability = LanguageAvailability()
let status = await availability.status(
    from: Locale.Language(identifier: "en"),
    to: Locale.Language(identifier: "ja")
)
switch status {
case .installed: break    // Ready to translate offline
case .supported: break    // Needs download
case .unsupported: break  // Language pair not available
}

Common Mistakes
DON'T: Share NLTagger/NLTokenizer across threads

These classes are not thread-safe and will produce incorrect results or crash.

// WRONG
let sharedTagger = NLTagger(tagSchemes: [.lexicalClass])
DispatchQueue.concurrentPerform(iterations: 10) { _ in
    sharedTagger.string = someText  // Data race
}

// CORRECT
await withTaskGroup(of: Void.self) { group in
    for _ in 0..<10 {
        group.addTask {
            let tagger = NLTagger(tagSchemes: [.lexicalClass])
            tagger.string = someText
            // process...
        }
    }
}

DON'T: Confuse NaturalLanguage with Core ML

NaturalLanguage provides built-in linguistic analysis. Use Core ML for custom trained models. They complement each other via NLModel.

// WRONG: Trying to do NER with raw Core ML
let coreMLModel = try MLModel(contentsOf: modelURL)

// CORRECT: Use NLTagger for built-in NER
let tagger = NLTagger(tagSchemes: [.nameType])

// Or load a custom Core ML model via NLModel
let nlModel = try NLModel(mlModel: coreMLModel)
tagger.setModels([nlModel], forTagScheme: .nameType)

DON'T: Assume embeddings exist for all languages

Not all languages have word or sentence embeddings available on device.

// WRONG: Force unwrap
let embedding = NLEmbedding.wordEmbedding(for: .japanese)!

// CORRECT: Handle nil
guard let embedding = NLEmbedding.wordEmbedding(for: .japanese) else {
    // Embedding not available for this language
    return
}

DON'T: Create a new tagger per token

Creating and configuring a tagger is expensive. Reuse it for the same text.

// WRONG: New tagger per word
for word in words {
    let tagger = NLTagger(tagSchemes: [.lexicalClass])
    tagger.string = word
}

// CORRECT: Set string once, enumerate
let tagger = NLTagger(tagSchemes: [.lexicalClass])
tagger.string = fullText
tagger.enumerateTags(in: fullText.startIndex..<fullText.endIndex,
                     unit: .word, scheme: .lexicalClass, options: []) { tag, range in
    return true
}

DON'T: Ignore language hints for short text

Language detection on short strings (under ~20 characters) is unreliable. Set constraints or hints to improve accuracy.

// WRONG: Detect language of a single word
let lang = NLLanguageRecognizer.dominantLanguage(for: "chat")  // French or English?

// CORRECT: Provide context
let recognizer = NLLanguageRecognizer()
recognizer.languageHints = [.english: 0.8, .french: 0.2]
recognizer.processString("chat")

Review Checklist
 NLTokenizer and NLTagger instances used from a single thread
 Tagger created once per text, not per token
 Language detection uses constraints/hints for short text
 NLEmbedding availability checked before use (returns nil if unavailable)
 Translation LanguageAvailability checked before attempting translation
 .translationTask() used within a SwiftUI view hierarchy
 Batch translation uses clientIdentifier to match responses to requests
 Sentiment scores handled as optional (may return nil for unsupported languages)
 .joinNames option used with NER to keep multi-word names together
 Custom ML models loaded via NLModel, not raw Core ML
References
Extended patterns (custom models, contextual embeddings, gazetteers): references/translation-patterns.md
Natural Language framework
NLTokenizer
NLTagger
NLEmbedding
NLLanguageRecognizer
Translation framework
TranslationSession
LanguageAvailability
Weekly Installs
1.1K
Repository
dpearson2699/sw…s-skills
GitHub Stars
512
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass