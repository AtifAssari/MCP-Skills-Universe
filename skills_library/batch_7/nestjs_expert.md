---
title: nestjs-expert
url: https://skills.sh/jeffallan/claude-skills/nestjs-expert
---

# nestjs-expert

skills/jeffallan/claude-skills/nestjs-expert
nestjs-expert
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill nestjs-expert
Summary

Enterprise-grade NestJS module scaffolding with dependency injection, validation, authentication, and testing patterns.

Generates complete module architecture including controllers, services, DTOs, guards, and interceptors with proper TypeScript typing and dependency injection wiring
Includes class-validator decorators for input validation, Swagger/OpenAPI documentation, and typed HTTP exception handling across all layers
Covers authentication patterns (JWT, Passport), TypeORM/Prisma integration, and modular organization for scalable backend applications
Provides unit and E2E testing templates using Jest and Supertest, plus reference guides for controllers, services, DTOs, and Express migration
SKILL.md
NestJS Expert

Senior NestJS specialist with deep expertise in enterprise-grade, scalable TypeScript backend applications.

Core Workflow
Analyze requirements — Identify modules, endpoints, entities, and relationships
Design structure — Plan module organization and inter-module dependencies
Implement — Create modules, services, and controllers with proper DI wiring
Secure — Add guards, validation pipes, and authentication
Verify — Run npm run lint, npm run test, and confirm DI graph with nest info
Test — Write unit tests for services and E2E tests for controllers
Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
Controllers	references/controllers-routing.md	Creating controllers, routing, Swagger docs
Services	references/services-di.md	Services, dependency injection, providers
DTOs	references/dtos-validation.md	Validation, class-validator, DTOs
Authentication	references/authentication.md	JWT, Passport, guards, authorization
Testing	references/testing-patterns.md	Unit tests, E2E tests, mocking
Express Migration	references/migration-from-express.md	Migrating from Express.js to NestJS
Code Examples
Controller with DTO Validation and Swagger
// create-user.dto.ts
import { IsEmail, IsString, MinLength } from 'class-validator';
import { ApiProperty } from '@nestjs/swagger';

export class CreateUserDto {
  @ApiProperty({ example: 'user@example.com' })
  @IsEmail()
  email: string;

  @ApiProperty({ example: 'strongPassword123', minLength: 8 })
  @IsString()
  @MinLength(8)
  password: string;
}

// users.controller.ts
import { Body, Controller, Post, HttpCode, HttpStatus } from '@nestjs/common';
import { ApiCreatedResponse, ApiTags } from '@nestjs/swagger';
import { UsersService } from './users.service';
import { CreateUserDto } from './dto/create-user.dto';

@ApiTags('users')
@Controller('users')
export class UsersController {
  constructor(private readonly usersService: UsersService) {}

  @Post()
  @HttpCode(HttpStatus.CREATED)
  @ApiCreatedResponse({ description: 'User created successfully.' })
  create(@Body() createUserDto: CreateUserDto) {
    return this.usersService.create(createUserDto);
  }
}

Service with Dependency Injection and Error Handling
// users.service.ts
import { Injectable, ConflictException, NotFoundException } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { User } from './entities/user.entity';
import { CreateUserDto } from './dto/create-user.dto';

@Injectable()
export class UsersService {
  constructor(
    @InjectRepository(User)
    private readonly usersRepository: Repository<User>,
  ) {}

  async create(createUserDto: CreateUserDto): Promise<User> {
    const existing = await this.usersRepository.findOneBy({ email: createUserDto.email });
    if (existing) {
      throw new ConflictException('Email already registered');
    }
    const user = this.usersRepository.create(createUserDto);
    return this.usersRepository.save(user);
  }

  async findOne(id: number): Promise<User> {
    const user = await this.usersRepository.findOneBy({ id });
    if (!user) {
      throw new NotFoundException(`User #${id} not found`);
    }
    return user;
  }
}

Module Definition
// users.module.ts
import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { UsersController } from './users.controller';
import { UsersService } from './users.service';
import { User } from './entities/user.entity';

@Module({
  imports: [TypeOrmModule.forFeature([User])],
  controllers: [UsersController],
  providers: [UsersService],
  exports: [UsersService], // export only when other modules need this service
})
export class UsersModule {}

Unit Test for Service
// users.service.spec.ts
import { Test, TestingModule } from '@nestjs/testing';
import { getRepositoryToken } from '@nestjs/typeorm';
import { ConflictException } from '@nestjs/common';
import { UsersService } from './users.service';
import { User } from './entities/user.entity';

const mockRepo = {
  findOneBy: jest.fn(),
  create: jest.fn(),
  save: jest.fn(),
};

describe('UsersService', () => {
  let service: UsersService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [
        UsersService,
        { provide: getRepositoryToken(User), useValue: mockRepo },
      ],
    }).compile();
    service = module.get<UsersService>(UsersService);
    jest.clearAllMocks();
  });

  it('throws ConflictException when email already exists', async () => {
    mockRepo.findOneBy.mockResolvedValue({ id: 1, email: 'user@example.com' });
    await expect(
      service.create({ email: 'user@example.com', password: 'pass1234' }),
    ).rejects.toThrow(ConflictException);
  });
});

Constraints
MUST DO
Use @Injectable() and constructor injection for all services — never instantiate services with new
Validate all inputs with class-validator decorators on DTOs and enable ValidationPipe globally
Use DTOs for all request/response bodies; never pass raw req.body to services
Throw typed HTTP exceptions (NotFoundException, ConflictException, etc.) in services
Document all endpoints with @ApiTags, @ApiOperation, and response decorators
Write unit tests for every service method using Test.createTestingModule
Store all config values via ConfigModule and process.env; never hardcode them
MUST NOT DO
Expose passwords, secrets, or internal stack traces in responses
Accept unvalidated user input — always apply ValidationPipe
Use any type unless absolutely necessary and documented
Create circular dependencies between modules — use forwardRef() only as a last resort
Hardcode hostnames, ports, or credentials in source files
Skip error handling in service methods
Output Templates

When implementing a NestJS feature, provide in this order:

Module definition (.module.ts)
Controller with Swagger decorators (.controller.ts)
Service with typed error handling (.service.ts)
DTOs with class-validator decorators (dto/*.dto.ts)
Unit tests for service methods (*.service.spec.ts)
Knowledge Reference

NestJS, TypeScript, TypeORM, Prisma, Passport, JWT, class-validator, class-transformer, Swagger/OpenAPI, Jest, Supertest, Guards, Interceptors, Pipes, Filters

Documentation

Weekly Installs
2.1K
Repository
jeffallan/claude-skills
GitHub Stars
8.7K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass