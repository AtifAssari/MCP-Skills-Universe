---
title: odoo-development
url: https://skills.sh/sergioperez8042/sophia_ecommerce/odoo-development
---

# odoo-development

skills/sergioperez8042/sophia_ecommerce/odoo-development
odoo-development
Installation
$ npx skills add https://github.com/sergioperez8042/sophia_ecommerce --skill odoo-development
SKILL.md
Descripción técnica

Odoo es un ERP modular basado en Python. Cada módulo encapsula modelos, vistas, seguridad, datos y pruebas.

Estructura recomendada de un módulo

my_module/ models/ views/ security/ data/ reports/ tests/ manifest.py

Buenas prácticas clave
Modelos
Clases en PascalCase
_name en snake.case
ORM
Evitar SQL directo si no es necesario
No usar cr.commit en lógica ni tests
Vistas
XML claro y desacoplado
QWeb para reportes
Testing
TransactionCase
Tests en tests/test_*.py
CI/CD
Odoo.sh o pipelines propios
Arquitectura
MVC: Modelos (Python), Vistas (XML/QWeb), Controladores (HTTP)

El desarrollo profesional en Odoo requiere alinearse estrictamente con las guías oficiales para garantizar mantenibilidad y compatibilidad futura.

Weekly Installs
11
Repository
sergioperez8042…commerce
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass