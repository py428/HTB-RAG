---
type: technique
title: DLL reverse shell
tags: []
platforms: []
updated: 2026-07-09
---
# DLL reverse shell

## What it is
A malicious DLL authored to act as a payload that, once loaded by a vulnerable process, executes attacker code and calls back to a listener with an interactive shell. Rather than exploiting in-process logic directly, the attacker controls the contents of a DLL the target is coerced into loading (typically via a signature-check or search-order race), and uses its entry point or a specific exported function to spawn the shell. It pairs naturally with flaws like ThemeBleed (CVE-2023-38146), where Windows theme validation loads an attacker-supplied `_vrf.dll` and invokes a named export (`VerifyThemeVersion`) before the signature is fully validated.

## When it works
- The victim runs an unpatched Windows host vulnerable to a DLL-loading race (e.g., theme signature verification).
- You can deliver a crafted file (.theme / .msstyles) that references your DLL along a path the target will resolve.
- The target host can reach your listener over the network (outbound connect-back).
- You have a build chain to compile a properly exported Windows DLL (MSVC / Visual Studio).

## How it's done
Author the DLL with the export signature the loader expects to call, and have that export spawn a reverse shell. With Visual Studio (MSVC), create an x64 DLL exporting the required function name (e.g., `VerifyThemeVersion`) whose body opens a socket back to your IP and redirects stdin/stdout/stderr (a classic `WSASocket` + `CreateProcess` shell, or `msfvenom -p windows/x64/shell_reverse_tcp -f dll` with the export stubbed in). Place the compiled `_vrf.dll` where the malicious theme file points it, deliver the .theme to the victim, and catch the callback with netcat (`nc -lvnp <PORT>`). On a clean callback you land an interactive shell as the user that applied the theme.

## Observed on
- [[aero]] — Custom DLL with VerifyThemeVersion export for theme exploit

## See also
