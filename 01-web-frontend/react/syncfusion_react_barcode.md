---
rating: ⭐⭐⭐
title: syncfusion-react-barcode
url: https://skills.sh/syncfusion/react-ui-components-skills/syncfusion-react-barcode
---

# syncfusion-react-barcode

skills/syncfusion/react-ui-components-skills/syncfusion-react-barcode
syncfusion-react-barcode
Installation
$ npx skills add https://github.com/syncfusion/react-ui-components-skills --skill syncfusion-react-barcode
SKILL.md
Implementing Syncfusion React Barcode
When to Use This Skill

Use this skill when you need to:

Generate barcodes (Code39, Code128, Code11, Code32, Code93, Codabar) in React
Create QR codes for URLs, contact info, or product identification
Generate Data Matrix codes for labels, tracking, or inventory
Customize barcode appearance (size, color, text display)
Export barcodes as images (JPG, PNG) or base64 strings
Integrate barcode generation into forms, reports, or applications
Library Overview: Three Generator Types

Syncfusion React Barcode provides three main components:

BarcodeGeneratorComponent - Traditional 1D barcodes (Code39, Code128, etc.)

Character encoding varies by type
Ideal for: Product codes, inventory, retail
Readability: High, works with basic scanners

QRCodeGeneratorComponent - 2D Quick Response codes

Versions 1-40 with automatic scaling
Ideal for: URLs, contact info, product links, advertising
Capacity: Up to thousands of characters

DataMatrixGeneratorComponent - 2D Data Matrix codes

Square/rectangular format, compact size
Ideal for: Labels, parts tracking, aerospace/automotive
Capacity: Alphanumeric data, efficient encoding
Documentation and Navigation Guide
Getting Started

📄 Read: references/getting-started.md

Installation and dependencies
Vite/React setup
Component imports and basic structure
Parent component initialization
Barcode Generator Types

📄 Read: references/barcode-generator.md

Code39, Code39Extended, Code11, Code128, Code32, Code93, Codabar
When to use each type
Character set support per type
Encoding and checksum information
Implementation examples for each
QR Code Generator

📄 Read: references/qr-code-generator.md

QR Code basics and versions
Automatic version selection
Character encoding (numeric, alphanumeric, JIS8)
Common use cases and patterns
Implementation with different data types
Data Matrix Generator

📄 Read: references/data-matrix-generator.md

Data Matrix basics and structure
Encoding rules and character support
Size and capacity considerations
Label and printing applications
Comparison with other barcode types
Customization and Styling

📄 Read: references/customization.md

Barcode dimensions (width, height)
Colors (foreColor, backgroundColor)
Display text customization
Examples of size and color variations
Responsive design patterns
Export and Integration

📄 Read: references/export-and-integration.md

Export as image (JPG, PNG)
Export as base64 string
Method: exportImage(filename, format)
Method: exportAsBase64Image(format)
Integration with forms, APIs, and reports
Quick Start Examples
Code39 Barcode
import React from 'react';
import { BarcodeGeneratorComponent } from '@syncfusion/ej2-react-barcode-generator';

export default function App() {
  return (
    <BarcodeGeneratorComponent
      id="barcode"
      type="Code39"
      value="SYNCFUSION"
      width="200px"
      height="150px"
    />
  );
}

QR Code
import React from 'react';
import { QRCodeGeneratorComponent } from '@syncfusion/ej2-react-barcode-generator';

export default function App() {
  return (
    <QRCodeGeneratorComponent
      id="qrcode"
      value="https://www.syncfusion.com"
      width="200px"
      height="200px"
    />
  );
}

Data Matrix
import React from 'react';
import { DataMatrixGeneratorComponent } from '@syncfusion/ej2-react-barcode-generator';

export default function App() {
  return (
    <DataMatrixGeneratorComponent
      id="datamatrix"
      value="Syncfusion"
      width="200px"
      height="200px"
    />
  );
}

Common Patterns
Pattern 1: Dynamic Value Generation
const [barcodeValue, setBarcodeValue] = React.useState('DEFAULT123');

<BarcodeGeneratorComponent
  type="Code128"
  value={barcodeValue}
  width="200px"
  height="150px"
/>

Pattern 2: Export on Button Click
const barcodeRef = React.useRef();

const handleExport = () => {
  barcodeRef.current.exportImage('barcode', 'PNG');
};

<div>
  <BarcodeGeneratorComponent
    ref={barcodeRef}
    type="Code39"
    value="SYNC123"
    width="200px"
    height="150px"
  />
  <button onClick={handleExport}>Download Barcode</button>
</div>

Pattern 3: Styled Container
<div style={{ padding: '20px', border: '1px solid #ddd' }}>
  <QRCodeGeneratorComponent
    value="https://example.com"
    width="250px"
    height="250px"
    foreColor="#333"
    backgroundColor="#fff"
  />
</div>

Key Props
Prop	Description	Used By
type	Barcode type (Code39, Code128, Code11, Code32, Code93, Codabar)	BarcodeGeneratorComponent
value	Data to encode	All generators
width	Barcode width (string with px)	All generators
height	Barcode height (string with px)	All generators
foreColor	Dark/bar color	All generators
backgroundColor	Light/space color	All generators
displayText	Object to customize display text	All generators
id	Unique component identifier (required for export)	All generators
Common Use Cases
Retail & Inventory: Code128 barcodes for products and SKUs
E-commerce: QR codes linking to product pages or reviews
Logistics: Data Matrix for package tracking and labels
Document Management: QR codes embedding document metadata
Marketing: Dynamic QR codes with analytics
Healthcare: Code128/Code39 for specimen/patient labeling
Form Workflows: Export barcodes for printing or archival
Next Steps
Choose your generator type based on use case
Read the getting started guide
Review the specific generator documentation
Customize appearance as needed
Implement export if required for your workflow
Weekly Installs
82
Repository
syncfusion/reac…s-skills
GitHub Stars
1
First Seen
Mar 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass