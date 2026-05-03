---
title: golang-best-practices
url: https://skills.sh/difyz9/golang-best-practices/golang-best-practices
---

# golang-best-practices

skills/difyz9/golang-best-practices/golang-best-practices
golang-best-practices
Installation
$ npx skills add https://github.com/difyz9/golang-best-practices --skill golang-best-practices
SKILL.md
Golang Best Practices
Overview

This skill provides battle-tested best practices for Go development, covering project organization, error handling, concurrency patterns, testing strategies, performance optimization, and code quality standards. Use these guidelines when writing, reviewing, or refactoring Go code.

Project Structure
Standard Layout

Follow a clean and practical Go project structure:

project/
├── cmd/
│   └── server/
│       └── main.go           # Application entry point
├── internal/
│   ├── model/                # Domain models/entities
│   │   ├── user.go
│   │   └── product.go
│   ├── handler/              # HTTP handlers
│   │   ├── user_handler.go
│   │   ├── product_handler.go
│   │   └── middleware.go
│   ├── service/              # Business logic & data access
│   │   ├── user_service.go
│   │   └── product_service.go
│   └── config/               # Configuration
│       └── config.go
├── pkg/                      # Reusable utilities
│   ├── logger/
│   ├── validator/
│   └── utils/
├── migrations/               # Database migrations
│   ├── 001_create_users.up.sql
│   └── 001_create_users.down.sql
├── configs/                  # Config files
│   ├── config.yaml
│   └── config.local.yaml
├── scripts/                  # Helper scripts
│   └── build.sh
├── docs/                     # Documentation
├── Dockerfile
├── docker-compose.yml
├── go.mod
├── go.sum
├── Makefile
├── .env.example
├── .gitignore
└── README.md


Directory Explanation:

cmd/server - Application entry point, minimal main.go
internal/model - Domain entities and business models
internal/handler - HTTP request handlers and middleware
internal/service - Business logic and database operations
internal/config - Application configuration loading
pkg/ - Shared utilities that could be extracted to separate packages
migrations/ - SQL migration files for database schema
configs/ - YAML/JSON configuration files for different environments
Key Principles
Use internal/ for code that shouldn't be imported by external projects
Use pkg/ for reusable library code
Keep cmd/ minimal - just initialization and wiring
One package = one responsibility
Error Handling
Always Check Errors
// ❌ BAD
data, _ := os.ReadFile("file.txt")

// ✅ GOOD
data, err := os.ReadFile("file.txt")
if err != nil {
    return fmt.Errorf("read file: %w", err)
}

Error Wrapping

Use %w to wrap errors for error chain inspection:

if err != nil {
    return fmt.Errorf("failed to process user %s: %w", userID, err)
}

Custom Errors

Create sentinel errors and custom error types:

var ErrNotFound = errors.New("resource not found")

type ValidationError struct {
    Field string
    Err   error
}

func (e *ValidationError) Error() string {
    return fmt.Sprintf("validation failed on %s: %v", e.Field, e.Err)
}

Error Checking
// Check for specific errors
if errors.Is(err, ErrNotFound) {
    // handle not found
}

// Check error type
var valErr *ValidationError
if errors.As(err, &valErr) {
    // handle validation error
}

Concurrency
Goroutine Best Practices

Always handle goroutine lifecycle:

// ✅ Use context for cancellation
func worker(ctx context.Context) {
    for {
        select {
        case <-ctx.Done():
            return
        default:
            // do work
        }
    }
}

// ✅ Use WaitGroup for synchronization
var wg sync.WaitGroup
for i := 0; i < 10; i++ {
    wg.Add(1)
    go func(id int) {
        defer wg.Done()
        // work
    }(i)
}
wg.Wait()

Channel Patterns

Producer-Consumer:

func producer(ch chan<- int) {
    defer close(ch)
    for i := 0; i < 10; i++ {
        ch <- i
    }
}

func consumer(ch <-chan int) {
    for val := range ch {
        fmt.Println(val)
    }
}


Fan-out/Fan-in:

func fanOut(in <-chan int, workers int) []<-chan int {
    channels := make([]<-chan int, workers)
    for i := 0; i < workers; i++ {
        channels[i] = worker(in)
    }
    return channels
}

func fanIn(channels ...<-chan int) <-chan int {
    out := make(chan int)
    var wg sync.WaitGroup
    for _, ch := range channels {
        wg.Add(1)
        go func(c <-chan int) {
            defer wg.Done()
            for val := range c {
                out <- val
            }
        }(ch)
    }
    go func() {
        wg.Wait()
        close(out)
    }()
    return out
}

Avoid Race Conditions
Use sync.Mutex for shared state
Use channels for communication
Run tests with -race flag
Prefer immutable data structures
Interface Design
Small Interfaces
// ✅ Small, focused interfaces
type Reader interface {
    Read(p []byte) (n int, err error)
}

type Writer interface {
    Write(p []byte) (n int, err error)
}

// Compose when needed
type ReadWriter interface {
    Reader
    Writer
}

Accept Interfaces, Return Structs
// ✅ Accept interface for flexibility
func Process(r io.Reader) error {
    // implementation
}

// ✅ Return concrete type
func NewClient() *Client {
    return &Client{}
}

Code Quality
Naming Conventions
Use camelCase for private, PascalCase for public
Keep names short but descriptive
Avoid stuttering: user.UserID → user.ID
Use consistent naming: Get, Set, New, Init
Function Design
Keep functions small and focused
Limit parameters (max 3-4)
Use functional options for configuration:
type Option func(*Server)

func WithTimeout(d time.Duration) Option {
    return func(s *Server) {
        s.timeout = d
    }
}

func NewServer(opts ...Option) *Server {
    s := &Server{timeout: 30 * time.Second}
    for _, opt := range opts {
        opt(s)
    }
    return s
}

Constants and Enums
// Use iota for enums
type Status int

const (
    StatusPending Status = iota
    StatusActive
    StatusInactive
)

// Group related constants
const (
    maxRetries    = 3
    retryDelay    = time.Second
    timeout       = 30 * time.Second
)

Testing
Table-Driven Tests
func TestAdd(t *testing.T) {
    tests := []struct {
        name     string
        a, b     int
        expected int
    }{
        {"positive", 2, 3, 5},
        {"negative", -2, -3, -5},
        {"mixed", -2, 3, 1},
    }
    
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            result := Add(tt.a, tt.b)
            if result != tt.expected {
                t.Errorf("got %d, want %d", result, tt.expected)
            }
        })
    }
}

Test Helpers
func TestMain(m *testing.M) {
    // Setup
    code := m.Run()
    // Teardown
    os.Exit(code)
}

func setupTest(t *testing.T) func() {
    // Setup code
    return func() {
        // Cleanup code
    }
}

func TestSomething(t *testing.T) {
    cleanup := setupTest(t)
    defer cleanup()
    // test code
}

Mocking

Use interfaces for dependencies to enable testing:

type UserStore interface {
    Get(id string) (*User, error)
}

type Service struct {
    store UserStore
}

// In tests, provide mock implementation
type mockStore struct{}
func (m *mockStore) Get(id string) (*User, error) {
    return &User{ID: id}, nil
}

Performance
Memory Allocation
Pre-allocate slices when size is known: make([]int, 0, capacity)
Reuse buffers with sync.Pool
Use pointers for large structs
Avoid string concatenation in loops (use strings.Builder)
Profiling
import _ "net/http/pprof"

// CPU profiling
go func() {
    log.Println(http.ListenAndServe("localhost:6060", nil))
}()


Run profiling:

go test -cpuprofile cpu.prof -memprofile mem.prof -bench .
go tool pprof cpu.prof

Benchmarking
func BenchmarkFunction(b *testing.B) {
    for i := 0; i < b.N; i++ {
        Function()
    }
}

// With setup
func BenchmarkWithSetup(b *testing.B) {
    data := setupData()
    b.ResetTimer()
    for i := 0; i < b.N; i++ {
        Process(data)
    }
}

Dependencies
Module Management
go mod init github.com/user/project
go mod tidy
go mod vendor  # Optional: vendor dependencies

Version Pinning
go get github.com/pkg/errors@v0.9.1

Private Modules
export GOPRIVATE=github.com/myorg/*

Documentation
Package Documentation
// Package mypackage provides utilities for X.
//
// This package includes:
//   - Feature A
//   - Feature B
package mypackage

Function Documentation
// ProcessData validates and transforms the input data.
// It returns an error if validation fails.
//
// Example:
//   result, err := ProcessData(input)
//   if err != nil {
//       log.Fatal(err)
//   }
func ProcessData(input string) (string, error) {
    // implementation
}

Layered Architecture
Two-Layer Pattern

Separate concerns into distinct layers:

Handler Layer: HTTP request/response handling, input validation, routing, database operations
Service Layer: Complex business logic, external integrations, shared utilities

This simpler architecture:

Reduces complexity for most applications
Keeps data access logic close to HTTP handlers
Easier to understand and maintain
Faster development for MVPs and small-to-medium projects
Dependency Injection with Uber FX
Core Concepts

Uber FX is a dependency injection framework that manages application lifecycle and dependencies automatically.

Key Benefits:

✅ Automatic dependency resolution
✅ Built-in lifecycle management (OnStart/OnStop hooks)
✅ Clear dependency graph
✅ Easier testing with mock injection
Handler Self-Managed Routes Pattern

Each handler manages its own routes through a RegisterRoutes method:

package handler

import (
    "github.com/gin-gonic/gin"
    "gorm.io/gorm"
)

type UserHandler struct {
    db *gorm.DB
}

func NewUserHandler(db *gorm.DB) *UserHandler {
    return &UserHandler{db: db}
}

func (h *UserHandler) Register(c *gin.Context) {
    // Handle user registration
    var user User
    if err := c.ShouldBindJSON(&user); err != nil {
        c.JSON(400, gin.H{"error": err.Error()})
        return
    }
    
    if err := h.db.Create(&user).Error; err != nil {
        c.JSON(500, gin.H{"error": "failed to create user"})
        return
    }
    
    c.JSON(200, gin.H{"data": user})
}

func (h *UserHandler) Login(c *gin.Context) {
    // Handle user login
}

func (h *UserHandler) GetProfile(c *gin.Context) {
    userID := c.GetUint("user_id")
    
    var user User
    if err := h.db.First(&user, userID).Error; err != nil {
        c.JSON(404, gin.H{"error": "user not found"})
        return
    }
    
    c.JSON(200, gin.H{"data": user})
}

// RegisterRoutes - Each handler registers its own routes
func (h *UserHandler) RegisterRoutes(r *gin.Engine) {
    api := r.Group("/api/user")
    {
        api.POST("/register", h.Register)
        api.POST("/login", h.Login)
        
        // Protected routes
        auth := api.Group("", AuthMiddleware())
        {
            auth.GET("/profile", h.GetProfile)
        }
    }
}

Complete FX Application Example
package main

import (
    "context"
    "log"
    "net/http"
    "os"
    "os/signal"
    "syscall"
    "time"
    
    "github.com/gin-gonic/gin"
    "go.uber.org/fx"
    "gorm.io/driver/mysql"
    "gorm.io/gorm"
    
    "your-project/internal/config"
    "your-project/internal/handler"
    "your-project/internal/service"
    "your-project/internal/model"
)

func main() {
    app := fx.New(
        // ==================== Configuration ====================
        fx.Provide(config.Load),
        
        // ==================== Database ====================
        fx.Provide(NewDatabase),
        
        // ==================== Services ====================
        fx.Provide(service.NewEmailService),
        fx.Provide(service.NewSMSService),
        
        // ==================== Handlers ====================
        fx.Provide(handler.NewUserHandler),
        fx.Provide(handler.NewChatHandler),
        fx.Provide(handler.NewHealthHandler),
        
        // ==================== HTTP Server ====================
        fx.Provide(NewGinEngine),
        fx.Provide(NewHTTPServer),
        
        // ==================== Route Registration ====================
        fx.Invoke(RegisterAllRoutes),
        
        // ==================== Lifecycle ====================
        fx.Invoke(RegisterLifecycle),
    )
    
    // Start application
    startCtx, cancel := context.WithTimeout(context.Background(), 15*time.Second)
    defer cancel()
    
    if err := app.Start(startCtx); err != nil {
        log.Fatal("failed to start application:", err)
    }
    
    log.Println("✅ Application started successfully")
    
    // Wait for interrupt signal
    quit := make(chan os.Signal, 1)
    signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
    <-quit
    
    log.Println("📡 Shutting down gracefully...")
    
    // Graceful shutdown
    stopCtx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
    defer cancel()
    
    if err := app.Stop(stopCtx); err != nil {
        log.Fatal("failed to stop application:", err)
    }
    
    log.Println("👋 Application stopped")
}

// NewDatabase creates database connection with lifecycle management
func NewDatabase(lc fx.Lifecycle, cfg *config.Config) (*gorm.DB, error) {
    db, err := gorm.Open(mysql.Open(cfg.Database.DSN), &gorm.Config{})
    if err != nil {
        return nil, err
    }
    
    sqlDB, err := db.DB()
    if err != nil {
        return nil, err
    }
    
    // Configure connection pool
    sqlDB.SetMaxIdleConns(10)
    sqlDB.SetMaxOpenConns(100)
    sqlDB.SetConnMaxLifetime(time.Hour)
    
    // Auto-migrate models
    if err := db.AutoMigrate(&model.User{}, &model.Chat{}); err != nil {
        return nil, err
    }
    
    lc.Append(fx.Hook{
        OnStart: func(ctx context.Context) error {
            log.Println("📊 Database connected")
            return sqlDB.Ping()
        },
        OnStop: func(ctx context.Context) error {
            log.Println("📊 Closing database connection")
            return sqlDB.Close()
        },
    })
    
    return db, nil
}

// NewGinEngine creates Gin engine with middleware
func NewGinEngine(cfg *config.Config) *gin.Engine {
    if cfg.App.Env == "production" {
        gin.SetMode(gin.ReleaseMode)
    }
    
    engine := gin.New()
    engine.Use(gin.Recovery())
    engine.Use(LoggerMiddleware())
    engine.Use(CORSMiddleware())
    
    return engine
}

// NewHTTPServer creates HTTP server with lifecycle
func NewHTTPServer(lc fx.Lifecycle, engine *gin.Engine, cfg *config.Config) *http.Server {
    srv := &http.Server{
        Addr:           cfg.Server.Address,
        Handler:        engine,
        ReadTimeout:    cfg.Server.ReadTimeout,
        WriteTimeout:   cfg.Server.WriteTimeout,
        MaxHeaderBytes: 1 << 20,
    }
    
    lc.Append(fx.Hook{
        OnStart: func(ctx context.Context) error {
            go func() {
                log.Printf("🚀 HTTP server listening on %s", cfg.Server.Address)
                if err := srv.ListenAndServe(); err != nil && err != http.ErrServerClosed {
                    log.Fatal("HTTP server error:", err)
                }
            }()
            return nil
        },
        OnStop: func(ctx context.Context) error {
            log.Println("🛑 Shutting down HTTP server")
            return srv.Shutdown(ctx)
        },
    })
    
    return srv
}

// RegisterAllRoutes registers all handler routes
func RegisterAllRoutes(
    engine *gin.Engine,
    healthHandler *handler.HealthHandler,
    userHandler *handler.UserHandler,
    chatHandler *handler.ChatHandler,
) {
    healthHandler.RegisterRoutes(engine)
    userHandler.RegisterRoutes(engine)
    chatHandler.RegisterRoutes(engine)
    
    log.Println("✅ All routes registered")
}

// RegisterLifecycle adds global lifecycle hooks
func RegisterLifecycle(lc fx.Lifecycle) {
    lc.Append(fx.Hook{
        OnStart: func(ctx context.Context) error {
            log.Println("🎯 Application starting...")
            return nil
        },
        OnStop: func(ctx context.Context) error {
            log.Println("🎯 Application stopping...")
            return nil
        },
    })
}

Service Layer with FX

When business logic is complex, extract it to services:

package service

import (
    "fmt"
    "gorm.io/gorm"
)

type EmailService struct {
    db     *gorm.DB
    apiKey string
}

func NewEmailService(db *gorm.DB, cfg *config.Config) *EmailService {
    return &EmailService{
        db:     db,
        apiKey: cfg.Email.APIKey,
    }
}

func (s *EmailService) SendWelcome(email string) error {
    // Complex email sending logic
    return nil
}

func (s *EmailService) SendVerification(userID uint) error {
    var user User
    if err := s.db.First(&user, userID).Error; err != nil {
        return fmt.Errorf("user not found: %w", err)
    }
    
    // Generate verification token and send email
    return nil
}

Handler Using Service
type UserHandler struct {
    db           *gorm.DB
    emailService *service.EmailService
}

func NewUserHandler(db *gorm.DB, emailService *service.EmailService) *UserHandler {
    return &UserHandler{
        db:           db,
        emailService: emailService,
    }
}

func (h *UserHandler) Register(c *gin.Context) {
    var user User
    if err := c.ShouldBindJSON(&user); err != nil {
        c.JSON(400, gin.H{"error": err.Error()})
        return
    }
    
    // Direct database access for simple operations
    if err := h.db.Create(&user).Error; err != nil {
        c.JSON(500, gin.H{"error": "failed to create user"})
        return
    }
    
    // Use service for complex operations
    go h.emailService.SendWelcome(user.Email)
    
    c.JSON(200, gin.H{"data": user})
}

FX Best Practices

DO ✅

Use constructor functions that return pointers: func NewX() *X
Inject dependencies via constructor parameters
Use fx.Lifecycle for startup/shutdown logic
Keep handlers focused on HTTP concerns
Extract complex logic to services

DON'T ❌

Don't access gin.Context in services
Don't create global variables
Don't mix HTTP logic with business logic
Don't forget to handle lifecycle errors
Don't create circular dependencies
Testing with FX
func TestUserHandler(t *testing.T) {
    // Create test database
    db, _ := gorm.Open(sqlite.Open(":memory:"), &gorm.Config{})
    db.AutoMigrate(&User{})
    
    // Create mock service
    emailService := &MockEmailService{}
    
    // Inject dependencies manually for testing
    handler := NewUserHandler(db, emailService)
    
    // Test handler methods
    w := httptest.NewRecorder()
    c, _ := gin.CreateTestContext(w)
    
    handler.Register(c)
    
    assert.Equal(t, 200, w.Code)
}


See references/fx-architecture.md for complete implementation examples.

Resources

See the bundled references for detailed guides:

references/fx-architecture.md: Complete Fx dependency injection architecture with handlers, services, GORM repositories, and configuration management
references/patterns.md: Common Go design patterns and idioms
references/stdlib.md: Essential standard library packages guide
references/tools.md: Development tools and linters configuration
Weekly Installs
70
Repository
difyz9/golang-b…ractices
GitHub Stars
1
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass