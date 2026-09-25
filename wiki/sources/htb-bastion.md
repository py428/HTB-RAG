---
type: source
title: "HTB Bastion writeup"
raw: raw/htb-bastion.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[bastion]]
---
# Source: HTB Bastion writeup
> Writeup demonstrating SMB enumeration, VHD backup mounting, and password recovery techniques on a Windows Server 2016 system with mRemoteNG installation.
## Key facts extracted
- Backups SMB share contains WindowsImageBackup with VHD files from L4mpje-PC
- Registry dump reveals l4mpje user hash and default autologin password "bureaulampje"
- mRemoteNG confCons.xml contains encrypted administrator password
- Multiple decryption methods available for mRemoteNG passwords
- SSH access available with recovered credentials
## Filed into
[[bastion]], [[vhd-mount]], [[registry-hashes]], [[mremoteng-decrypt]]
