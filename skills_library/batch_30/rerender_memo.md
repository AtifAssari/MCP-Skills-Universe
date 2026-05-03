---
title: rerender-memo
url: https://skills.sh/theorcdev/8bitcn-ui/rerender-memo
---

# rerender-memo

skills/theorcdev/8bitcn-ui/rerender-memo
rerender-memo
Installation
$ npx skills add https://github.com/theorcdev/8bitcn-ui --skill rerender-memo
SKILL.md
Extract to Memoized Components

Extract expensive work into memoized components to enable early returns before computation.

Incorrect (computes avatar even when loading):

function Profile({ user, loading }: Props) {
  const avatar = useMemo(() => {
    const id = computeAvatarId(user)
    return <Avatar id={id} />
  }, [user])

  if (loading) return <Skeleton />
  return <div>{avatar}</div>
}


Correct (skips computation when loading):

const UserAvatar = memo(function UserAvatar({ user }: { user: User }) {
  const id = useMemo(() => computeAvatarId(user), [user])
  return <Avatar id={id} />
})

function Profile({ user, loading }: Props) {
  if (loading) return <Skeleton />
  return (
    <div>
      <UserAvatar user={user} />
    </div>
  )
}


Note: If your project has React Compiler enabled, manual memoization with memo() and useMemo() is not necessary. The compiler automatically optimizes re-renders.

Weekly Installs
22
Repository
theorcdev/8bitcn-ui
GitHub Stars
1.8K
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass