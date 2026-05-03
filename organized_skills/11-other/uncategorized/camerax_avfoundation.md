---
rating: ⭐⭐
title: camerax_avfoundation
url: https://skills.sh/davidcastagnetoa/skills/camerax_avfoundation
---

# camerax_avfoundation

skills/davidcastagnetoa/skills/camerax_avfoundation
camerax_avfoundation
Installation
$ npx skills add https://github.com/davidcastagnetoa/skills --skill camerax_avfoundation
SKILL.md
camerax_avfoundation

CameraX (Android) y AVFoundation (iOS) proporcionan acceso directo al hardware de cámara del dispositivo, permitiendo capturar video en vivo y bloquear el acceso a la galería de fotos durante la verificación KYC.

When to use

Usar en el capture_agent para la captura de selfie y documento en apps móviles nativas (React Native / Flutter). Complementa a WebRTC que se usa en la versión web.

Instructions
React Native: usar react-native-camera o expo-camera que abstrae CameraX/AVFoundation.
Configurar permisos: CAMERA en AndroidManifest.xml y NSCameraUsageDescription en Info.plist.
Bloquear el acceso a galería: no usar ImagePicker, solo captura en vivo.
Configurar resolución mínima: 720p para selfie, 1080p para documento.
Capturar secuencia de frames (3-5 segundos) para liveness, no solo un snapshot.
Validar que el dispositivo tiene cámara frontal disponible antes de iniciar.
Implementar overlay guiado para alinear el documento dentro del frame.
Notes
CameraX simplifica el manejo de lifecycle en Android (auto-bind al lifecycle del fragment).
En Flutter, usar camera plugin oficial que soporta ambas plataformas.
Detectar cámaras virtuales verificando el nombre del dispositivo de cámara contra una lista negra.
Weekly Installs
12
Repository
davidcastagnetoa/skills
First Seen
Mar 3, 2026