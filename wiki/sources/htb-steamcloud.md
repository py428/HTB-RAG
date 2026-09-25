---
type: source
title: "HTB SteamCloud writeup"
raw: raw/htb-steamcloud.md
source_type: htb-writeup
ingested: 2026-07-09
machine: [[steamcloud]]
---
# Source: HTB SteamCloud writeup
> Writeup covering Kubernetes exploitation via unauthenticated Kubelet API, service account token extraction, and container escape through host filesystem mount.
## Key facts extracted
- Kubelet API on 10250/tcp allows unauthenticated command execution
- Service account tokens available in pods at `/run/secrets/kubernetes.io/serviceaccount/`
- nginx pod running with root privileges
- Service account has permissions to create pods
- Host filesystem can be mounted into pods for container escape

## Filed into
[[steamcloud]], [[kubelet-exec]], [[service-account-token]], [[kubernetes-api-auth]], [[kubernetes-pod-creation]], [[container-escape]]
