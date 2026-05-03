---
title: amneziawg-openwrt-guide
url: https://skills.sh/nordz0r/skills/amneziawg-openwrt-guide
---

# amneziawg-openwrt-guide

skills/nordz0r/skills/amneziawg-openwrt-guide
amneziawg-openwrt-guide
Installation
$ npx skills add https://github.com/nordz0r/skills --skill amneziawg-openwrt-guide
SKILL.md
AmneziaWG OpenWrt Guide

Этот skill описывает именно интеграцию протокола AmneziaWG в OpenWrt, а не "весь Amnezia-продукт". Репозиторий содержит kernel module, userspace tools, netifd helper и LuCI UI.

Используй его, когда нужно понять, как поднять proto 'amneziawg', как устроены peer sections, как работает fallback на userspace и где чинить LuCI/RPC часть.

Когда использовать
Настройка интерфейса AmneziaWG на OpenWrt.
Разбор UCI schema или полей LuCI формы.
Отладка handshakes, endpoint resolution, key generation, status page.
Сборка пакетов в OpenWrt SDK/Buildroot.
Работа с kmod-amneziawg, amneziawg-tools, luci-proto-amneziawg.
Проверка, почему не загрузился kernel module и включился userspace fallback.
Быстрый выбор workflow
Если задача про роутер и UCI/LuCI: начни с references/uci-model.md.
Если задача про устройство репозитория: открой references/architecture.md.
Если задача про сборку, совместимость или диагностику: открой references/build-and-debug.md.

Открывай только нужный reference, потому что upstream почти не объясняет workflow словами и важные детали спрятаны в коде.

Router Workflow
Уточни, нужен ли kernel mode или допустим userspace fallback.
Проверь, какие пакеты реально стоят на роутере: amneziawg-tools, luci-proto-amneziawg, kmod-amneziawg.
Сверь UCI-модель интерфейса и peer sections.
Если проблема в endpoint/динамическом DNS, проверь persistent_keepalive и watchdog workflow.
Если задача про LuCI, проверь JS форму, RPC ucode и status page вместе.
Development Workflow
amneziawg-tools/ дает бинарник awg, netifd helper и watchdog.
kmod-amneziawg/ патчит in-tree WireGuard sources OpenWrt и потому очень чувствителен к смене kernel layout.
luci-proto-amneziawg/ содержит форму протокола, RPC методы, ACL и страницу статуса.
При любых изменениях нужно держать в голове и runtime на роутере, и packaging в Buildroot.
На что обращать внимание
Репозиторий не поставляет "полный клиент Amnezia", а только OpenWrt integration layer.
Userspace fallback требует amneziawg-go, но этот бинарник upstream-репозиторий не кладет.
QR generation требует установленный qrencode.
Изменения kernel patch легко ломаются на новых версиях OpenWrt/kernel tree.
Security Notes
Ставь пакеты и бинарники только из проверенного feed, релизного артефакта или зафиксированного commit/tag, а не из непроверенного зеркала.
Для amneziawg-go, kernel patches и LuCI-компонентов фиксируй версию и сверяй источник перед обновлением.
Не подмешивай в UCI/LuCI значения, которые пришли из недоверенного внешнего источника, без ручной проверки.
References
references/architecture.md: роли пакетов и карта ключевых файлов.
references/uci-model.md: интерфейс proto amneziawg, peer sections, опции и их смысл.
references/build-and-debug.md: сборка, kernel/userspace fallback, watchdog и runtime-диагностика.
Weekly Installs
15
Repository
nordz0r/skills
GitHub Stars
2
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass