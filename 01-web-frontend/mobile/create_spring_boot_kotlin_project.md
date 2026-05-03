---
rating: ⭐⭐⭐
title: create-spring-boot-kotlin-project
url: https://skills.sh/github/awesome-copilot/create-spring-boot-kotlin-project
---

# create-spring-boot-kotlin-project

skills/github/awesome-copilot/create-spring-boot-kotlin-project
create-spring-boot-kotlin-project
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill create-spring-boot-kotlin-project
Summary

Generate a Spring Boot Kotlin project skeleton with pre-configured databases and development services.

Downloads a Spring Boot 3.4.5 project template with Kotlin, WebFlux, R2DBC, Redis, and MongoDB dependencies via Spring Initializr
Includes Docker Compose configuration for PostgreSQL 17, Redis 6, and MongoDB 8 with pre-set credentials and volume mounts
Adds SpringDoc OpenAPI integration for Swagger UI documentation and ArchUnit for architecture testing
Requires Java 21, Docker, and Docker Compose; customizable project name, Spring Boot version, and package structure through template variables
SKILL.md
Create Spring Boot Kotlin project prompt

Please make sure you have the following software installed on your system:

Java 21
Docker
Docker Compose

If you need to custom the project name, please change the artifactId and the packageName in download-spring-boot-project-template

If you need to update the Spring Boot version, please change the bootVersion in download-spring-boot-project-template

Check Java version
Run following command in terminal and check the version of Java
java -version

Download Spring Boot project template
Run following command in terminal to download a Spring Boot project template
curl https://start.spring.io/starter.zip \
  -d artifactId=${input:projectName:demo-kotlin} \
  -d bootVersion=3.4.5 \
  -d dependencies=configuration-processor,webflux,data-r2dbc,postgresql,data-redis-reactive,data-mongodb-reactive,validation,cache,testcontainers \
  -d javaVersion=21 \
  -d language=kotlin \
  -d packageName=com.example \
  -d packaging=jar \
  -d type=gradle-project-kotlin \
  -o starter.zip

Unzip the downloaded file
Run following command in terminal to unzip the downloaded file
unzip starter.zip -d ./${input:projectName:demo-kotlin}

Remove the downloaded zip file
Run following command in terminal to delete the downloaded zip file
rm -f starter.zip

Unzip the downloaded file
Run following command in terminal to unzip the downloaded file
unzip starter.zip -d ./${input:projectName:demo-kotlin}

Add additional dependencies
Insert springdoc-openapi-starter-webmvc-ui and archunit-junit5 dependency into build.gradle.kts file
dependencies {
  implementation("org.springdoc:springdoc-openapi-starter-webflux-ui:2.8.6")
  testImplementation("com.tngtech.archunit:archunit-junit5:1.2.1")
}

Insert SpringDoc configurations into application.properties file
# SpringDoc configurations
springdoc.swagger-ui.doc-expansion=none
springdoc.swagger-ui.operations-sorter=alpha
springdoc.swagger-ui.tags-sorter=alpha

Insert Redis configurations into application.properties file
# Redis configurations
spring.data.redis.host=localhost
spring.data.redis.port=6379
spring.data.redis.password=rootroot

Insert R2DBC configurations into application.properties file
# R2DBC configurations
spring.r2dbc.url=r2dbc:postgresql://localhost:5432/postgres
spring.r2dbc.username=postgres
spring.r2dbc.password=rootroot

spring.sql.init.mode=always
spring.sql.init.platform=postgres
spring.sql.init.continue-on-error=true

Insert MongoDB configurations into application.properties file
# MongoDB configurations
spring.data.mongodb.host=localhost
spring.data.mongodb.port=27017
spring.data.mongodb.authentication-database=admin
spring.data.mongodb.username=root
spring.data.mongodb.password=rootroot
spring.data.mongodb.database=test


Create docker-compose.yaml at project root and add following services: redis:6, postgresql:17 and mongo:8.

redis service should have
password rootroot
mapping port 6379 to 6379
mounting volume ./redis_data to /data
postgresql service should have
password rootroot
mapping port 5432 to 5432
mounting volume ./postgres_data to /var/lib/postgresql/data
mongo service should have
initdb root username root
initdb root password rootroot
mapping port 27017 to 27017
mounting volume ./mongo_data to /data/db

Insert redis_data, postgres_data and mongo_data directories in .gitignore file

Run gradle clean test command to check if the project is working

./gradlew clean test

(Optional) docker-compose up -d to start the services, ./gradlew spring-boot:run to run the Spring Boot project, docker-compose rm -sf to stop the services.

Let's do this step by step.

Weekly Installs
8.3K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail