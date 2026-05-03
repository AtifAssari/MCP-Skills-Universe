---
title: configure-api-gateway
url: https://skills.sh/pjt222/development-guides/configure-api-gateway
---

# configure-api-gateway

skills/pjt222/development-guides/configure-api-gateway
configure-api-gateway
Installation
$ npx skills add https://github.com/pjt222/development-guides --skill configure-api-gateway
SKILL.md
Configure API Gateway

Deploy and configure an API gateway for centralized API traffic management and policy enforcement.

When to Use
Multiple backend services need unified API endpoint with consistent policies
Require centralized authentication/authorization for API access
Need rate limiting and quota management across APIs
Want to transform requests/responses without modifying backend services
Implementing API versioning and deprecation strategies
Need detailed API analytics and monitoring
Require service discovery and load balancing for microservices
Inputs
Required: Kubernetes cluster or Docker environment
Required: Choice of API gateway (Kong or Traefik)
Required: Backend service endpoints to proxy
Optional: Authentication provider (OAuth2, OIDC, API keys)
Optional: Rate limiting requirements (requests per minute/hour)
Optional: Custom middleware or plugin configurations
Optional: TLS certificates for HTTPS endpoints
Procedure

See Extended Examples for complete configuration files and templates.

Step 1: Install API Gateway

Deploy the API gateway with database (Kong) or file-based config (Traefik).

For Kong with PostgreSQL:

# kong-deployment.yaml (excerpt - see EXAMPLES.md for complete file)
apiVersion: v1
kind: Namespace
metadata:
  name: kong
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: kong
  namespace: kong
spec:
  replicas: 2
  # ... (PostgreSQL, migrations, services - see EXAMPLES.md)


For Traefik:

# traefik-deployment.yaml (excerpt - see EXAMPLES.md for complete file)
apiVersion: v1
kind: Namespace
metadata:
  name: traefik
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: traefik
  namespace: traefik
spec:
  replicas: 2
  # ... (RBAC, ConfigMap, services - see EXAMPLES.md)


See EXAMPLES.md for the complete deployment manifests

Deploy:

kubectl apply -f kong-deployment.yaml  # OR traefik-deployment.yaml
kubectl wait --for=condition=ready pod -l app=kong -n kong --timeout=300s
kubectl get svc -n kong kong-proxy  # Get load balancer IP


Expected: Gateway pods running with 2 replicas. Load balancer service has external IP assigned. Admin API accessible (Kong: port 8001, Traefik: dashboard port 8080). Health checks passing.

On failure:

Check pod logs: kubectl logs -n kong -l app=kong
Verify database connection (Kong): kubectl logs -n kong kong-migrations-<hash>
Check service account permissions (Traefik): kubectl get clusterrolebinding traefik -o yaml
Ensure ports not already bound: kubectl get svc --all-namespaces | grep 8000
Step 2: Configure Backend Services and Routes

Define upstream services and create routes to expose APIs.

For Kong (using decK for declarative config):

# Install decK CLI
curl -sL https://github.com/Kong/deck/releases/download/v1.28.0/deck_1.28.0_linux_amd64.tar.gz | tar -xz
sudo mv deck /usr/local/bin/

# Create kong.yaml with services, routes, upstreams
# (see EXAMPLES.md for complete configuration)
deck sync --kong-addr http://localhost:8001 -s kong.yaml
curl -i http://localhost:8001/routes  # Verify routes


For Traefik (using IngressRoute CRD):

# traefik-routes.yaml (excerpt)
apiVersion: traefik.io/v1alpha1
kind: IngressRoute
metadata:
  name: user-api-route
spec:
  entryPoints: [websecure]
  routes:
  - match: Host(`api.example.com`) && PathPrefix(`/api/users`)
    # ... (see EXAMPLES.md for full configuration)


Apply routes:

kubectl apply -f traefik-routes.yaml
curl -H "Host: api.example.com" https://GATEWAY_IP/api/users


See EXAMPLES.md for complete routing configurations

Expected: Routes correctly proxy traffic to backend services. Weighted routing distributes traffic according to configuration. Health checks monitor backend service health.

On failure:

Verify backend services running: kubectl get svc -n default
Check DNS resolution: kubectl run test --rm -it --image=busybox -- nslookup user-service.default.svc.cluster.local
Review gateway logs: kubectl logs -n kong -l app=kong --tail=50
Validate configuration: deck validate -s kong.yaml
Step 3: Implement Authentication and Authorization

Configure authentication plugins/middleware for API security.

For Kong (API Key and JWT authentication):

# kong-auth-config.yaml (excerpt)
consumers:
- username: mobile-app
  custom_id: app-001

keyauth_credentials:
- consumer: mobile-app
  key: mobile-secret-key-123

plugins:
- name: key-auth
  service: user-api
  # ... (see EXAMPLES.md for full configuration)

deck sync --kong-addr http://localhost:8001 -s kong-auth-config.yaml
curl -i -H "apikey: mobile-secret-key-123" http://GATEWAY_IP/api/users


For Traefik (BasicAuth and ForwardAuth middleware):

# traefik-auth-middleware.yaml (excerpt)
apiVersion: traefik.io/v1alpha1
kind: Middleware
metadata:
  name: basic-auth-middleware
spec:
  basicAuth:
    secret: basic-auth
    removeHeader: true
# ... (see EXAMPLES.md for OAuth2, rate limiting)

kubectl apply -f traefik-auth-middleware.yaml
curl -u user1:password https://GATEWAY_IP/api/protected


See EXAMPLES.md for complete authentication configurations

Expected: Unauthenticated requests return 401. Valid credentials allow access. Rate limiting returns 429 after threshold. JWT tokens validate correctly. ACL enforces group permissions.

On failure:

Verify consumer creation: curl http://localhost:8001/consumers
Check plugin enabled: curl http://localhost:8001/plugins | jq .
Test with verbose: curl -v to see response headers
Validate JWT: use jwt.io to decode token
Step 4: Configure Request/Response Transformation

Add middleware to transform requests and responses.

For Kong:

# kong-transformations.yaml (excerpt)
plugins:
- name: request-transformer
  service: user-api
  config:
    add:
      headers: [X-Gateway-Version:1.0, X-Request-ID:$(uuid)]
    remove:
      headers: [X-Internal-Token]
- name: correlation-id
  # ... (see EXAMPLES.md for full configuration)

deck sync --kong-addr http://localhost:8001 -s kong-transformations.yaml


For Traefik:

# traefik-transformations.yaml (excerpt)
apiVersion: traefik.io/v1alpha1
kind: Middleware
metadata:
  name: add-headers
spec:
  headers:
    customRequestHeaders:
      X-Gateway-Version: "1.0"
    # ... (see EXAMPLES.md for circuit breaker, retry, chain)

kubectl apply -f traefik-transformations.yaml
curl -v https://GATEWAY_IP/api/users | grep X-Gateway


See EXAMPLES.md for complete transformation configurations

Expected: Request headers added/removed as configured. Response headers include gateway metadata. Large requests rejected with 413. Circuit breaker trips on repeated failures. Retries occur for transient errors.

On failure:

Verify middleware order in chain
Check for header conflicts with backend services
Test transformations individually before chaining
Review logs for transformation errors
Step 5: Enable Monitoring and Analytics

Configure metrics, logging, and dashboards for API visibility.

Kong monitoring setup:

# kong-monitoring.yaml (excerpt)
plugins:
- name: prometheus
  config:
    per_consumer: true
- name: http-log
  service: user-api
  # ... (see EXAMPLES.md for Datadog, file-log configuration)

deck sync --kong-addr http://localhost:8001 -s kong-monitoring.yaml

# Deploy ServiceMonitor (see EXAMPLES.md)
kubectl apply -f kong-servicemonitor.yaml
curl http://localhost:8100/metrics


Traefik monitoring (built-in):

# ServiceMonitor (excerpt - see EXAMPLES.md for Grafana dashboard)
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: traefik-metrics
spec:
  endpoints:
  - port: metrics
    path: /metrics
    interval: 30s

kubectl port-forward -n traefik svc/traefik-dashboard 8080:8080
# Open http://localhost:8080/dashboard/


See EXAMPLES.md for complete monitoring configurations

Expected: Prometheus scraping gateway metrics successfully. Dashboards show request rates, latency percentiles, error rates. Logs forwarding to aggregation system. Metrics segmented by service, route, and consumer.

On failure:

Verify ServiceMonitor: kubectl get servicemonitor -A
Check Prometheus targets in UI
Ensure metrics port accessible: kubectl port-forward -n kong svc/kong-metrics 8100:8100
Validate log endpoint reachability
Step 6: Implement API Versioning and Deprecation

Configure version management and graceful API deprecation.

Kong versioning strategy:

# kong-versioning.yaml (excerpt)
services:
- name: user-api-v1
  url: http://user-service-v1.default.svc.cluster.local:8080
  routes:
  - name: user-v1-route
    paths: [/api/v1/users]
  plugins:
  - name: response-transformer
    config:
      add:
        headers:
        - X-Deprecation-Notice:"API v1 deprecated on 2024-12-31"
        - Sunset:"Wed, 31 Dec 2024 23:59:59 GMT"
# ... (see EXAMPLES.md for v2, default routing, rate limits)


Traefik versioning:

# traefik-versioning.yaml (excerpt)
apiVersion: traefik.io/v1alpha1
kind: Middleware
metadata:
  name: v1-deprecation-headers
spec:
  headers:
    customResponseHeaders:
      X-Deprecation-Notice: "API v1 deprecated on 2024-12-31"
# ... (see EXAMPLES.md for complete IngressRoutes)


Test versioning:

curl -i https://api.example.com/api/v1/users  # Deprecated
curl -i https://api.example.com/api/v2/users  # Current
curl -i https://api.example.com/api/users     # Routes to v2


See EXAMPLES.md for complete versioning configurations

Expected: Different versions route to appropriate backend services. Deprecation headers present on v1 responses. Rate limits stricter for deprecated versions. Default path routes to latest version. Metrics segmented by API version.

On failure:

Verify path precedence/priority configuration (higher priority = evaluated first)
Check for overlapping path patterns
Test each version route independently
Review routing logs for path matching
Ensure backend services for each version are running
Validation
 API gateway pods running with multiple replicas for HA
 Load balancer service has external IP assigned
 Routes correctly proxy traffic to backend services
 Authentication/authorization enforcing access control (401/403 responses)
 Rate limiting returns 429 after exceeding quotas
 Request/response transformation adding/removing headers correctly
 Circuit breaker trips on repeated backend failures
 Metrics exposed and scraped by Prometheus
 Dashboards showing request rates, latency, errors
 API versioning routing requests to correct backend versions
 Deprecation headers present on older API versions
 Health checks monitoring backend service availability
Common Pitfalls

Database Dependency (Kong): Kong with database requires PostgreSQL/Cassandra. DB-less mode available but limits some features (runtime config changes). Use DB mode for production with multiple gateway instances.

Path Matching Order: Routes/IngressRoutes evaluated in specific order. More specific paths should have higher priority. Overlapping paths cause unpredictable routing. Test with curl -v to verify actual route hit.

Authentication Bypass: Ensure authentication plugins applied to all routes. Easy to add route without auth. Use default plugins at service level, then override per-route as needed.

Rate Limit Scope: Rate limiting policy: local counts per gateway pod. For consistent limits across replicas, use centralized policy (Redis) or sticky sessions.

CORS Configuration: API gateway should handle CORS, not individual services. Add CORS plugin/middleware early to avoid browser preflight failures.

SSL/TLS Termination: Gateway typically terminates SSL. Ensure certificates valid and auto-renewal configured. Use cert-manager for Kubernetes certificate management.

Upstream Health Checks: Configure active health checks to detect backend failures quickly. Passive checks rely on real traffic and may be slower to detect issues.

Plugin/Middleware Execution Order: Order matters. Authentication before rate limiting (avoid wasted rate limit slots for invalid requests). Transformation before logging (log transformed values).

Resource Limits: Gateway pods can consume significant CPU under load. Set appropriate resource requests/limits. Monitor CPU throttling in production.

Migration Strategy: Don't enable all plugins at once. Roll out incrementally: routing → authentication → rate limiting → transformations → advanced features.

Related Skills
configure-ingress-networking - Ingress controller setup complements API gateway
setup-service-mesh - Service mesh provides complementary east-west traffic management
manage-kubernetes-secrets - Certificate and credential management for gateway
setup-prometheus-monitoring - Monitoring integration for gateway metrics
enforce-policy-as-code - Policy enforcement that complements gateway authorization
Weekly Installs
17
Repository
pjt222/developm…t-guides
GitHub Stars
12
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail