---
type: source
title: "HTB Waldo writeup"
raw: raw/htb-waldo.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[waldo]]
---
# Source: HTB Waldo writeup
> 0xdf's complete writeup for HTB Waldo covering PHP file read filter bypass, SSH key access to Alpine container, SSH pivot back to host, rbash escape via ed editor, and Linux capabilities exploitation using tac with CAP_DAC_READ_SEARCH for root flag read.

## Key facts extracted
- PHP filter bypass: str_replace not recursive; ....// bypasses ../ and ..\ filters
- SSH discovery: .monitor key found in /home/nobody/.ssh/ with comment "svc_backup@DC"
- Container architecture: Alpine Linux container accessible via SSH on port 22, host SSH on port 8888
- rbash escape: ed editor links to unrestricted binary; !/bin/sh escapes restricted shell
- Linux capabilities: tac has CAP_DAC_READ_SEARCH+ei for full system read access
- Alternative rbash escape: ssh -t bash skips rbash entirely but requires PATH reset
- No root shell: Intended design; capabilities provide read-only access, not full compromise

## Filed into
[[waldo]], [[str_replace-bypass]], [[ssh-key-auth]], [[container-pivot]], [[rbash-escape]], [[linux-capabilities]]
