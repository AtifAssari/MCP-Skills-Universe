---
title: musickit
url: https://skills.sh/dpearson2699/swift-ios-skills/musickit
---

# musickit

skills/dpearson2699/swift-ios-skills/musickit
musickit
Installation
$ npx skills add https://github.com/dpearson2699/swift-ios-skills --skill musickit
SKILL.md
MusicKit

Search the Apple Music catalog, manage playback with ApplicationMusicPlayer, check subscriptions, and publish Now Playing metadata via MPNowPlayingInfoCenter and MPRemoteCommandCenter. Targets Swift 6.3 / iOS 26+.

Contents
Setup
Authorization
Catalog Search
Subscription Checks
Playback with ApplicationMusicPlayer
Queue Management
Now Playing Info
Remote Command Center
Common Mistakes
Review Checklist
References
Setup
Project Configuration
Enable the MusicKit capability in Xcode (adds the com.apple.developer.musickit entitlement)
Add NSAppleMusicUsageDescription to Info.plist explaining why the app accesses Apple Music
For background playback, add the audio background mode to UIBackgroundModes
Imports
import MusicKit       // Catalog, auth, playback
import MediaPlayer    // MPRemoteCommandCenter, MPNowPlayingInfoCenter

Authorization

Request permission before accessing the user's music data or playing Apple Music content. Authorization is a one-time prompt per app install.

func requestMusicAccess() async -> MusicAuthorization.Status {
    let status = await MusicAuthorization.request()
    switch status {
    case .authorized:
        // Full access to MusicKit APIs
        break
    case .denied, .restricted:
        // Show guidance to enable in Settings
        break
    case .notDetermined:
        break
    @unknown default:
        break
    }
    return status
}

// Check current status without prompting
let current = MusicAuthorization.currentStatus

Catalog Search

Use MusicCatalogSearchRequest to search the Apple Music catalog. The user must have an Apple Music subscription for full catalog access.

func searchCatalog(term: String) async throws -> MusicItemCollection<Song> {
    var request = MusicCatalogSearchRequest(term: term, types: [Song.self])
    request.limit = 25

    let response = try await request.response()
    return response.songs
}

Displaying Results
for song in songs {
    print("\(song.title) by \(song.artistName)")
    if let artwork = song.artwork {
        let url = artwork.url(width: 300, height: 300)
        // Load artwork from url
    }
}

Subscription Checks

Check whether the user has an active Apple Music subscription before offering playback features.

func checkSubscription() async throws -> Bool {
    let subscription = try await MusicSubscription.current
    return subscription.canPlayCatalogContent
}

// Observe subscription changes
func observeSubscription() async {
    for await subscription in MusicSubscription.subscriptionUpdates {
        if subscription.canPlayCatalogContent {
            // Enable full playback UI
        } else {
            // Show subscription offer
        }
    }
}

Offering Apple Music

Present the Apple Music subscription offer sheet when the user is not subscribed.

import MusicKit
import SwiftUI

struct MusicOfferView: View {
    @State private var showOffer = false

    var body: some View {
        Button("Subscribe to Apple Music") {
            showOffer = true
        }
        .musicSubscriptionOffer(isPresented: $showOffer)
    }
}

Playback with ApplicationMusicPlayer

ApplicationMusicPlayer plays Apple Music content independently from the Music app. It does not affect the system player's state.

let player = ApplicationMusicPlayer.shared

func playSong(_ song: Song) async throws {
    player.queue = [song]
    try await player.play()
}

func pause() {
    player.pause()
}

func skipToNext() async throws {
    try await player.skipToNextEntry()
}

Observing Playback State
func observePlayback() {
    // player.state is an @Observable property
    let state = player.state
    switch state.playbackStatus {
    case .playing:
        break
    case .paused:
        break
    case .stopped, .interrupted, .seekingForward, .seekingBackward:
        break
    @unknown default:
        break
    }
}

Queue Management

Build and manipulate the playback queue using ApplicationMusicPlayer.Queue.

// Initialize with multiple items
func playAlbum(_ album: Album) async throws {
    player.queue = [album]
    try await player.play()
}

// Append songs to the existing queue
func appendToQueue(_ songs: [Song]) async throws {
    try await player.queue.insert(songs, position: .tail)
}

// Insert song to play next
func playNext(_ song: Song) async throws {
    try await player.queue.insert(song, position: .afterCurrentEntry)
}

Now Playing Info

Update MPNowPlayingInfoCenter so the Lock Screen, Control Center, and CarPlay display current track metadata. This is essential when playing custom audio (non-MusicKit sources). ApplicationMusicPlayer handles this automatically for Apple Music content.

import MediaPlayer

func updateNowPlaying(title: String, artist: String, duration: TimeInterval, elapsed: TimeInterval) {
    var info = [String: Any]()
    info[MPMediaItemPropertyTitle] = title
    info[MPMediaItemPropertyArtist] = artist
    info[MPMediaItemPropertyPlaybackDuration] = duration
    info[MPNowPlayingInfoPropertyElapsedPlaybackTime] = elapsed
    info[MPNowPlayingInfoPropertyPlaybackRate] = 1.0
    info[MPNowPlayingInfoPropertyMediaType] = MPNowPlayingInfoMediaType.audio.rawValue

    MPNowPlayingInfoCenter.default().nowPlayingInfo = info
}

func clearNowPlaying() {
    MPNowPlayingInfoCenter.default().nowPlayingInfo = nil
}

Adding Artwork
func setArtwork(_ image: UIImage) {
    let artwork = MPMediaItemArtwork(boundsSize: image.size) { _ in image }
    var info = MPNowPlayingInfoCenter.default().nowPlayingInfo ?? [:]
    info[MPMediaItemPropertyArtwork] = artwork
    MPNowPlayingInfoCenter.default().nowPlayingInfo = info
}

Remote Command Center

Register handlers for MPRemoteCommandCenter to respond to Lock Screen controls, AirPods tap gestures, and CarPlay buttons.

func setupRemoteCommands() {
    let center = MPRemoteCommandCenter.shared()

    center.playCommand.addTarget { _ in
        resumePlayback()
        return .success
    }

    center.pauseCommand.addTarget { _ in
        pausePlayback()
        return .success
    }

    center.nextTrackCommand.addTarget { _ in
        skipToNext()
        return .success
    }

    center.previousTrackCommand.addTarget { _ in
        skipToPrevious()
        return .success
    }

    // Disable commands you do not support
    center.seekForwardCommand.isEnabled = false
    center.seekBackwardCommand.isEnabled = false
}

Scrubbing Support
func enableScrubbing() {
    let center = MPRemoteCommandCenter.shared()
    center.changePlaybackPositionCommand.addTarget { event in
        guard let positionEvent = event as? MPChangePlaybackPositionCommandEvent else {
            return .commandFailed
        }
        seek(to: positionEvent.positionTime)
        return .success
    }
}

Common Mistakes
DON'T: Skip the MusicKit entitlement or usage description

Without the MusicKit entitlement your app crashes at authorization. Without NSAppleMusicUsageDescription, App Review rejects the submission.

// WRONG: No entitlement configured
let status = await MusicAuthorization.request() // Crashes

// CORRECT: Enable MusicKit capability in Xcode first,
// then add NSAppleMusicUsageDescription to Info.plist
let status = await MusicAuthorization.request()

DON'T: Forget to check subscription before playback

Attempting to play catalog content without a subscription silently fails or throws.

// WRONG
func play(_ song: Song) async throws {
    player.queue = [song]
    try await player.play() // Fails if no subscription
}

// CORRECT
func play(_ song: Song) async throws {
    let sub = try await MusicSubscription.current
    guard sub.canPlayCatalogContent else {
        showSubscriptionOffer()
        return
    }
    player.queue = [song]
    try await player.play()
}

DON'T: Use SystemMusicPlayer when you mean ApplicationMusicPlayer

SystemMusicPlayer controls the global Music app queue. Changes affect the user's Music app state. Use ApplicationMusicPlayer for app-scoped playback.

// WRONG: Modifies the user's Music app queue
let player = SystemMusicPlayer.shared

// CORRECT: App-scoped playback
let player = ApplicationMusicPlayer.shared

DON'T: Forget to update Now Playing info when track changes

Stale metadata on the Lock Screen confuses users. Update Now Playing info every time the current track changes.

// WRONG: Set once and forget
updateNowPlaying(title: firstSong.title, ...)

// CORRECT: Update on every track change
func onTrackChanged(_ song: Song) {
    updateNowPlaying(
        title: song.title,
        artist: song.artistName,
        duration: song.duration ?? 0,
        elapsed: 0
    )
}

DON'T: Register remote commands without handling them

Registering a command but returning .commandFailed breaks Lock Screen controls. Disable commands you do not support instead.

// WRONG
center.skipForwardCommand.addTarget { _ in .commandFailed }

// CORRECT
center.skipForwardCommand.isEnabled = false

Review Checklist
 MusicKit capability enabled in Xcode project
 NSAppleMusicUsageDescription added to Info.plist
 MusicAuthorization.request() called before any MusicKit access
 Subscription checked before attempting catalog playback
 ApplicationMusicPlayer used (not SystemMusicPlayer) for app-scoped playback
 Background audio mode enabled if music plays in background
 Now Playing info updated on every track change (for custom audio)
 Remote command handlers return .success for supported commands
 Unsupported remote commands disabled with isEnabled = false
 Artwork provided in Now Playing info for Lock Screen display
 Elapsed playback time updated periodically for scrubber accuracy
 Subscription offer presented when user lacks Apple Music subscription
References
Extended patterns (SwiftUI integration, genre browsing, playlist management): references/musickit-patterns.md
MusicKit framework
MusicAuthorization
ApplicationMusicPlayer
MusicCatalogSearchRequest
MusicSubscription
MPRemoteCommandCenter
MPNowPlayingInfoCenter
NSAppleMusicUsageDescription
Weekly Installs
677
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