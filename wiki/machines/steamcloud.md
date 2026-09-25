---
type: machine
title: SteamCloud
platform: htb
os: linux
difficulty: easy
tags: [kubernetes, kubelet, container, easy, linux, privesc]
solved: 2026-07-09
sources: [[htb-steamcloud]]
related: []
---
# SteamCloud
> Easy Linux box featuring Kubernetes misconfigurations. Initial access through unauthenticated Kubelet API access allowing command execution in nginx pod. Privilege escalation by creating malicious pod with host filesystem mount, leveraging service account token for Kubernetes API access.
## Attack path
1. [[kubelet-exec]] — execute commands in nginx pod via kubelet API
2. [[service-account-token]] — extract service account token from pod
3. [[kubernetes-api-auth]] — authenticate to Kubernetes API with token
4. [[kubernetes-pod-creation]] — create pod with host filesystem mount
5. [[container-escape]] — access host filesystem from privileged pod

## Techniques used
- [[kubelet-exec]] — unauthenticated command execution via kubelet API
- [[service-account-token]] — extract Kubernetes service account credentials
- [[kubernetes-api-auth]] — authenticate using service account tokens
- [[kubernetes-pod-creation]] — create pods with custom configurations
- [[container-escape]] — escape pod via host filesystem mount

## Tools used
- [[nmap]] — port scanning identifying Kubernetes services
- kubeletctl — Kubelet API interaction tool
- kubectl — Kubernetes API CLI tool
- jq — JSON parsing for API responses

## Services / ports
- 22/tcp — [[ssh]] — OpenSSH 7.9p1 Debian
- 2379/tcp — etcd-client
- 2380/tcp — etcd-server
- 8443/tcp — Kubernetes API (HTTPS)
- 10249/tcp — kubelet (read-only)
- 10250/tcp — kubelet (exec)
- 10256/tcp — kubelet (healthz)

## Lessons / notes
- Kubelet API (10250) allows command execution without authentication
- Service account tokens stored in `/run/secrets/kubernetes.io/serviceaccount/`
- Kubernetes pods can mount host filesystem for container escape
- minikube runs all components on single host for development
- Unprotected kubelet endpoints provide easy container access
- Service account permissions should be minimized
