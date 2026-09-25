---
type: machine
title: Rebound
platform: htb
os: windows
difficulty: insane
tags: [windows, ad, kerberos, delegation, acl]
solved: 2026-07-09
sources: [[htb-rebound]]
related: []
---
# Rebound
> Complex Active Directory box requiring AS-REP roasting, Kerberoasting, ACL abuse, delegation manipulation, and Kerberos relay attacks across multiple users.

## Attack path
1. Perform RID cycling to enumerate users and [[as-rep-roasting]] to get jjones account
2. Use AS-REP account for [[kerberoasting]] to crack ldap_monitor password
3. Password reuse gives access to oorend with Self privilege on ServiceMGMT group
4. Add self to ServiceMGMT granting GenericAll over Service Users OU
5. Use [[shadow-credentials]] to get WinRM_svc access and user flag
6. Perform [[kerberos-relay]] with both RemotePotato0 and KrbRelayUp to get tbrady
7. Read GMSA password for delegator$ with constrained delegation
8. Combine [[constrained-delegation]] and [[rbcd]] to get DC01$ ticket and [[dcsync]]

## Techniques used
- [[as-rep-roasting]] — jjones account had preauth disabled, used for Kerberoasting without creds
- [[kerberoasting]] — Cracked ldap_monitor service account password "1GR8t@$$4u"
- [[acl-self-add]] — oorend had Self rights on ServiceMGMT allowing self-add to group
- [[shadow-credentials]] — Added KeyCredentialLink to winrm_svc and authenticated as certificate
- [[kerberos-relay]] — Both RemotePotato0 and KrbRelayUp for cross-session relay attacks
- [[constrained-delegation]] — abused delegator$ with S4U2Self/S4U2Proxy to impersonate DC
- [[rbcd]] — Added KDCCredentialLink to DC01$ then used certificate for delegation

## Tools used
[[nmap]], [[netexec]], [[hashcat]], [[bloodhound]], [[certipy]], [[bloodyAD]], [[powerview]], [[RemotePotato0]], [[KrbRelayUp]], [[impacket]]

## Services / ports
[[dns]] (53), [[kerberos]] (88), [[ldap]] (389), [[smb]] (445), [[winrm]] (5985)

## Lessons / notes
- AS-REP roasting enables Kerberoasting without any domain credentials
- Password reuse between service accounts and domain users is common
- Self ACL permission allows adding yourself to groups
- Constrained delegation + RBCD chain allows impersonating DC computer account
- Multiple relay tools needed as different tools work in different session contexts