---
rating: ⭐⭐
title: k8s-storage
url: https://skills.sh/rohitg00/kubectl-mcp-server/k8s-storage
---

# k8s-storage

skills/rohitg00/kubectl-mcp-server/k8s-storage
k8s-storage
Installation
$ npx skills add https://github.com/rohitg00/kubectl-mcp-server --skill k8s-storage
SKILL.md
Kubernetes Storage

Manage Kubernetes storage using kubectl-mcp-server's storage tools.

When to Apply

Use this skill when:

User mentions: "PVC", "PV", "storage class", "volume", "disk", "storage"
Operations: provisioning storage, mounting volumes, expanding storage
Keywords: "persist", "data", "backup storage", "volume claim"
Priority Rules
Priority	Rule	Impact	Tools
1	Verify storage class exists before PVC	CRITICAL	get_storage_classes
2	Check PVC status before pod deployment	HIGH	describe_pvc
3	Review access modes for multi-pod access	MEDIUM	get_pvcs
4	Monitor PV reclaim policy	LOW	get_persistent_volumes
Quick Reference
Task	Tool	Example
List PVCs	get_pvcs	get_pvcs(namespace)
PVC details	describe_pvc	describe_pvc(name, namespace)
Storage classes	get_storage_classes	get_storage_classes()
List PVs	get_persistent_volumes	get_persistent_volumes()
Persistent Volume Claims (PVCs)
get_pvcs(namespace="default")

describe_pvc(name="my-pvc", namespace="default")

kubectl_apply(manifest="""
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
  namespace: default
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
  storageClassName: standard
""")

kubectl_delete(resource_type="pvc", name="my-pvc", namespace="default")

Storage Classes
get_storage_classes()

kubectl_apply(manifest="""
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-ssd
provisioner: kubernetes.io/gce-pd
parameters:
  type: pd-ssd
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
""")

Persistent Volumes
get_persistent_volumes()

describe_persistent_volume(name="pv-001")

Volume Snapshots
kubectl_apply(manifest="""
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: my-snapshot
  namespace: default
spec:
  volumeSnapshotClassName: csi-snapclass
  source:
    persistentVolumeClaimName: my-pvc
""")

kubectl_apply(manifest="""
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: restored-pvc
spec:
  dataSource:
    name: my-snapshot
    kind: VolumeSnapshot
    apiGroup: snapshot.storage.k8s.io
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
""")

Troubleshooting Storage
describe_pvc(name="my-pvc", namespace="default")

get_events(namespace="default")
describe_pod(name="my-pod", namespace="default")

Related Skills
k8s-backup - Velero backup/restore
k8s-operations - kubectl apply/patch
Weekly Installs
9
Repository
rohitg00/kubect…p-server
GitHub Stars
869
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass