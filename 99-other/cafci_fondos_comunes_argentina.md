---
title: cafci-fondos-comunes-argentina
url: https://skills.sh/ferminrp/agent-skills/cafci-fondos-comunes-argentina
---

# cafci-fondos-comunes-argentina

skills/ferminrp/agent-skills/cafci-fondos-comunes-argentina
cafci-fondos-comunes-argentina
Installation
$ npx skills add https://github.com/ferminrp/agent-skills --skill cafci-fondos-comunes-argentina
SKILL.md
CAFCI Fondos Comunes Argentina

Skill para consultar la API publica oficial de CAFCI directamente (sin wrappers deprecados).

API Overview
Base URL: https://api.pub.cafci.org.ar
Auth: No requiere token
Formato: JSON
Origen: API publica usada por https://www.cafci.org.ar
Shape comun: la mayoria de endpoints responde como objeto con success y data
Headers recomendados: incluir accept, origin, referer, user-agent para evitar respuestas inconsistentes del edge
Endpoints Operativos
1) Tipos de renta
GET /tipo-renta
Devuelve el catalogo de categorias y sus IDs para usar en consultas diarias (.data[]).
Ejemplos de categorias esperadas: renta fija, renta variable, mercado de dinero, mixta, pymes, retorno total, infraestructura, fondos cerrados, asg.
curl -s "https://api.pub.cafci.org.ar/tipo-renta" \
  -H "accept: application/json, text/plain, */*" \
  -H "origin: https://www.cafci.org.ar" \
  -H "referer: https://www.cafci.org.ar/" \
  -H "user-agent: Mozilla/5.0" | jq '.data'

2) Informacion diaria por tipo de renta y fecha
GET /estadisticas/informacion/diaria/{tipoRentaId}/{YYYY-MM-DD}
El tipoRentaId se obtiene desde /tipo-renta.
Leer principalmente .data.
En dias sin informacion puede venir data: [] o un objeto de error como {"error":"inexistance"}.

IMPORTANTE — estructura mixta de .data[]: el array mezcla dos tipos de registros:

Agregados (estadisticas por categoria): solo tienen fondo (label como "Region: Argentina", "Moneda: Peso Argentina") y patrimonio.
Por clase (fondos individuales): tienen fecha, vcp, ccp, patrimonio, horizonte y fondo con el nombre real de la clase.

Para filtrar solo fondos individuales usar select(.fecha != null). Para ordenar numericamente por patrimonio agregar select((.patrimonio | type) == "number") ya que algunos valores pueden ser strings.

curl -s "https://api.pub.cafci.org.ar/estadisticas/informacion/diaria/2/2026-04-20" \
  -H "accept: application/json, text/plain, */*" \
  -H "origin: https://www.cafci.org.ar" \
  -H "referer: https://www.cafci.org.ar/" \
  -H "user-agent: Mozilla/5.0" | jq '[.data[] | select(.fecha != null and (.patrimonio | type) == "number")] | sort_by(.patrimonio) | reverse | .[0:10]'

3) Listado/buscador de fondos
GET /fondo?estado=1&include=...&limit=0&order=clase_fondos.nombre
Endpoint usado por el buscador de la web para listar fondos activos y metadata relacionada.
Devuelve datos en .data[], con IDs de fondo y clases en clase_fondos[].
IMPORTANTE: tipoRentaId es un string ("4"), no un numero. Usar siempre comparacion con string: select(.tipoRentaId == "4"). Comparar con numero devuelve 0 resultados sin error.
curl -s "https://api.pub.cafci.org.ar/fondo?estado=1&include=entidad;depositaria,entidad;gerente,tipoRenta,tipoRentaMixta,region,benchmark,horizonte,duration,tipo_fondo,clase_fondo&limit=0&order=clase_fondos.nombre" \
  -H "accept: application/json, text/plain, */*" \
  -H "origin: https://www.cafci.org.ar" \
  -H "referer: https://www.cafci.org.ar/" \
  -H "user-agent: Mozilla/5.0" | jq '.data[0]'

4) Ficha de fondo por fondo+clase
GET /fondo/{fondoId}/clase/{claseId}/ficha
Requiere ambos IDs: fondo y clase.

Campos clave en .data.info:

Patrimonio actualizado (mas reciente que estadisticas diarias): .data.info.diaria.actual.patrimonio y .data.info.diaria.actual.fecha
Management fee (honorarios gerente): .data.info.mensual.honorariosComisiones.honorariosAdministracionGerente — porcentaje anual como string, ej. "1.9400"
Otros costos: .data.info.mensual.honorariosComisiones.honorariosAdministracionDepositaria, .comisionIngreso, .comisionRescate
Rendimientos: .data.info.diaria.rendimientos.day.tna, .month, .oneYear, etc.
Cartera semanal: .data.info.semanal.carteras[] con nombreActivo y share (%)
curl -s "https://api.pub.cafci.org.ar/fondo/1717/clase/5772/ficha" \
  -H "accept: application/json, text/plain, */*" \
  -H "origin: https://www.cafci.org.ar" \
  -H "referer: https://www.cafci.org.ar/" \
  -H "user-agent: Mozilla/5.0" | jq '{patrimonio: .data.info.diaria.actual.patrimonio, fecha: .data.info.diaria.actual.fecha, fee_gerente: .data.info.mensual.honorariosComisiones.honorariosAdministracionGerente}'

5) Tipos/clases de un fondo
GET /fondo/tipo-clase
Devuelve el catalogo global de tipos de clase (.data[]: Mayorista, Minorista, PyMes, General, etc.).
Se usa para traducir tipoClaseId presente en cada item de clase_fondos[].
curl -s "https://api.pub.cafci.org.ar/fondo/tipo-clase" \
  -H "accept: application/json, text/plain, */*" \
  -H "origin: https://www.cafci.org.ar" \
  -H "referer: https://www.cafci.org.ar/" \
  -H "user-agent: Mozilla/5.0" | jq '.data'

Workflow Recomendado
A) Historia diaria por categoria (tipo de renta)
Normalizar categoria pedida por el usuario (ej. "renta fija").
Consultar /tipo-renta y mapear nombre -> tipoRentaId.
Consultar /estadisticas/informacion/diaria/{tipoRentaId}/{fecha}.
Si responde sin datos (data: []) o {"error":"inexistance"}, reportar explicitamente que no hay datos para esa fecha (fin de semana o feriado) y ofrecer:
usar la ultima fecha habil anterior, o
consultar otra fecha especifica.
B) Llegar a la ficha de un fondo desde el buscador/listado
Consultar el listado de fondos (/fondo?...).
Buscar por nombre (coincidencia exacta o parcial) y seleccionar el fondo correcto.
Resolver fondoId y claseId:
usar id del fondo encontrado,
tomar claseId desde clase_fondos[].id,
usar /fondo/tipo-clase para etiquetar clase_fondos[].tipoClaseId (Mayorista/Minorista/etc).
Consultar /fondo/{fondoId}/clase/{claseId}/ficha.
Responder con resumen claro (sociedad gerente/depositaria, tipo de renta, clase, metricas relevantes de la ficha).
C) Si el usuario no especifica clase
Pedir aclaracion de clase cuando haya multiples clases validas para el fondo.
Si hay una sola clase, continuar automaticamente.
D) Top N fondos por patrimonio con management fee
Consultar /tipo-renta para obtener tipoRentaId (es string, ej. "4").
Consultar estadisticas diarias, filtrar registros individuales y ordenar:
jq '[.data[] | select(.fecha != null and (.patrimonio | type) == "number")] | sort_by(.patrimonio) | reverse | .[0:N]'

Para cada fondo del top N: buscar fondoId y claseId en el listado de fondos filtrando por tipoRentaId == "4" (string).
Consultar /fondo/{fondoId}/clase/{claseId}/ficha en paralelo (usar & + wait en bash) para obtener el fee desde .data.info.mensual.honorariosComisiones.honorariosAdministracionGerente.
Manejo de Respuestas Vacias y Errores
data: [] o {"error":"inexistance"} en /estadisticas/informacion/diaria/*: tratar como ausencia de rueda (fin de semana/feriado), no como error tecnico.
404: validar IDs de fondo/clase y ruta utilizada.
422 o validaciones: revisar formato de fecha (YYYY-MM-DD) y parametros.
Fallos de red/timeout: reintentar hasta 2 veces con breve espera.
Presentacion de Resultados
Empezar por un resumen corto y accionable.
Para historia diaria: incluir fecha consultada, categoria y cantidad de registros.
Para ficha de fondo: incluir nombre del fondo, clase usada, IDs resueltos (fondoId, claseId) y principales campos de la ficha.
Si no hubo datos, explicarlo explicitamente como posible fin de semana/feriado.
Snippets Utiles de Resolucion

Buscar IDs de tipo de renta por nombre:

curl -s "https://api.pub.cafci.org.ar/tipo-renta" \
  -H "accept: application/json, text/plain, */*" \
  -H "origin: https://www.cafci.org.ar" \
  -H "referer: https://www.cafci.org.ar/" \
  -H "user-agent: Mozilla/5.0" | jq -r '.data[] | "\(.id)\t\(.nombre)"'


Buscar un fondo por nombre y listar sus clases:

curl -s "https://api.pub.cafci.org.ar/fondo?estado=1&include=entidad;depositaria,entidad;gerente,tipoRenta,tipoRentaMixta,region,benchmark,horizonte,duration,tipo_fondo,clase_fondo&limit=0&order=clase_fondos.nombre" \
  -H "accept: application/json, text/plain, */*" \
  -H "origin: https://www.cafci.org.ar" \
  -H "referer: https://www.cafci.org.ar/" \
  -H "user-agent: Mozilla/5.0" | jq -r '.data[] | select(.nombre | ascii_downcase | contains("ahorro")) | {fondoId: .id, nombre: .nombre, clases: [.clase_fondos[] | {claseId: .id, nombre: .nombre, tipoClaseId: .tipoClaseId}] }'

Alcance

Esta skill se enfoca en:

descubrimiento de categorias (/tipo-renta)
historia diaria por categoria (/estadisticas/informacion/diaria/*)
descubrimiento de fondos por nombre (/fondo?...)
resolucion de clase y consulta de ficha (/fondo/{id}/clase/{id}/ficha, /fondo/tipo-clase)

No extender a scrapers ni wrappers legacy.

Weekly Installs
39
Repository
ferminrp/agent-skills
GitHub Stars
35
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn