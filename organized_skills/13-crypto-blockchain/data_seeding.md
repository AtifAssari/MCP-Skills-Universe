---
rating: ⭐⭐⭐
title: data-seeding
url: https://skills.sh/sgcarstrends/sgcarstrends/data-seeding
---

# data-seeding

skills/sgcarstrends/sgcarstrends/data-seeding
data-seeding
Installation
$ npx skills add https://github.com/sgcarstrends/sgcarstrends --skill data-seeding
SKILL.md
Data Seeding Skill

Seed scripts live in packages/database/src/seed/.

Running Seeds
pnpm -F @sgcarstrends/database db:seed           # Run all seeds
pnpm -F @sgcarstrends/database db:seed:cars      # Seed specific table

Basic Seed Pattern
// packages/database/src/seed/cars.ts
import { db } from "../index";
import { cars } from "../db/schema";
import { nanoid } from "nanoid";

export async function seedCars() {
  console.log("Seeding cars...");

  const carData = [
    { id: nanoid(), make: "Toyota", model: "Camry", vehicleClass: "Sedan", fuelType: "Petrol", month: "2024-01", number: 150 },
    { id: nanoid(), make: "Honda", model: "Civic", vehicleClass: "Sedan", fuelType: "Petrol", month: "2024-01", number: 120 },
  ];

  await db.insert(cars).values(carData);
  console.log(`Seeded ${carData.length} cars`);
}

Main Seed Runner
// packages/database/src/seed/index.ts
export async function seed() {
  console.log("Starting database seed...");

  await clearDatabase();  // Optional: clear existing data
  await seedCars();
  await seedCOE();
  await seedPosts();

  console.log("Database seeded successfully!");
}

async function clearDatabase() {
  // Delete in reverse order of dependencies
  await db.delete(posts);
  await db.delete(coe);
  await db.delete(cars);
}

Seed with Faker.js
pnpm -F @sgcarstrends/database add -D @faker-js/faker

import { faker } from "@faker-js/faker";

export async function seedRealisticCars(count = 100) {
  const makes = ["Toyota", "Honda", "BMW", "Mercedes"];
  const carData = Array.from({ length: count }, () => ({
    id: nanoid(),
    make: faker.helpers.arrayElement(makes),
    model: faker.vehicle.model(),
    month: faker.date.between({ from: "2020-01-01", to: "2024-12-31" }).toISOString().slice(0, 7),
    number: faker.number.int({ min: 10, max: 500 }),
  }));

  // Batch insert for performance
  const batchSize = 50;
  for (let i = 0; i < carData.length; i += batchSize) {
    await db.insert(cars).values(carData.slice(i, i + batchSize));
  }
}

Environment-Specific Seeds
export async function seed() {
  const env = process.env.NODE_ENV || "development";

  switch (env) {
    case "development":
      await seedDevelopment();  // Small, predictable dataset
      break;
    case "test":
      await seedTesting();  // Minimal, deterministic data
      break;
    case "staging":
      await seedStaging();  // Larger, production-like dataset
      break;
  }
}

Idempotent Seeds (Upsert)
await db.insert(cars).values(carData).onConflictDoUpdate({
  target: cars.id,
  set: { make: carData[0].make, number: carData[0].number, updatedAt: new Date() },
});

Check Before Insert
export async function seedIfEmpty() {
  const existing = await db.select().from(cars).limit(1);
  if (existing.length > 0) {
    console.log("Database has data, skipping seed");
    return;
  }
  await seedCars();
}

Transactions
await db.transaction(async (tx) => {
  await tx.insert(cars).values([...carData]);
  await tx.insert(coe).values([...coeData]);
});

CLI for Selective Seeding
// packages/database/scripts/seed-cli.ts
const seeders = { cars: seedCars, coe: seedCOE, posts: seedPosts, all: seedAll };
const target = process.argv[2] as keyof typeof seeders;

if (!target || !seeders[target]) {
  console.error("Usage: pnpm db:seed [cars|coe|posts|all]");
  process.exit(1);
}

seeders[target]().then(() => process.exit(0)).catch(() => process.exit(1));

Best Practices
Idempotent: Safe to run multiple times (use upserts or check-before-insert)
Environment-Specific: Different data for dev/test/staging
Batch Inserts: Use batching for large datasets
Relationships: Seed parent tables first
Transactions: Use for atomic seeding
Logging: Provide clear progress feedback
References
packages/database/CLAUDE.md for schema details
See schema-design skill for migrations
Weekly Installs
55
Repository
sgcarstrends/sg…rstrends
GitHub Stars
20
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass