---
rating: ⭐⭐⭐
title: drupal-hook-oop-converter
url: https://skills.sh/diegodz98/drupal-skills/drupal-hook-oop-converter
---

# drupal-hook-oop-converter

skills/diegodz98/drupal-skills/drupal-hook-oop-converter
drupal-hook-oop-converter
Installation
$ npx skills add https://github.com/diegodz98/drupal-skills --skill drupal-hook-oop-converter
SKILL.md
Drupal Hook OOP Converter
Objetivo

Migrar hooks procedurales de Drupal a clases OOP usando atributos de Drupal 11: métodos con #[Hook('...')], clase de hooks en src/Hook.
Aplica a módulos y themes (custom o contrib).

Flujo de trabajo
Paso 1 — Resolver contexto (OBLIGATORIO antes de cualquier edición)

Inferir módulo/theme por ruta y archivos del proyecto. Si es ambiguo, preguntar y esperar confirmación.

Hacer una sola pregunta:

¿Necesitás mantener compatibilidad con Drupal 10 (legacy)?

SÍ → generar wrappers #[LegacyHook] + registrar clase en services.yml
NO → solo generar la clase OOP (Drupal descubre hooks por atributos)

Si el hook no tiene soporte OOP actualmente, consultar la referencia de hooks solo procedurales (references/procedural-only-hooks.md) y preguntar igualmente:

Este hook (hook_xxx) no tiene soporte OOP en Drupal 11. ¿Querés mantener el soporte procedural actual sin migrar?

No editar archivos hasta tener el contexto resuelto y la respuesta sobre compatibilidad.

Paso 2 — Identificar candidatos
Buscar funciones en archivos .module e .inc.
Validar que realmente implementen un hook (el docblock Implements hook_* ayuda, no es requisito único).
Excluir hooks de la lista procedural → ver references/procedural-only-hooks.md.
Excluir funciones ya marcadas con #[LegacyHook].
Paso 3 — Convertir
Generar clase en src/Hook/<ClassName>.php → ver references/class-structure.md.
Convertir nombre de función a método camelCase sin prefijo del módulo.
Mantener firma exacta: tipos, referencias &, valores por defecto y retorno.
Resolver __FUNCTION__ al nombre original de la función.
Recolectar y reemitir los use de entrada en el archivo de clase generado.
Si la implementación pertenece a otro módulo, usar #[Hook('hook_name', module: 'other_module')].
Paso 4 — Inyección de dependencias

Aplica principalmente a módulos. En themes, no forzar DI.

Módulo:

Usar constructor con propiedades tipadas para servicios requeridos.
Mantener métodos de hook delgados: delegar lógica a servicios inyectados.
Reservar \Drupal::service(...) solo para wrappers legacy procedurales.
Si compatibilidad legacy = NO → no registrar clase en MODULE.services.yml.
Si compatibilidad legacy = SÍ → registrar clase en MODULE.services.yml (ver references/services-yml.md).

Theme:

No forzar constructor con dependencias ni autowire: true.
Solo registrar servicio si compatibilidad legacy = SÍ.
Si hay servicio custom, resolver con \Drupal::service('service_id').
Paso 5 — Compatibilidad legacy (solo si = SÍ)
Reemplazar cuerpo procedural por delegación al servicio: \Drupal::service(HookClass::class)->methodName(...).
Si la función original tenía return, devolver también el resultado.
Marcar la función procedural con #[LegacyHook].
Crear o actualizar MODULE.services.yml / THEME.services.yml → ver references/services-yml.md.
Caso especial

Para system_page_attachments, mantener el wrapper procedural _system_page_attachments según el comportamiento esperado de conversión.

Referencias

Leer según necesidad:

Archivo	Cuándo leerlo
references/procedural-only-hooks.md	Para verificar si un hook puede migrarse o no
references/class-structure.md	Para generar la clase OOP correctamente
references/services-yml.md	Solo cuando compatibilidad legacy = SÍ
Checklist de validación
 Cada función convertida tiene su método correspondiente.
 Nombre del método en camelCase sin prefijo del módulo.
 Atributo #[Hook('...')] correcto en cada método.
 Firma conservada (tipos, &, defaults, retorno).
 No se migraron hooks solo procedurales.

Si es módulo:

 Métodos OOP no usan \Drupal::... para lógica de negocio.
 Si legacy = NO → clase de hooks NO registrada en MODULE.services.yml.
 Si legacy = SÍ → clase de hooks registrada en MODULE.services.yml.

Si es theme:

 No se forzó autowire ni DI para servicios custom.
 Si legacy = NO → clase NO registrada en THEME.services.yml.

Si legacy = SÍ:

 Wrapper procedural con #[LegacyHook] por cada hook migrado.
 Wrapper delega a \Drupal::service(HookClass::class)->metodo(...).
 Registro correcto en archivo de servicios de la extensión.

Si legacy = NO:

 No se agregó wrapper procedural #[LegacyHook].
Weekly Installs
8
Repository
diegodz98/drupal-skills
First Seen
Mar 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass