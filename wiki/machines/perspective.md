---
type: machine
title: "HTB Perspective"
platform: htb
os: windows
difficulty: insane
tags: [web, windows, privesc, ad]
solved: 2026-07-09
sources: [[htb-perspective]]
related: []
---
# HTB Perspective
> ASP.NET application with multiple exploitation paths including SHTML file upload, cookie forgery, SSRF, ViewState deserialization, and padding oracle attacks on staging environment for command injection and root access.

## Attack path
1. Enumerate [[http]] service with [[feroxbuster]] and identify ASP.NET application
2. Upload [[shtml-file-upload]] to read web.config and extract machineKey
3. Forge admin cookie using leaked machineKey with custom C# tool
4. Exploit [[ssrf]] via PDF generation to access internal crypto service
5. Decrypt ViewStateUserKey using XOR stream cipher attack
6. Generate malicious ViewState payload with [[ysoserial.net]] for [[deserialization]]
7. Access staging site via SSH tunnel for additional exploitation
8. Perform [[padding-oracle]] attack on password reset tokens
9. Forge malicious token for [[command-injection]] via PasswordReset.exe

## Techniques used
- [[shtml-file-upload]] — Upload .shtml files with <!--#include--> directives to read files
- [[cookie-forgery]] — Forge .ASPXAUTH cookies using leaked machineKey validation/decryption keys
- [[ssrf]] — HTML meta tag refresh in PDF generation to access internal services
- [[deserialization]] — .NET ViewState deserialization using ysoserial.net TypeConfuseDelegate gadget
- [[padding-oracle]] — Attack AES-CBC encrypted tokens using padbuster for plaintext/ciphertext recovery
- [[command-injection]] — Inject commands via encrypted token parameter in password reset handler

## Tools used
- [[nmap]] — Port scanning identifying IIS and HTTP services
- [[feroxbuster]] — Directory brute forcing lowercase wordlists
- [[ysoserial.net]] — .NET deserialization payload generation
- padbuster — Padding oracle attack tool for encrypted tokens

## Services / ports
- [[ssh]] (22) — OpenSSH for Windows 7.7
- [[http]] (80) — IIS 10.0 with ASP.NET 4.6.1 application
- [[http]] (8000) — Internal crypto service (AdminAPI)
- [[http]] (8009) — Staging environment accessible via tunnel

## Lessons / notes
- ASP.NET machineKey in web.config used for cookie and ViewState encryption/validation
- SHTML files can read files using server-side includes with <!--#include virtual="..."-->
- XOR stream cipher with key reuse allows known-plaintext attacks
- Padding oracle attacks work when different error messages distinguish padding from decryption failures
- Staging environments often have different security configurations and more verbose error messages
- ViewStateUserKey provides CSRF protection but can be leaked via SSRF to internal services
