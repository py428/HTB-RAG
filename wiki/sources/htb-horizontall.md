---
type: source
title: "HTB Horizontall writeup"
raw: raw/htb-horizontall.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[horizontall]]
---
# Source: HTB Horizontall writeup
> Complete walkthrough of Horizontall HackTheBox machine covering Strapi CMS exploitation (CVE-2019-18818 and CVE-2019-19609), Laravel debug mode deserialization attack, and analysis of vulnerability patches.
## Key facts extracted
- Strapi 3.0.0-beta.17.4 vulnerable to password reset bypass and authenticated RCE
- CVE-2019-18818 sends {"code": {}} to bypass reset password verification
- CVE-2019-19609 command injection in plugin parameter via npm install command
- Laravel application running on localhost:8000 with debug mode enabled
- /profiles endpoint crashes Laravel exposing debug information
- PHAR deserialization with Monolog RCE chain achieves code execution as root
- Strapi patches wrap code parameter in ${} to force string type
- Plugin install/uninstall patches add alphanumeric/dash/underscore validation
## Filed into
[[horizontall]], [[strapi-password-reset]], [[strapi-auth-rce]], [[deserialization]], [[laravel-debug-rce]]
