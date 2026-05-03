---
title: jwt_rs256_validation
url: https://skills.sh/davidcastagnetoa/skills/jwt_rs256_validation
---

# jwt_rs256_validation

skills/davidcastagnetoa/skills/jwt_rs256_validation
jwt_rs256_validation
Installation
$ npx skills add https://github.com/davidcastagnetoa/skills --skill jwt_rs256_validation
SKILL.md
jwt_rs256_validation

Los clientes del API KYC se autentican presentando un JWT firmado con RS256. El gateway valida la firma usando la clave pública del emisor (almacenada en Vault), el tiempo de expiración y los claims requeridos. RS256 es asimétrico — el gateway solo necesita la clave pública, nunca la privada.

When to use

Usar en el middleware de FastAPI que protege todos los endpoints /v1/. Rechazar con 401 cualquier request sin token válido antes de iniciar el pipeline KYC.

Instructions
Instalar: pip install python-jose[cryptography] cryptography
Cargar clave pública desde Vault al arrancar: PUBLIC_KEY = vault.read("secret/kyc/jwt_public_key").
Middleware de validación en backend/api/middleware/auth.py:
from jose import jwt, JWTError
async def verify_jwt(token: str) -> dict:
    try:
        payload = jwt.decode(token, PUBLIC_KEY, algorithms=["RS256"],
                             options={"verify_exp": True, "verify_aud": True},
                             audience="kyc-api")
        return payload
    except JWTError as e:
        raise HTTPException(status_code=401, detail="Token inválido")

Extraer sub (client_id) del payload y añadir a los contextvars de logging.
Claims obligatorios en el token: sub, exp, iat, aud="kyc-api", scope.
Cachear validaciones exitosas en Redis con TTL = exp - now - 60s para no verificar firma en cada request.
Endpoint de JWKS público en GET /.well-known/jwks.json para facilitar rotación de claves.
Notes
Nunca usar HS256 (simétrico) en producción — si la clave se filtra, cualquiera puede firmar tokens.
El tiempo de expiración del token debe ser corto: 15-60 minutos. Los clientes renuevan via refresh token.
En caso de compromiso de la clave privada, revocar publicando nueva clave en Vault + invalidar caché Redis.
Weekly Installs
8
Repository
davidcastagnetoa/skills
First Seen
Mar 3, 2026