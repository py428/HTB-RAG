---
type: machine
title: Precious
platform: htb
os: linux
difficulty: easy
tags: [linux, web, privesc]
solved: 2026-07-09
sources: [[htb-precious]]
related: []
---
# Precious
> Easy Linux box with a URL-to-PDF conversion service. Exploit CVE-2022-25765 command injection in pdfkit for initial access, find credentials in Ruby Bundler config for user pivot, and exploit YAML deserialization in dependency management script for root.
## Attack path
1. [[cve-2022-25765]] — Command injection in PDF generation via backticks in URL parameter
2. [[ruby-bundler-credentials]] — Extract henry password from ~/.bundle/config
3. [[yaml-deserialization]] — Unsafe YAML.load() in update_dependencies.rb script run via sudo
## Techniques used
- [[cve-2022-25765]] — pdfkit v0.8.6 vulnerable to command injection via URL parameter
- [[ruby-bundler-credentials]] — RubyGems credentials stored in ~/.bundle/config file
- [[yaml-deserialization]] — Psych YAML.load() executes arbitrary code via gem Package::TarReader gadgets
## Tools used
- [[nmap]] — Port scanning (SSH 22, HTTP 80)
- [[ffuf]] — Subdomain brute force
- [[feroxbuster]] — Directory brute force
- [[exiftool]] — Extract PDF metadata showing pdfkit v0.8.6
- [[curl]] — Trigger PDF generation with malicious URLs
- [[netcat]] — Reverse shell listener
- [[sshpass]] — SSH login with password
## Services / ports
- [[ssh]] — TCP 22 (OpenSSH 8.4p1)
- [[http]] — TCP 80 (nginx 1.18.0 + Phusion Passenger 6.0.15, Ruby)
## Lessons / notes
- CVE-2022-25765: pdfkit passes URL to wkhtmltopdf without sanitization, backticks execute commands
- PDF metadata reveals pdfkit version, leading to CVE discovery
- Bundler config stores credentials as BUNDLE_HTTPS://RUBYGEMS__ORG/: "user:password"
- Ruby YAML.load() unsafe; should use YAML.safe_load() or Psych.safe_load()
- SetUID bash copy gives effective root via -p flag
- nginx hosts Ruby app via Phusion Passenger module
