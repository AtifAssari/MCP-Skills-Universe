---
title: extension-object-storage
url: https://skills.sh/caffeinelabs/skills/extension-object-storage
---

# extension-object-storage

skills/caffeinelabs/skills/extension-object-storage
extension-object-storage
Installation
$ npx skills add https://github.com/caffeinelabs/skills --skill extension-object-storage
SKILL.md
Object Storage

Object storage extension for Caffeine AI.

Overview

This skill adds off-chain file/object storage with on-chain references. The MixinObjectStorage mixin provides infrastructure for file operations; you track uploaded files in your own data structures using Storage.ExternalBlob.

Backend

File content is stored off-chain. The backend manages references to external files using the Storage.ExternalBlob type from mo:caffeineai-object-storage/Storage. The frontend handles the actual upload/download; the backend only stores the reference.

CRITICAL: ANY data field that represents a file, image, photo, document, or media MUST use Storage.ExternalBlob as its type -- NEVER Text. Using Text breaks the upload/download proxy. Method parameters that accept file uploads MUST also use Storage.ExternalBlob, not Text.

Correct:

blob : Storage.ExternalBlob


Wrong:

blobId : Text
imageUrl : Text
fileRef : Text

Module API

The only type you use from mo:caffeineai-object-storage/Storage is ExternalBlob (which is Blob). All other functions in Storage.mo are internal infrastructure used by MixinObjectStorage -- do not call them directly.

Setup in main.mo

include MixinObjectStorage() MUST be placed in main.mo, not in a custom mixin file. Your own file-tracking logic goes in a separate mixin.

import MixinObjectStorage "mo:caffeineai-object-storage/Mixin";
import Storage "mo:caffeineai-object-storage/Storage";

actor {
  include MixinObjectStorage();

   // Track file references
  type Data = {
        id: Text;
        blob: Storage.ExternalBlob;
        name: Text;
        // other metadata
    };
};

Frontend

Backend Blob fields are represented as ExternalBlob on the frontend.

import { ExternalBlob } from "@caffeineai/object-storage";
import type { FileRecord } from "@caffeineai/object-storage";

ExternalBlob API
class ExternalBlob {
  getBytes(): Promise<Uint8Array<ArrayBuffer>>;
  getDirectURL(): string;
  static fromURL(url: string): ExternalBlob;
  static fromBytes(blob: Uint8Array<ArrayBuffer>): ExternalBlob;
  withUploadProgress(onProgress: (percentage: number) => void): ExternalBlob;
}

Uploading Files

Convert the browser File object to ExternalBlob and pass the original filename alongside:

const handleUpload = async (file: File) => {
  const bytes = new Uint8Array(await file.arrayBuffer());
  const blob = ExternalBlob.fromBytes(bytes).withUploadProgress((pct) => {
    setProgress(pct);
  });

  await actor.uploadFile(file.name, blob);
};


Always send file.name so the backend stores the original filename.

Displaying Files

Use getDirectURL() for inline display (images, videos). This returns an opaque proxy URL -- it has no file extension, so never inspect the URL to determine file type.

<img src={record.blob.getDirectURL()} alt={record.filename} />

File Type Detection

CRITICAL: Never detect file types by inspecting the URL from getDirectURL(). These are opaque proxy URLs with no extension. Instead use the filename field from the backend record:

const isImage = (filename: string) =>
  /\.(jpg|jpeg|png|gif|webp|svg|bmp|ico)$/i.test(filename);

// Conditional rendering
{isImage(record.filename) ? (
  <img src={record.blob.getDirectURL()} alt={record.filename} />
) : (
  <div>{record.filename}</div>
)}


If the backend also returns a mimeType field, prefer that:

const isImage = (mimeType?: string) => mimeType?.startsWith("image/");

Downloading Files

For downloads with the original filename, use getBytes() to create a downloadable link:

const handleDownload = async (record: FileRecord) => {
  const bytes = await record.blob.getBytes();
  const blob = new Blob([bytes]);
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = record.filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
};


Use getDirectURL() for inline display, getBytes() for save-as downloads.

Summary
Use case	Method	Notes
Display image/video	blob.getDirectURL()	Streaming, cached
Download with filename	blob.getBytes()	Wrap in Blob + anchor
Upload from browser	ExternalBlob.fromBytes(bytes)	Pair with .withUploadProgress()
Detect file type	filename or mimeType field	NEVER inspect the URL
Weekly Installs
23
Repository
caffeinelabs/skills
First Seen
9 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass