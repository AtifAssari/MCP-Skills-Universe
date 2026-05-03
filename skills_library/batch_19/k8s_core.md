---
title: k8s-core
url: https://skills.sh/rohitg00/kubectl-mcp-server/k8s-core
---

# k8s-core

skills/rohitg00/kubectl-mcp-server/k8s-core
k8s-core
Installation
$ npx skills add https://github.com/rohitg00/kubectl-mcp-server --skill k8s-core
SKILL.md
Core Kubernetes Resources

Manage fundamental Kubernetes objects using kubectl-mcp-server's core tools.

When to Apply

Use this skill when:

User mentions: "pods", "namespaces", "configmaps", "secrets", "nodes", "events"
Operations: listing resources, describing objects, creating/deleting resources
Keywords: "show me", "list", "get", "describe", "create", "delete"
Priority Rules
Priority	Rule	Impact	Tools
1	Check namespace exists before operations	CRITICAL	get_namespaces
2	Never expose secrets in plain text	CRITICAL	Handle get_secret output carefully
3	Use labels for filtering	HIGH	label_selector parameter
4	Check events after changes	MEDIUM	get_events
Quick Reference
Task	Tool	Example
List pods	get_pods	get_pods(namespace="default")
Describe pod	describe_pod	describe_pod(name, namespace)
Get logs	get_pod_logs	get_pod_logs(name, namespace)
List namespaces	get_namespaces	get_namespaces()
Get configmap	get_configmap	get_configmap(name, namespace)
List nodes	get_nodes	get_nodes()
Pods
get_pods(namespace="default")
get_pods(namespace="kube-system", label_selector="app=nginx")

describe_pod(name="my-pod", namespace="default")

get_pod_logs(name="my-pod", namespace="default")
get_pod_logs(name="my-pod", namespace="default", previous=True)

delete_pod(name="my-pod", namespace="default")

Namespaces
get_namespaces()

create_namespace(name="my-namespace")

delete_namespace(name="my-namespace")

ConfigMaps
get_configmaps(namespace="default")

get_configmap(name="my-config", namespace="default")

create_configmap(
    name="app-config",
    namespace="default",
    data={"key": "value", "config.yaml": "setting: true"}
)

Secrets
get_secrets(namespace="default")

get_secret(name="my-secret", namespace="default")

create_secret(
    name="db-credentials",
    namespace="default",
    data={"username": "admin", "password": "secret123"}
)

Nodes
get_nodes()

describe_node(name="node-1")

get_nodes_summary()

cordon_node(name="node-1")
uncordon_node(name="node-1")

drain_node(name="node-1", ignore_daemonsets=True)

Events
get_events(namespace="default")

get_events(namespace="default", field_selector="involvedObject.name=my-pod")

Multi-Cluster Support

All tools support context parameter:

get_pods(namespace="default", context="production-cluster")
get_nodes(context="staging-cluster")

Related Skills
k8s-troubleshoot - Debug failing pods
k8s-operations - kubectl apply/patch/delete
Weekly Installs
10
Repository
rohitg00/kubect…p-server
GitHub Stars
869
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail