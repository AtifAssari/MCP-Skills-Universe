---
rating: ⭐⭐⭐
title: django-components
url: https://skills.sh/krzysztofsurdy/code-virtuoso/django-components
---

# django-components

skills/krzysztofsurdy/code-virtuoso/django-components
django-components
Installation
$ npx skills add https://github.com/krzysztofsurdy/code-virtuoso --skill django-components
SKILL.md
Django Components

Complete reference for all 33 Django components -- patterns, APIs, configuration, and best practices for Python 3.10+ and Django 6.0.

Component Index
Models & Database
Models -- Model definition, field types, Meta options, inheritance, managers -> reference
QuerySets -- QuerySet API, field lookups, Q objects, F expressions, aggregation -> reference
Migrations -- Migration workflow, operations, data migrations, squashing -> reference
Database Functions -- Database functions, conditional expressions, full-text search -> reference
Views & HTTP
Views -- Function-based views, shortcuts (render, redirect, get_object_or_404) -> reference
Class-Based Views -- ListView, DetailView, CreateView, UpdateView, DeleteView, mixins -> reference
URL Routing -- URL configuration, path(), re_path(), namespaces, reverse() -> reference
Middleware -- Middleware architecture, built-in middleware, custom middleware -> reference
Request & Response -- HttpRequest, HttpResponse, JsonResponse, StreamingHttpResponse -> reference
Templates
Templates -- Template language, tags, filters, inheritance, custom template tags -> reference
Forms
Forms -- Form class, fields, widgets, ModelForm, formsets, validation -> reference
Admin
Admin -- ModelAdmin, list_display, fieldsets, inlines, actions, customization -> reference
Authentication & Security
Authentication -- User model, login/logout, permissions, groups, custom user models -> reference
Security -- CSRF, XSS, clickjacking, SSL, CSP, cryptographic signing -> reference
Sessions -- Session framework, backends, configuration -> reference
Caching
Cache -- Cache backends (Redis, Memcached, DB, filesystem), per-view/template caching -> reference
Signals
Signals -- Signal dispatcher, built-in signals (pre_save, post_save, etc.) -> reference
Communication
Email -- send_mail, EmailMessage, HTML emails, backends -> reference
Messages -- Messages framework, levels, storage backends -> reference
Testing
Testing -- TestCase, Client, assertions, RequestFactory, fixtures -> reference
Files & Static Assets
Files -- File objects, storage API, file uploads, custom storage -> reference
Static Files -- Static file configuration, collectstatic, ManifestStaticFilesStorage -> reference
Internationalization
I18n -- Translation, localization, timezones, message files -> reference
Serialization & Data
Serialization -- Serializers, JSON/XML formats, natural keys, fixtures -> reference
Content Types -- ContentType model, generic relations -> reference
Validators -- Built-in validators, custom validators -> reference
Pagination -- Paginator, Page objects, template integration -> reference
Async & Tasks
Async -- Async views, async ORM, sync_to_async, ASGI -> reference
Tasks -- Tasks framework, task backends, scheduling -> reference
Configuration & CLI
Settings -- Settings reference by category, splitting settings -> reference
Management Commands -- Built-in commands, custom commands, call_command -> reference
Logging -- Logging configuration, handlers, Django loggers -> reference
Deployment
Deployment -- WSGI, ASGI, Gunicorn, Uvicorn, static files, checklist -> reference
Quick Patterns
Define a Model
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

Define a URL + View
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('articles/<int:pk>/', views.article_detail, name='article_detail'),
]

# views.py
from django.shortcuts import render, get_object_or_404

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'articles/detail.html', {'article': article})

Class-Based View
from django.views.generic import ListView, DetailView

class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.filter(published=True)
    paginate_by = 20

class ArticleDetailView(DetailView):
    model = Article
    slug_field = 'slug'

QuerySet Filtering
from django.db.models import Q, F, Count

# Complex filtering
articles = Article.objects.filter(
    Q(title__icontains='django') | Q(content__icontains='django'),
    published=True,
).exclude(
    author__is_active=False
).annotate(
    comment_count=Count('comments')
).order_by('-created_at')

Form with Validation
from django import forms

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'slug', 'content', 'published']

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError('Title must be at least 5 characters.')
        return title

Cache a View
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)  # 15 minutes
def article_list(request):
    articles = Article.objects.filter(published=True)
    return render(request, 'articles/list.html', {'articles': articles})

Signal Receiver
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Article)
def notify_on_publish(sender, instance, created, **kwargs):
    if instance.published and created:
        send_notification(instance)

Management Command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Process pending articles'

    def add_arguments(self, parser):
        parser.add_argument('--limit', type=int, default=100)

    def handle(self, *args, **options):
        count = process_articles(limit=options['limit'])
        self.stdout.write(self.style.SUCCESS(f'Processed {count} articles'))

Test Case
from django.test import TestCase

class ArticleTests(TestCase):
    def setUp(self):
        self.article = Article.objects.create(
            title='Test Article',
            slug='test-article',
            content='Content here',
            published=True,
        )

    def test_article_detail_view(self):
        response = self.client.get(f'/articles/{self.article.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Article')

Best Practices
Target Python 3.10+ and Django 6.0 with type hints where helpful
Use class-based views for CRUD; function-based views for custom logic
Prefer select_related/prefetch_related to avoid N+1 queries
Use F expressions for database-level operations instead of Python
Apply migrations atomically -- one logical change per migration
Use Django's cache framework with Redis or Memcached in production
Write TestCase tests with assertions specific to Django (assertContains, assertRedirects)
Use custom user models from the start (AUTH_USER_MODEL)
Enable CSRF protection everywhere -- never use @csrf_exempt without good reason
Use environment variables for secrets -- never commit SECRET_KEY or database credentials
Deploy with Gunicorn/Uvicorn behind a reverse proxy (nginx)
Run manage.py check --deploy before every production deployment
Weekly Installs
18
Repository
krzysztofsurdy/…virtuoso
GitHub Stars
17
First Seen
Mar 8, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass