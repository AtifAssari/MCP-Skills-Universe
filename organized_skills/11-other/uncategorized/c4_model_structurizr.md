---
rating: ⭐⭐
title: c4_model_structurizr
url: https://skills.sh/davidcastagnetoa/skills/c4_model_structurizr
---

# c4_model_structurizr

skills/davidcastagnetoa/skills/c4_model_structurizr
c4_model_structurizr
Installation
$ npx skills add https://github.com/davidcastagnetoa/skills --skill c4_model_structurizr
SKILL.md
c4_model_structurizr

El modelo C4 (Context, Containers, Components, Code) proporciona un lenguaje común para diagramar arquitecturas de software a distintos niveles de abstracción. Structurizr DSL permite escribirlos como código.

When to use

Usar para mantener actualizados los diagramas de arquitectura del sistema en 4 niveles: contexto, contenedores, componentes y código.

Instructions
Instalar Structurizr Lite: docker run -p 8080:8080 -v $(pwd):/usr/local/structurizr structurizr/lite.
Crear workspace.dsl en docs/architecture/.
Definir los 4 niveles C4 en DSL:
workspace {
  model {
    user = person "Usuario KYC"
    kyc_system = softwareSystem "Sistema KYC" {
      api_gateway = container "API Gateway" { technology "Nginx + Lua" }
      orchestrator = container "Orchestrator" { technology "FastAPI + Python" }
      ...
    }
  }
  views {
    systemContext kyc_system "Context" { include * autoLayout }
    container kyc_system "Containers" { include * autoLayout }
  }
}

Visualizar en http://localhost:8080.
Exportar a PNG/SVG para documentación.
Mantener el DSL actualizado en Git; los diagramas son generados, no editados manualmente.
Notes
Documentación C4: https://c4model.com
Structurizr: https://structurizr.com/help/dsl
Weekly Installs
23
Repository
davidcastagnetoa/skills
First Seen
Mar 2, 2026