---
title: symfony-components
url: https://skills.sh/krzysztofsurdy/code-virtuoso/symfony-components
---

# symfony-components

skills/krzysztofsurdy/code-virtuoso/symfony-components
symfony-components
Installation
$ npx skills add https://github.com/krzysztofsurdy/code-virtuoso --skill symfony-components
SKILL.md
Symfony Components

Complete reference for all 38 Symfony components — patterns, APIs, configuration, and best practices for PHP 8.3+ and Symfony 7.x.

Component Index
HTTP & Runtime
HttpFoundation — Object-oriented HTTP requests/responses replacing PHP globals → reference
HttpKernel — Request handling, kernel events, controller resolution, middleware → reference
PSR-7 Bridge — Bidirectional HttpFoundation ↔ PSR-7 conversion → reference
Runtime — Decoupled bootstrapping for multiple runtime environments → reference
Messaging
Messenger — Sync/async message buses, transports (AMQP, Redis, Doctrine), middleware, envelopes → reference
Console
Console — CLI commands, input/output handling, helpers, formatters, progress bars → reference
Dependency Injection
DependencyInjection — Service container, autowiring, compiler passes, tagged services → reference
Contracts — Decoupled abstractions for interoperability (Cache, EventDispatcher, HttpClient, etc.) → reference
Forms & Validation
Form — Form creation, field types, events, data transformers, collections, theming → reference
Validator — JSR-303 constraints, custom validators, groups, severity levels → reference
OptionsResolver — Option configuration with defaults, validation, normalization, nesting → reference
Cache, Lock & Semaphore
Cache — PSR-6/PSR-16 adapters, tag-based invalidation, stampede prevention → reference
Lock — Exclusive resource locking across processes/servers (Redis, PostgreSQL, file) → reference
Semaphore — Concurrent access with configurable limits (Redis, DynamoDB) → reference
Events & Workflow
EventDispatcher — Observer/Mediator patterns, listeners, subscribers, priorities → reference
Workflow — State machines, workflow transitions, guards, metadata, events → reference
Configuration & Expressions
Config — Configuration loading, validation, caching, tree building, bundle config → reference
ExpressionLanguage — Safe expression sandbox for business rules, validation, security → reference
Yaml — YAML parsing, dumping, linting with full data type support → reference
Filesystem, Finder & Process
Filesystem — Platform-independent file/directory operations, atomic writes, path utils → reference
Finder — File search with fluent criteria (name, size, date, depth, content) → reference
Process — Secure system command execution, async processes, output streaming → reference
Serialization & Types
PropertyAccess — Read/write objects and arrays via string paths (foo.bar[baz]) → reference
PropertyInfo — Property metadata extraction (types, access, descriptions) → reference
TypeInfo — PHP type extraction, resolution, and validation → reference
VarDumper — Enhanced variable debugging with HTML/CLI formatters → reference
VarExporter — Export PHP data to OPcache-optimized code, lazy ghost/proxy objects → reference
Testing
BrowserKit — Simulated browser for programmatic HTTP, cookies, history → reference
DomCrawler — HTML/XML traversal, CSS selectors, form automation → reference
CssSelector — CSS-to-XPath conversion for DOM querying → reference
PHPUnit Bridge — Deprecation reporting, time/DNS mocking, parallel tests → reference
Data & Text Utilities
Uid — UUID (v1–v8) and ULID generation, conversion, Doctrine integration → reference
Clock — Testable time abstraction with MockClock and DatePoint → reference
Intl — Internationalization data (languages, countries, currencies, timezones) → reference
JsonPath — RFC 9535 JSONPath queries on JSON structures → reference
Mime — MIME message creation for emails and content types → reference
Ldap — LDAP/Active Directory connections, queries, and management → reference
Asset — URL generation and versioning for web assets → reference
Quick Patterns
Dependency Injection (Autowiring)
# services.yaml — most services are autowired automatically
services:
    _defaults:
        autowire: true
        autoconfigure: true
    App\:
        resource: '../src/'
        exclude: '../src/{DI,Entity,Kernel.php}'

Define a Route + Controller
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class ArticleController
{
    #[Route('/articles/{id}', methods: ['GET'])]
    public function show(int $id): Response
    {
        return new Response("Article $id");
    }
}

Dispatch a Message (Async)
use Symfony\Component\Messenger\MessageBusInterface;

class OrderService
{
    public function __construct(private MessageBusInterface $bus) {}

    public function place(Order $order): void
    {
        $this->bus->dispatch(new OrderPlaced($order->getId()));
    }
}

Create and Validate a Form
$form = $this->createForm(ArticleType::class, $article);
$form->handleRequest($request);

if ($form->isSubmitted() && $form->isValid()) {
    $em->persist($form->getData());
    $em->flush();
    return $this->redirectToRoute('article_list');
}

Cache with Tags
use Symfony\Contracts\Cache\ItemInterface;

$value = $cache->get('products_list', function (ItemInterface $item) {
    $item->expiresAfter(3600);
    $item->tag(['products']);
    return $this->repository->findAll();
});

$cache->invalidateTags(['products']);

Console Command
use Symfony\Component\Console\Attribute\AsCommand;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;

#[AsCommand(name: 'app:process', description: 'Process items')]
class ProcessCommand extends Command
{
    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $output->writeln('Processing...');
        return Command::SUCCESS;
    }
}

Event Subscriber
use Symfony\Component\EventDispatcher\EventSubscriberInterface;

class OrderSubscriber implements EventSubscriberInterface
{
    public static function getSubscribedEvents(): array
    {
        return [OrderPlacedEvent::class => 'onOrderPlaced'];
    }

    public function onOrderPlaced(OrderPlacedEvent $event): void
    {
        // Handle event
    }
}

Workflow Transition
if ($workflow->can($article, 'publish')) {
    $workflow->apply($article, 'publish');
}

Lock a Resource
$lock = $factory->createLock('pdf-generation', ttl: 30);
if ($lock->acquire()) {
    try {
        generatePdf();
    } finally {
        $lock->release();
    }
}

Best Practices
Target PHP 8.3+ and Symfony 7.x with strict typing
Use attributes over YAML/XML for routes, commands, message handlers, event listeners
Prefer autowiring — only register services manually when configuration is needed
Use Cache Contracts ($cache->get()) over raw PSR-6 for stampede prevention
Apply validation groups to support multiple form contexts
Use state machines by default; use workflows only when parallel states are needed
Create custom constraints for business logic that can't be expressed with built-in ones
Mock time and DNS in tests using PHPUnit Bridge for deterministic results
Weekly Installs
76
Repository
krzysztofsurdy/…virtuoso
GitHub Stars
17
First Seen
Mar 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass