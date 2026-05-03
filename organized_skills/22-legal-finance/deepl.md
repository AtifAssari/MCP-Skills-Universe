---
rating: ⭐⭐⭐
title: deepl
url: https://skills.sh/zephyrwang6/myskill/deepl
---

# deepl

skills/zephyrwang6/myskill/deepl
deepl
Installation
$ npx skills add https://github.com/zephyrwang6/myskill --skill deepl
SKILL.md
DeepL Translation Skill

Übersetzt Texte, Dokumente und XLIFF-Dateien via DeepL API.

Konfiguration

Erforderlich:

DEEPL_API_KEY - DeepL API-Schlüssel

Optional:

DEEPL_TARGET_LANG - Standard-Zielsprache (Default: DE)
Verfügbare Befehle
Befehl	Beschreibung
/deepl translate "<text>"	Text übersetzen
/deepl file <path>	Dokument übersetzen
/deepl xliff <path>	XLIFF-Datei übersetzen
Gemeinsame Optionen
--to <LANG> - Zielsprache (z.B. EN, DE, FR)
--from <LANG> - Quellsprache (sonst Auto-Detect)
API-Konfiguration
API-Key Prüfung

Vor jedem API-Call prüfen:

if [ -z "$DEEPL_API_KEY" ]; then
    echo "❌ DEEPL_API_KEY nicht gesetzt"
    echo ""
    echo "Setup:"
    echo "  export DEEPL_API_KEY='your-api-key'"
    echo ""
    echo "API-Key erhältlich unter: https://www.deepl.com/pro-api"
    exit 1
fi

API-Endpunkt bestimmen

DeepL Free Keys enden auf :fx:

if [[ "$DEEPL_API_KEY" == *":fx" ]]; then
    DEEPL_API_URL="https://api-free.deepl.com/v2"
else
    DEEPL_API_URL="https://api.deepl.com/v2"
fi

Zielsprache bestimmen
TARGET_LANG="${DEEPL_TARGET_LANG:-DE}"
# Kann mit --to überschrieben werden

/deepl translate

Übersetzt freien Text.

Syntax
/deepl translate "<text>" [--to LANG] [--from LANG]

Beispiele
/deepl translate "Hello, how are you?"
/deepl translate "Guten Morgen" --to EN
/deepl translate "Bonjour" --from FR --to DE

Anweisungen

Parameter parsen:

Text aus Anführungszeichen extrahieren
--to und --from Flags verarbeiten

API-Call ausführen:

# Variablen setzen
TEXT="{{user_text}}"
TARGET="${TARGET_LANG}"  # aus --to oder Environment
SOURCE_PARAM=""
if [ -n "$SOURCE_LANG" ]; then
    SOURCE_PARAM="--data-urlencode \"source_lang=$SOURCE_LANG\""
fi

# API-Call
RESPONSE=$(curl -s -X POST "$DEEPL_API_URL/translate" \
    -H "Authorization: DeepL-Auth-Key $DEEPL_API_KEY" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    --data-urlencode "text=$TEXT" \
    --data-urlencode "target_lang=$TARGET" \
    $SOURCE_PARAM)

# Ergebnis extrahieren
TRANSLATED=$(echo "$RESPONSE" | jq -r '.translations[0].text // empty')
DETECTED_LANG=$(echo "$RESPONSE" | jq -r '.translations[0].detected_source_language // empty')

if [ -z "$TRANSLATED" ]; then
    ERROR=$(echo "$RESPONSE" | jq -r '.message // "Unbekannter Fehler"')
    echo "❌ Übersetzung fehlgeschlagen: $ERROR"
    exit 1
fi

echo "📝 Original ($DETECTED_LANG): $TEXT"
echo "✅ Übersetzung ($TARGET): $TRANSLATED"

Error Handling
HTTP Code	Bedeutung	Aktion
403	Ungültiger API-Key	Key prüfen
429	Rate Limit	1s warten, retry
456	Quota überschritten	DeepL-Konto prüfen
/deepl file

Übersetzt Dokumente (DeepL-native Formate).

Unterstützte Formate
Format	Extension
Microsoft Word	.docx
Microsoft PowerPoint	.pptx
PDF	.pdf (nur Pro)
HTML	.html, .htm
Plain Text	.txt
Syntax
/deepl file <path> [--to LANG] [--from LANG] [--output <path>]

Beispiele
/deepl file README.txt --to EN
/deepl file document.docx --to FR --output document_fr.docx

Anweisungen
Datei prüfen:
FILE_PATH="{{user_path}}"

if [ ! -f "$FILE_PATH" ]; then
    echo "❌ Datei nicht gefunden: $FILE_PATH"
    exit 1
fi

# Extension prüfen
EXT="${FILE_PATH##*.}"
case "$EXT" in
    docx|pptx|pdf|html|htm|txt) ;;
    md)
        # Markdown als txt behandeln
        EXT="txt"
        ;;
    *)
        echo "❌ Format nicht unterstützt: .$EXT"
        echo "Unterstützt: docx, pptx, pdf, html, txt"
        exit 1
        ;;
esac

Dokument hochladen:
UPLOAD_RESPONSE=$(curl -s -X POST "$DEEPL_API_URL/document" \
    -H "Authorization: DeepL-Auth-Key $DEEPL_API_KEY" \
    -F "file=@$FILE_PATH" \
    -F "target_lang=$TARGET_LANG")

DOC_ID=$(echo "$UPLOAD_RESPONSE" | jq -r '.document_id // empty')
DOC_KEY=$(echo "$UPLOAD_RESPONSE" | jq -r '.document_key // empty')

if [ -z "$DOC_ID" ]; then
    ERROR=$(echo "$UPLOAD_RESPONSE" | jq -r '.message // "Upload fehlgeschlagen"')
    echo "❌ $ERROR"
    exit 1
fi

echo "📤 Dokument hochgeladen (ID: $DOC_ID)"

Status prüfen (polling):
echo "⏳ Übersetze..."
while true; do
    STATUS_RESPONSE=$(curl -s -X POST "$DEEPL_API_URL/document/$DOC_ID" \
        -H "Authorization: DeepL-Auth-Key $DEEPL_API_KEY" \
        -d "document_key=$DOC_KEY")

    STATUS=$(echo "$STATUS_RESPONSE" | jq -r '.status')

    case "$STATUS" in
        "done")
            echo "✅ Übersetzung fertig"
            break
            ;;
        "error")
            ERROR=$(echo "$STATUS_RESPONSE" | jq -r '.message')
            echo "❌ Fehler: $ERROR"
            exit 1
            ;;
        "translating"|"queued")
            sleep 2
            ;;
    esac
done

Dokument herunterladen:
# Output-Pfad bestimmen
if [ -z "$OUTPUT_PATH" ]; then
    BASENAME="${FILE_PATH%.*}"
    OUTPUT_PATH="${BASENAME}_${TARGET_LANG}.${EXT}"
fi

curl -s -X POST "$DEEPL_API_URL/document/$DOC_ID/result" \
    -H "Authorization: DeepL-Auth-Key $DEEPL_API_KEY" \
    -d "document_key=$DOC_KEY" \
    -o "$OUTPUT_PATH"

echo "📥 Gespeichert: $OUTPUT_PATH"

/deepl xliff

Übersetzt XLIFF-Dateien (TYPO3, Symfony, etc.).

Syntax
/deepl xliff <path> [--to LANG] [--force] [--dry-run] [--output <path>]

Optionen
Option	Beschreibung
--force	Alle Übersetzungen neu erstellen
--dry-run	Nur zeigen was übersetzt würde
--output <path>	In neue Datei schreiben
Beispiele
/deepl xliff locallang.xlf --to DE
/deepl xliff locallang.xlf --force --to FR
/deepl xliff locallang.xlf --dry-run

Anweisungen
XLIFF-Datei einlesen und validieren:
XLIFF_PATH="{{user_path}}"

if [ ! -f "$XLIFF_PATH" ]; then
    echo "❌ Datei nicht gefunden: $XLIFF_PATH"
    exit 1
fi

# XML validieren
if ! xmllint --noout "$XLIFF_PATH" 2>/dev/null; then
    echo "❌ Ungültiges XML in: $XLIFF_PATH"
    exit 1
fi

Trans-units extrahieren die Übersetzung brauchen:
# XLIFF 1.2: <trans-unit> mit leerem/fehlendem <target>
# XLIFF 2.0: <unit>/<segment> mit leerem/fehlendem <target>

# Für XLIFF 1.2:
UNITS_TO_TRANSLATE=$(xmllint --xpath "//trans-unit[not(target) or target='']" "$XLIFF_PATH" 2>/dev/null)

# Bei --force: alle Units
if [ "$FORCE" = "true" ]; then
    UNITS_TO_TRANSLATE=$(xmllint --xpath "//trans-unit" "$XLIFF_PATH" 2>/dev/null)
fi

Source-Texte sammeln:
# Alle source-Texte extrahieren
SOURCES=$(xmllint --xpath "//trans-unit/source/text()" "$XLIFF_PATH" 2>/dev/null)

# Als Array für Batch-Übersetzung
readarray -t SOURCE_ARRAY <<< "$SOURCES"

Batch-Übersetzung via API:
# DeepL unterstützt mehrere Texte in einem Request
# Baue JSON-Array für text Parameter

TRANSLATIONS=()
for SOURCE in "${SOURCE_ARRAY[@]}"; do
    RESPONSE=$(curl -s -X POST "$DEEPL_API_URL/translate" \
        -H "Authorization: DeepL-Auth-Key $DEEPL_API_KEY" \
        --data-urlencode "text=$SOURCE" \
        --data-urlencode "target_lang=$TARGET_LANG")

    TRANSLATED=$(echo "$RESPONSE" | jq -r '.translations[0].text')
    TRANSLATIONS+=("$TRANSLATED")
done

Bei --dry-run: Nur anzeigen:
if [ "$DRY_RUN" = "true" ]; then
    echo "📋 Würde übersetzen:"
    echo ""
    for i in "${!SOURCE_ARRAY[@]}"; do
        echo "  Source: ${SOURCE_ARRAY[$i]}"
        echo "  Target: ${TRANSLATIONS[$i]}"
        echo ""
    done
    echo "Gesamt: ${#SOURCE_ARRAY[@]} Einheiten"
    exit 0
fi

XLIFF-Datei aktualisieren:

Da XML-Manipulation in Bash komplex ist, verwende Python wenn verfügbar:

import xml.etree.ElementTree as ET

tree = ET.parse(xliff_path)
root = tree.getroot()

# Namespace handling für XLIFF
ns = {'xliff': 'urn:oasis:names:tc:xliff:document:1.2'}

for i, unit in enumerate(root.findall('.//xliff:trans-unit', ns)):
    target = unit.find('xliff:target', ns)
    if target is None:
        target = ET.SubElement(unit, 'target')

    if force or not target.text:
        target.text = translations[i]

tree.write(output_path, encoding='utf-8', xml_declaration=True)


Fallback für reines Bash (einfachere Variante mit sed):

# Backup erstellen
cp "$XLIFF_PATH" "${XLIFF_PATH}.bak"

# Für jede Übersetzung
for i in "${!SOURCE_ARRAY[@]}"; do
    SOURCE="${SOURCE_ARRAY[$i]}"
    TARGET="${TRANSLATIONS[$i]}"

    # Escape für sed
    SOURCE_ESC=$(printf '%s\n' "$SOURCE" | sed 's/[[\.*^$()+?{|]/\\&/g')
    TARGET_ESC=$(printf '%s\n' "$TARGET" | sed 's/[&/\]/\\&/g')

    # Leeres target füllen
    sed -i '' "s|<source>$SOURCE_ESC</source>\s*<target></target>|<source>$SOURCE_ESC</source><target>$TARGET_ESC</target>|g" "$XLIFF_PATH"

    # Fehlendes target einfügen
    sed -i '' "s|<source>$SOURCE_ESC</source>\s*</trans-unit>|<source>$SOURCE_ESC</source><target>$TARGET_ESC</target></trans-unit>|g" "$XLIFF_PATH"
done

Ergebnis ausgeben:
echo "✅ XLIFF aktualisiert: $OUTPUT_PATH"
echo "   Übersetzt: ${#TRANSLATIONS[@]} Einheiten"

Error Handling
HTTP Status Codes
Code	Bedeutung	Reaktion
200	Erfolg	Weiter
400	Bad Request	Parameter prüfen
403	Forbidden	API-Key ungültig
404	Not Found	Endpunkt prüfen
413	Payload too large	Text/Datei zu groß
429	Too Many Requests	1s warten, max 3 Retries
456	Quota exceeded	DeepL-Konto prüfen
5xx	Server Error	Retry mit Backoff
Retry-Logik
deepl_request() {
    local max_retries=3
    local retry_count=0
    local wait_time=1

    while [ $retry_count -lt $max_retries ]; do
        RESPONSE=$(curl -s -w "\n%{http_code}" "$@")
        HTTP_CODE=$(echo "$RESPONSE" | tail -n1)
        BODY=$(echo "$RESPONSE" | sed '$d')

        case "$HTTP_CODE" in
            200) echo "$BODY"; return 0 ;;
            429|5*)
                retry_count=$((retry_count + 1))
                echo "⏳ Retry $retry_count/$max_retries in ${wait_time}s..." >&2
                sleep $wait_time
                wait_time=$((wait_time * 2))
                ;;
            403)
                echo "❌ API-Key ungültig. Bitte prüfen:" >&2
                echo "   export DEEPL_API_KEY='your-key'" >&2
                return 1
                ;;
            456)
                echo "❌ DeepL-Quota überschritten." >&2
                echo "   Prüfe dein Konto: https://www.deepl.com/pro-account" >&2
                return 1
                ;;
            *)
                echo "❌ API-Fehler ($HTTP_CODE): $BODY" >&2
                return 1
                ;;
        esac
    done

    echo "❌ Max Retries erreicht" >&2
    return 1
}

Validierung

Vor API-Calls immer prüfen:

DEEPL_API_KEY gesetzt?
Datei existiert? (bei file/xliff)
Dateiformat unterstützt?
Zielsprache gültig?
Gültige Sprachcodes
BG, CS, DA, DE, EL, EN, EN-GB, EN-US, ES, ET, FI, FR, HU, ID, IT,
JA, KO, LT, LV, NB, NL, PL, PT, PT-BR, PT-PT, RO, RU, SK, SL, SV,
TR, UK, ZH, ZH-HANS, ZH-HANT

Weekly Installs
9
Repository
zephyrwang6/myskill
GitHub Stars
281
First Seen
Mar 25, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass