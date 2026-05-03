---
title: saas-architecture-deep-dive
url: https://skills.sh/founderjourney/claude-skills/saas-architecture-deep-dive
---

# saas-architecture-deep-dive

skills/founderjourney/claude-skills/saas-architecture-deep-dive
saas-architecture-deep-dive
Installation
$ npx skills add https://github.com/founderjourney/claude-skills --skill saas-architecture-deep-dive
SKILL.md
SaaS Architecture Deep Dive

Sistema para dominar arquitectura SaaS y comunicarla con autoridad senior.

Workflow Principal
1. Identificar necesidad
Usuario dice...	Accion
"Explicar multi-tenancy"	Ver multi-tenancy-patterns.md
"Disenar sistema SaaS"	Ir a Decision Framework (abajo)
"Integrar pagos/billing"	Ver billing-integration.md
"Escalar mi sistema"	Ver scaling-strategies.md
"Explicar mi arquitectura"	Ver your-architecture-answers.md
2. Decision Framework: Disenar SaaS

Paso 1: Requirements

Preguntas clave:
- Cuantos tenants esperamos? (10, 100, 10000?)
- Que tan sensibles son los datos? (compliance requirements?)
- Tenants similares o muy diferentes en uso?
- Budget de infraestructura?


Paso 2: Elegir modelo de tenancy

POCOS TENANTS + DATOS SENSIBLES + ALTO BUDGET
→ SILO (database per tenant)

MUCHOS TENANTS + DATOS NO SENSIBLES + BAJO BUDGET
→ POOL (shared database, tenant_id)

BALANCE
→ BRIDGE (schema per tenant)


Paso 3: Definir isolation boundaries

- Data isolation: como separar datos por tenant
- Compute isolation: recursos compartidos o dedicados
- Network isolation: VPCs, subnets separados?


Paso 4: Billing model

- Flat rate: simple, predecible
- Usage-based: justo, complejo de trackear
- Tiered: balance, feature gates
- Hybrid: base + overage

3. Patrones Core SaaS
Multi-Tenancy (resumen)
Modelo	Isolation	Costo	Complejidad	Cuando usar
Silo	Alto	Alto	Medio	Healthcare, Finance
Pool	Bajo	Bajo	Bajo	SaaS general
Bridge	Medio	Medio	Alto	Enterprise SaaS

Ver multi-tenancy-patterns.md para detalles.

Tenant Context
// Middleware pattern
const tenantMiddleware = (req, res, next) => {
  const tenantId = req.headers['x-tenant-id'] || extractFromJWT(req);
  if (!tenantId) return res.status(401).json({ error: 'Tenant required' });
  req.tenant = tenantId;
  next();
};

// Query builder injection
const withTenant = (query, tenantId) => {
  return query.where('tenant_id', tenantId);
};

Feature Flags
// Feature flag pattern por plan
const features = {
  free: ['basic_reports'],
  pro: ['basic_reports', 'advanced_reports', 'api_access'],
  enterprise: ['basic_reports', 'advanced_reports', 'api_access', 'sso', 'audit_logs']
};

const hasFeature = (tenant, feature) => {
  return features[tenant.plan]?.includes(feature) ?? false;
};

4. Trade-offs Comunes

Monolito vs Microservicios

Monolito cuando:
- Equipo pequeno (<5 devs)
- Dominio no claramente separable
- Time-to-market prioritario

Microservicios cuando:
- Equipos independientes por servicio
- Scaling muy diferente por componente
- Diferentes stacks por servicio tienen sentido


SQL vs NoSQL para SaaS

SQL (PostgreSQL) cuando:
- Datos relacionales (users, orders, subscriptions)
- Transacciones importantes (pagos)
- Queries complejas con JOINs

NoSQL (MongoDB) cuando:
- Schemas muy variables por tenant
- Write-heavy workloads
- Document-centric data


Sync vs Async processing

Sync cuando:
- Usuario espera resultado inmediato
- Operacion rapida (<500ms)
- Feedback importante para UX

Async cuando:
- Operaciones largas (emails, reports)
- Puede fallar y necesita retry
- No bloquea al usuario

5. Checklist de Arquitectura SaaS
DATA LAYER
[ ] Tenant isolation implementado
[ ] Backup strategy por tenant o global
[ ] Data retention policies definidas
[ ] Audit logging para compliance

APPLICATION LAYER
[ ] Tenant context en cada request
[ ] Feature flags por plan
[ ] Rate limiting por tenant
[ ] Error handling con tenant context

INFRASTRUCTURE
[ ] Scaling strategy definida
[ ] Monitoring por tenant
[ ] Cost allocation posible
[ ] Disaster recovery plan

BILLING
[ ] Subscription lifecycle manejado
[ ] Usage tracking si aplica
[ ] Webhook handlers para Stripe events
[ ] Dunning flow para pagos fallidos

Referencias
Archivo	Contenido	Cuando usar
multi-tenancy-patterns.md	Pool, Silo, Bridge en detalle	Disenar multi-tenancy
billing-integration.md	Stripe subscriptions, webhooks	Integrar billing
scaling-strategies.md	Horizontal, vertical, sharding	Escalar sistema
your-architecture-answers.md	HostelOS, Digitaliza explicados	Defender tu experiencia
Weekly Installs
45
Repository
founderjourney/…e-skills
GitHub Stars
10
First Seen
Feb 8, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass