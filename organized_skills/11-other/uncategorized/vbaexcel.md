---
rating: ⭐⭐
title: vbaexcel
url: https://skills.sh/lunasoft2001/github-copilot-excel-analyzer/vbaexcel
---

# vbaexcel

skills/lunasoft2001/github-copilot-excel-analyzer/vbaExcel
vbaExcel
Installation
$ npx skills add https://github.com/lunasoft2001/github-copilot-excel-analyzer --skill vbaExcel
SKILL.md
vbaExcel
Uso rapido
Extraer VBA a archivos .bas.
Refactorizar los .bas.
Reimportar al .xlsm.
Flujo recomendado
1) Exportar VBA
Ejecuta el script de exportacion en scripts/export_vba.py.
Si falla el acceso a VBA, habilita AccessVBOM con scripts/enable_vba_access.reg.
2) Refactorizar
Edita los archivos .bas en VS Code (o en el editor VBA).
3) Reimportar
Ejecuta el script scripts/import_vba.py para reemplazar el codigo de cada modulo.
Notas importantes
Excel debe estar instalado.
Cierra Excel antes de exportar o importar.
Siempre crea un backup del XLSM antes de importar.
Scripts incluidos
scripts/export_vba.py: exporta VBA a .bas usando VBScript y COM.
scripts/import_vba.py: importa los .bas al XLSM via COM.
scripts/enable_vba_access.reg: habilita acceso programatico a VBA.
Cuando usar este skill
Quieres extraer VBA para refactorizar.
Quieres automatizar el reingreso del codigo VBA al XLSM.
Tienes bloqueado el acceso a VBProject y necesitas habilitarlo.
Weekly Installs
24
Repository
lunasoft2001/gi…analyzer
GitHub Stars
3
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn