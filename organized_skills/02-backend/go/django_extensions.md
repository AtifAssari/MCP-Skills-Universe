---
rating: ⭐⭐⭐
title: django-extensions
url: https://skills.sh/kjnez/claude-code-django/django-extensions
---

# django-extensions

skills/kjnez/claude-code-django/django-extensions
django-extensions
Installation
$ npx skills add https://github.com/kjnez/claude-code-django --skill django-extensions
SKILL.md
Django Extensions

This project has django-extensions installed. Use these commands to understand and interact with the Django project.

Introspection
Show URL Routes
python manage.py show_urls

List Model Information
# All models
python manage.py list_model_info

# Specific model with signatures and field classes
python manage.py list_model_info --model <app.Model> --signature --field-class

# All methods including private
python manage.py list_model_info --model <app.Model> --all-methods --signature

Print Settings
# All settings
python manage.py print_settings --format=pprint

# Wildcards supported
python manage.py print_settings AUTH*
python manage.py print_settings DATABASE*
python manage.py print_settings *_DIRS

Show Permissions
python manage.py show_permissions
python manage.py show_permissions <app_label>

Show Template Tags
python manage.py show_template_tags

Development
Enhanced Shell (shell_plus)
python manage.py shell_plus
python manage.py shell_plus --print-sql


Auto-imports all models. Use --dont-load app1 to skip apps.

Enhanced Dev Server (runserver_plus)
python manage.py runserver_plus
python manage.py runserver_plus --print-sql


Includes Werkzeug debugger for interactive debugging.

Database
SQL Diff (Compare Models to Schema)
python manage.py sqldiff -a        # SQL differences
python manage.py sqldiff -a -t     # Text differences (readable)

Script Execution
Run Scripts with Django Context
python manage.py runscript <script_name>
python manage.py runscript <script_name> --script-args arg1 arg2
python manage.py runscript <script_name> --traceback


Scripts in scripts/ directory must define a run() function.

Profiling
Profile Server Requests
python manage.py runprofileserver --prof-path=/tmp/profiles
python manage.py runprofileserver --use-cprofile --prof-path=/tmp/profiles
python manage.py runprofileserver --kcachegrind --prof-path=/tmp/profiles

Notes
Model notation: app.ModelName (e.g., core.EmailAccount, metabox.Thread)
Settings wildcards: AUTH*, *_DIRS, DATABASE*
Commands run from project root
Weekly Installs
12
Repository
kjnez/claude-code-django
GitHub Stars
126
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail