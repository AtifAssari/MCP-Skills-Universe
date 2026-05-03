---
rating: ⭐⭐⭐
title: fail2ban
url: https://skills.sh/davidcastagnetoa/skills/fail2ban
---

# fail2ban

skills/davidcastagnetoa/skills/fail2ban
fail2ban
Installation
$ npx skills add https://github.com/davidcastagnetoa/skills --skill fail2ban
SKILL.md
fail2ban

Fail2ban lee los logs de Nginx/FastAPI y banea automáticamente las IPs que generan demasiados errores 401, 403 o 429. Complementa al rate limiter de Redis con bans a nivel de iptables/nftables — más eficiente que rechazar en la capa de aplicación.

When to use

Instalar en los nodos donde corre Nginx. El ban a nivel de kernel (iptables) rechaza paquetes antes de que lleguen a Nginx — protección más eficiente para ataques volumétricos.

Instructions
Instalar: apt-get install fail2ban en el host de Nginx.
Crear /etc/fail2ban/jail.d/kyc-nginx.conf:
[kyc-nginx-auth]
enabled = true
port = 443
filter = kyc-nginx-auth
logpath = /var/log/nginx/access.log
maxretry = 10        # 10 intentos fallidos
findtime = 300       # en 5 minutos
bantime = 86400      # ban de 24 horas
[kyc-nginx-ratelimit]
enabled = true
port = 443
filter = kyc-nginx-ratelimit
logpath = /var/log/nginx/access.log
maxretry = 20
findtime = 60
bantime = 3600

Crear filtro /etc/fail2ban/filter.d/kyc-nginx-auth.conf:
[Definition]
failregex = ^.*"status":40[13].*"remote_addr":"<HOST>".*$

Crear filtro para rate limiting (status 429):
[Definition]
failregex = ^.*"status":429.*"remote_addr":"<HOST>".*$

Reiniciar: systemctl restart fail2ban. Verificar: fail2ban-client status kyc-nginx-auth.
Whitelist de IPs internas y de monitorización: ignoreip = 127.0.0.1/8 10.0.0.0/8.
Notes
En Kubernetes, Fail2ban debe correr en el nodo de Nginx (DaemonSet o en el host), no como sidecar — necesita acceso a iptables del host.
Sincronizar los bans entre nodos via fail2ban-client + Redis o usando ipset compartido.
Mantener una duración de ban progresiva: 1h en primer ban, 24h en segundo, permanente en tercero.
Weekly Installs
10
Repository
davidcastagnetoa/skills
First Seen
Mar 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn