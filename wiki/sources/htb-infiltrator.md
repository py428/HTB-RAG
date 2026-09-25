---
type: source
title: "HTB Infiltrator writeup"
raw: raw/htb-infiltrator.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[infiltrator]]
---
# Source: HTB Infiltrator writeup
> Detailed writeup for HTB Infiltrator machine covering AS-REP roasting, ACL abuse, shadow credentials, Output Messenger exploitation, calendar execution, BitLocker recovery, NTDS extraction, gMSA password dumping, and ADCS ESC4 template abuse.

## Key facts extracted
- Target: Infiltrator Active Directory domain with complex attack chain
- Primary attack vector: AS-REP roasting → ACL abuse → Shadow credentials → ADCS exploitation
- Initial foothold: AS-REP roasting L.clark account for Kerberos pre-auth exploitation
- Privilege escalation: Complex ACL abuse chain leading to ADCS template abuse
- Root access: ADCS ESC4 exploitation via certipy for administrator certificate enrollment
- Lateral movement: Password reuse, shadow credentials, group membership abuse
- Persistence: Calendar automation, scheduled tasks, service accounts
- The box demonstrates an extremely realistic and complex Active Directory compromise scenario

## Filed into
[[infiltrator]], [[kerberos-username-enumeration]], [[as-rep-roasting]], [[password-reuse]], [[acl-genericall]], [[shadow-credentials]], [[acl-forcechangepassword]], [[rdp-initial-access]], [[calendar-execution]], [[tunnel]], [[api-abuse]], [[bitlocker]], [[dcsync]], [[gmsa]], [[adcs-template-abuse]]
