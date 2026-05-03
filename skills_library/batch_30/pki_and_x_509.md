---
title: pki and x.509
url: https://skills.sh/oriolrius/pki-manager-web/pki-and-x.509
---

# pki and x.509

skills/oriolrius/pki-manager-web/PKI and X.509
PKI and X.509
Installation
$ npx skills add https://github.com/oriolrius/pki-manager-web --skill 'PKI and X.509'
SKILL.md
PKI and X.509 Certificates

Expert assistance with Public Key Infrastructure and X.509 certificate management.

Overview

PKI provides secure digital certificate management:

X.509: Standard format for public key certificates
Certificate Authority (CA): Issues and signs certificates
Certificate Signing Request (CSR): Request for certificate issuance
Certificate Revocation: CRL and OCSP protocols
Key Management: Secure generation and storage
X.509 Certificate Structure
Certificate Components
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 4096 (0x1000)
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN=Example CA, O=Example Org, C=US
        Validity
            Not Before: Jan  1 00:00:00 2024 GMT
            Not After : Jan  1 00:00:00 2025 GMT
        Subject: CN=example.com, O=Example Org, C=US
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (2048 bit)
        X509v3 extensions:
            X509v3 Key Usage:
                Digital Signature, Key Encipherment
            X509v3 Extended Key Usage:
                TLS Web Server Authentication
            X509v3 Subject Alternative Name:
                DNS:example.com, DNS:www.example.com
    Signature Algorithm: sha256WithRSAEncryption

Distinguished Name (DN)
Components:
- CN (Common Name): example.com
- O (Organization): Example Organization
- OU (Organizational Unit): IT Department
- L (Locality): San Francisco
- ST (State): California
- C (Country): US
- EMAIL: admin@example.com

OpenSSL Commands
Generate Private Keys
# RSA 2048-bit
openssl genrsa -out private.key 2048

# RSA 4096-bit (more secure)
openssl genrsa -out private.key 4096

# Encrypted private key
openssl genrsa -aes256 -out private.key 4096

# ECDSA P-256
openssl ecparam -name prime256v1 -genkey -out private.key

# ECDSA P-384 (more secure)
openssl ecparam -name secp384r1 -genkey -out private.key

Generate Certificate Signing Request (CSR)
# Generate CSR from private key
openssl req -new -key private.key -out request.csr \
  -subj "/C=US/ST=California/L=San Francisco/O=Example/CN=example.com"

# Generate key and CSR together
openssl req -new -newkey rsa:4096 -nodes \
  -keyout private.key -out request.csr \
  -subj "/CN=example.com/O=Example Org/C=US"

# CSR with Subject Alternative Names (SAN)
openssl req -new -key private.key -out request.csr \
  -subj "/CN=example.com" \
  -addext "subjectAltName=DNS:example.com,DNS:www.example.com,IP:192.168.1.1"

View CSR
# Display CSR details
openssl req -in request.csr -text -noout

# Verify CSR signature
openssl req -in request.csr -verify -noout

Self-Signed Certificates
# Generate self-signed certificate (1 year)
openssl req -x509 -new -key private.key -out cert.pem -days 365 \
  -subj "/CN=example.com/O=Example/C=US"

# Self-signed with SAN
openssl req -x509 -new -key private.key -out cert.pem -days 365 \
  -subj "/CN=example.com" \
  -addext "subjectAltName=DNS:example.com,DNS:*.example.com"

# Generate key and self-signed cert together
openssl req -x509 -newkey rsa:4096 -nodes \
  -keyout private.key -out cert.pem -days 365 \
  -subj "/CN=Root CA/O=Example/C=US"

Certificate Authority Operations
# Create CA directory structure
mkdir -p ca/{certs,crl,newcerts,private}
touch ca/index.txt
echo 1000 > ca/serial

# Generate CA private key
openssl genrsa -aes256 -out ca/private/ca.key 4096

# Generate CA certificate
openssl req -x509 -new -key ca/private/ca.key \
  -out ca/certs/ca.crt -days 3650 \
  -subj "/CN=Example CA/O=Example/C=US"

# Sign CSR with CA
openssl ca -config openssl.cnf \
  -in request.csr \
  -out signed.crt \
  -days 365

# Or use x509 for simpler signing
openssl x509 -req -in request.csr \
  -CA ca/certs/ca.crt -CAkey ca/private/ca.key \
  -CAcreateserial -out signed.crt -days 365 \
  -extfile <(printf "subjectAltName=DNS:example.com")

View and Verify Certificates
# View certificate
openssl x509 -in cert.pem -text -noout

# View certificate dates
openssl x509 -in cert.pem -noout -dates

# View certificate subject
openssl x509 -in cert.pem -noout -subject

# View certificate issuer
openssl x509 -in cert.pem -noout -issuer

# Verify certificate against CA
openssl verify -CAfile ca.crt cert.pem

# Verify certificate chain
openssl verify -CAfile ca.crt -untrusted intermediate.crt cert.pem

Convert Certificate Formats
# PEM to DER
openssl x509 -in cert.pem -out cert.der -outform DER

# DER to PEM
openssl x509 -in cert.der -inform DER -out cert.pem -outform PEM

# PEM to PKCS#12 (.p12, .pfx)
openssl pkcs12 -export -out cert.p12 \
  -inkey private.key -in cert.pem -certfile ca.crt

# PKCS#12 to PEM
openssl pkcs12 -in cert.p12 -out cert.pem -nodes

Certificate Extensions
Key Usage
digitalSignature    - Digital signatures
nonRepudiation      - Non-repudiation
keyEncipherment     - Encrypt symmetric keys
dataEncipherment    - Encrypt data directly
keyAgreement        - Key agreement (DH/ECDH)
keyCertSign         - Sign certificates (CA only)
cRLSign             - Sign CRLs (CA only)

Extended Key Usage (EKU)
serverAuth          - TLS server authentication
clientAuth          - TLS client authentication
codeSigning         - Code signing
emailProtection     - S/MIME email protection
timeStamping        - Trusted time stamping
OCSPSigning         - OCSP response signing

Subject Alternative Names (SAN)
DNS:example.com                 - Domain name
DNS:*.example.com               - Wildcard domain
IP:192.168.1.1                  - IP address
email:admin@example.com         - Email address
URI:https://example.com         - URI

Certificate Revocation
Certificate Revocation List (CRL)
# Generate CRL
openssl ca -config openssl.cnf -gencrl -out crl.pem

# View CRL
openssl crl -in crl.pem -text -noout

# Revoke certificate
openssl ca -config openssl.cnf -revoke cert.pem \
  -crl_reason keyCompromise

# Verify certificate against CRL
openssl verify -crl_check -CRLfile crl.pem -CAfile ca.crt cert.pem

Revocation Reasons
unspecified             - No specific reason
keyCompromise           - Private key compromised
caCompromise            - CA key compromised
affiliationChanged      - Subject affiliation changed
superseded              - Certificate replaced
cessationOfOperation    - No longer needed
certificateHold         - Temporary suspension
removeFromCRL          - Remove from CRL
privilegeWithdrawn      - Privileges removed
aACompromise            - Attribute authority compromised

Certificate Hierarchy
Root CA
interface RootCA {
  subject: DistinguishedName;
  keyPair: KeyPair;
  certificate: X509Certificate;
  validity: {
    notBefore: Date;
    notAfter: Date; // Typically 10-20 years
  };
  keyUsage: ['keyCertSign', 'cRLSign'];
  basicConstraints: {
    cA: true;
    pathLenConstraint: undefined; // No limit
  };
}

Intermediate CA
interface IntermediateCA {
  subject: DistinguishedName;
  issuer: DistinguishedName; // Root CA
  keyPair: KeyPair;
  certificate: X509Certificate;
  validity: {
    notBefore: Date;
    notAfter: Date; // Shorter than root, typically 5-10 years
  };
  keyUsage: ['keyCertSign', 'cRLSign', 'digitalSignature'];
  basicConstraints: {
    cA: true;
    pathLenConstraint: 0; // Can only sign end-entity certs
  };
}

End-Entity Certificate
interface EndEntityCertificate {
  subject: DistinguishedName;
  issuer: DistinguishedName; // Intermediate or Root CA
  keyPair: KeyPair;
  certificate: X509Certificate;
  validity: {
    notBefore: Date;
    notAfter: Date; // Typically 1-2 years
  };
  keyUsage: ['digitalSignature', 'keyEncipherment'];
  extendedKeyUsage: ['serverAuth', 'clientAuth'];
  subjectAlternativeName: {
    dns: string[];
    ip: string[];
  };
  basicConstraints: {
    cA: false;
  };
}

Node.js Integration
Generate CSR with Node Crypto
import { generateKeyPairSync, createSign } from 'crypto';
import { X509Certificate } from 'crypto';

// Generate key pair
const { publicKey, privateKey } = generateKeyPairSync('rsa', {
  modulusLength: 4096,
  publicKeyEncoding: {
    type: 'spki',
    format: 'pem',
  },
  privateKeyEncoding: {
    type: 'pkcs8',
    format: 'pem',
  },
});

// Parse X.509 certificate
const cert = new X509Certificate(certPem);
console.log(cert.subject);
console.log(cert.issuer);
console.log(cert.validFrom);
console.log(cert.validTo);
console.log(cert.fingerprint256);

Best Practices
Key Size: Use RSA 4096-bit or ECDSA P-384 for CAs
Validity Period: Root CA (10-20 years), Intermediate (5-10 years), End-entity (1-2 years)
Key Storage: Store CA private keys in HSM or KMS
Certificate Chain: Always verify complete chain of trust
Revocation: Implement CRL and/or OCSP for revocation checking
SAN over CN: Use Subject Alternative Names instead of Common Name
Strong Algorithms: Use SHA-256 or better (avoid SHA-1, MD5)
Key Usage: Set appropriate key usage and extended key usage
Path Length: Limit path length in CA certificates
Audit Trail: Log all certificate operations
Common Operations
Verify Certificate Chain
# Create chain file (cert + intermediate + root)
cat cert.pem intermediate.pem root.pem > chain.pem

# Verify chain
openssl verify -CAfile root.pem -untrusted intermediate.pem cert.pem

Extract Public Key
# From certificate
openssl x509 -in cert.pem -pubkey -noout > public.key

# From private key
openssl rsa -in private.key -pubout -out public.key

Check Certificate-Key Match
# Compare modulus
openssl x509 -in cert.pem -noout -modulus | openssl md5
openssl rsa -in private.key -noout -modulus | openssl md5
# Should match!

Resources
RFC 5280: X.509 Certificate and CRL Profile
RFC 2986: PKCS #10 CSR Syntax
RFC 6960: OCSP Protocol
OpenSSL Cookbook: https://www.feistyduck.com/books/openssl-cookbook/
Weekly Installs
–
Repository
oriolrius/pki-m…ager-web
GitHub Stars
11
First Seen
–