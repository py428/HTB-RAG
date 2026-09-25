---
type: machine
title: Sizzle
platform: htb
os: windows
difficulty: insane
tags: [ad, windows, web, privesc]
solved: 2026-07-09
sources: [[htb-sizzle]]
related: []
---
# Sizzle
> Insane-difficulty Windows Active Directory box starting with SMB enumeration and SCF file NetNTLMv2 hash capture, progressing through certificate-based WinRM authentication, Kerberoasting, and DCSync attacks to achieve Domain Administrator access.

## Attack path
1. [[ntlm-capture-via-scf]] by dropping malicious .scf file in SMB share to capture amanda's NetNTLMv2 hash
2. [[ad-cs-certificate-auth]] via /certsrv to generate certificate for WinRM access
3. [[kerberoasting]] to crack mrlky's service account password
4. [[dcsync]] using mrlky's GetChanges/GetChangesAll privileges to dump Domain Controller hashes and pass-the-hash as Administrator

## Techniques used
- [[ntlm-capture-via-scf]] — Dropped .scf file with IconFile pointing to attacker's SMB server in Department Shares/Users/Public, captured NetNTLMv2 hash with responder when user browsed directory
- [[ad-cs-certificate-auth]] — Generated user certificate via /certsrv, exported with openssl pkcs12, used for SSL WinRM authentication on 5986/tcp
- [[kerberoasting]] — Used Rubeus or GetUserSPNs.py to request and crack service ticket for http/sizzle SPN associated with mrlky user
- [[dcsync]] — Exploited GetChanges and GetChangesAll privileges on domain object (visible in BloodHound) to replicate NTDS.dit using secretsdump.py
- [[applocker-bypass]] — Bypassed CLM and AppLocker restrictions using PSByPassCLM or msbuild with inline C# shellcode

## Tools used
- [[nmap]] for port and service discovery
- [[smbmap]] and [[smbclient]] for SMB share enumeration
- [[responder]] for NetNTLMv2 hash capture
- [[hashcat]] for cracking NetNTLMv2 and Kerberos tickets
- [[openssl]] for certificate export (pkcs12 format)
- [[rubeus]] for Kerberoasting
- [[impacket]] (GetUserSPNs, secretsdump, wmiexec) for Kerberos and DCSync
- [[bloodhound]] for privilege analysis
- [[chisel]] for port forwarding (Kerberos and LDAP)
- [[msfvenom]] and [[msbuild]] for AppLocker bypass
- [[pspy]] (or ps) for process monitoring

## Services / ports
- 21/tcp — [[ftp]] — Anonymous access available
- 53/tcp — [[dns]] — BIND 9.11.3  
- 80/tcp — [[http]] — Microsoft IIS 10.0
- 135/tcp — [[rpc]] — MSRPC
- 139/tcp, 445/tcp — [[smb]] — SMB2, message signing required
- 389/tcp — [[ldap]] — Active Directory LDAP (HTB.LOCAL)
- 443/tcp — [[http]] — SSL/TLS
- 464/tcp — kpasswd5
- 593/tcp — [[rpc]] — NCACN_HTTP
- 636/tcp — [[ldap]] — LDAPS
- 3268/tcp — [[ldap]] — Global Catalog LDAP
- 3269/tcp — [[ldap]] — Global Catalog LDAPS
- 5985/tcp — [[winrm]] — HTTP
- 5986/tcp — [[winrm]] — HTTPS (for certificate auth)
- 9389/tcp — ADWS

## Lessons / notes
- SCF files with remote IconFile paths trigger SMB authentication from Windows Explorer when directory is viewed
- BloodHound analysis revealed GetChanges/GetChangesAll privileges enabling DCSync without Domain Admin rights
- Certificate-based WinRM authentication requires SSL (5986/tcp) and client certificates in pkcs12 format
- AppLocker CLM (Constrained Language Mode) can be bypassed using signed binaries like InstallUtil.exe or msbuild.exe
- Burp Suite breaks NTLM authentication by closing TCP connections between type-2 and type-3 NTLM messages
- Kerberos requires time synchronization within 5 minutes between client and KDC