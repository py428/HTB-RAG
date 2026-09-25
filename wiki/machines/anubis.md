---
type: machine
title: Anubis
platform: htb
os: windows
difficulty: insane
tags: [ad, windows, asp, certificate, jamovi, adcs, kerberos, insane]
solved: 2026-07-09
sources: [[htb-anubis]]
related: []
---
# Anubis

> Anubis is an Active Directory environment where an ASP SSTI vulnerability leads to container compromise, followed by Jamovi file exploitation, AD CS template abuse, and Kerberos certificate authentication for domain admin access.

## Attack path

1. [[asp-ssti]] — Exploit ASP template injection in contact form for SYSTEM in container
2. [[jamovi-cve-2021-28079]] — Use malicious Jamovi file to gain execution as diegocruz
3. [[adcs-template-abuse]] — Abuse Web certificate template with ENROLLEE_SUPPLIES_SUBJECT flag
4. [[certificate-authentication]] — Generate admin certificate and authenticate via Kerberos PKINIT

## Techniques used

- [[asp-ssti]] — Classic ASP server-side template injection for code execution
- [[hidden-input-manipulation]] — Modifying hidden form fields for privilege escalation
- [[cookie-sharing]] — Sharing JWT cookies between applications with shared secrets
- [[ssrf]] — Server-side request forgery to access internal management interface
- [[file-upload-bypass]] — Uploading malicious files with PDF magic bytes
- [[jamovi-cve-2021-28079]] — Jamovi XSS vulnerability in .omv files for code execution
- [[adcs-template-abuse]] — AD CS template manipulation and certificate enrollment
- [[acl-write-members]] — Full control over certificate template object
- [[kerberos-pkinit]] — Kerberos certificate-based authentication with time skew handling
- [[chisel-tunnel]] — SOCKS proxy tunneling for internal network access

## Tools used

- [[nmap]] — TCP port scanning and service identification
- [[crackmapexec]] — SMB enumeration and authentication testing
- [[feroxbuster]] — Web directory brute force with ASP extension
- [[ffuf]] — Virtual host fuzzing
- [[responder]] — NTLM relay attack and hash capture
- [[hashcat]] — NetNTLMv2 hash cracking
- [[smbclient]] — SMB file share enumeration
- [[chisel]] — Reverse SOCKS tunnel creation
- [[proxychains]] — Tunneling traffic through SOCKS proxy
- Certify — AD CS template enumeration
- certreq — Windows certificate request submission
- certutil — CA certificate extraction
- openssl — Certificate request generation and parsing
- [[kinit]] — Kerberos ticket initialization with PKINIT
- [[evil-winrm]] — WinRM shell with Kerberos authentication
- [[impacket]] — Various AD exploitation tools

## Services / ports

- 135/tcp — msrpc — Microsoft Windows RPC
- 443/tcp — https — Microsoft HTTPAPI 2.0 with www.windcorp.htb certificate
- 445/tcp — smb — Microsoft-DS with message signing
- 593/tcp — http-rpc-epmap — Microsoft Windows RPC over HTTP
- 49721/tcp — unknown — Dynamic RPC port

## Lessons / notes

- ASP SSTI can provide SYSTEM access even in containerized environments
- Hidden form fields often contain important access control parameters
- Applications sharing JWT secrets allow cookie replay attacks
- Virtual host fuzzing essential for finding hidden internal applications
- NTLM relay attacks can capture hashes even without full relay exploitation
- Jamovi files are ZIP archives containing HTML with embedded JavaScript
- AD CS templates with ENROLLEE_SUPPLIES_SUBJECT allow arbitrary SAN specification
- Time synchronization critical for Kerberos certificate authentication
- Chisel reverse SOCKS tunnels useful for accessing internal network services
- Certificate-based authentication bypasses password requirements entirely

## CVEs

- CVE-2021-28079 — Jamovi XSS vulnerability allowing code execution
