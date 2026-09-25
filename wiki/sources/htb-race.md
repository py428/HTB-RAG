---
type: source
title: "HTB Race writeup"
raw: raw/htb-race.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[race]]
---
# Source: HTB Race writeup
> Comprehensive walkthrough of exploiting Grav CMS vulnerabilities including credential exposure from phpSysInfo, password reset token manipulation via backup downloads, and multiple RCE paths through SSTI or malicious theme upload, culminating in a TOCTOU race condition using named pipes for root access.

## Key facts extracted
- phpSysInfo page暴露backup用户凭证在进程列表中
- Grav CMS备份包含用户YAML配置文件和密码重置令牌
- CVE-2024-28116允许绕过Twig沙箱执行系统命令
- 备用路径：通过Burp代理拦截恶意主题上传实现RCE
- TOCTOU漏洞：在MD5校验和脚本执行之间使用命名管道替换脚本
- 后台容器进程错误地以UID 1000运行，允许进程越狱

## Filed into
[[race]], [[password-reset-abuse]], [[ssti]], [[toctou]], [[named-pipe]], [[grav-cms]], [[twig]]