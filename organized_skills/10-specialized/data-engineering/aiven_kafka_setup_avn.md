---
rating: ⭐⭐⭐
title: aiven-kafka-setup-avn
url: https://skills.sh/aiven-open/aiven-skills-bundle/aiven-kafka-setup-avn
---

# aiven-kafka-setup-avn

skills/aiven-open/aiven-skills-bundle/aiven-kafka-setup-avn
aiven-kafka-setup-avn
Installation
$ npx skills add https://github.com/aiven-open/aiven-skills-bundle --skill aiven-kafka-setup-avn
SKILL.md
Aiven Kafka Setup (avn CLI)

End-to-end workflow for creating an Apache Kafka service on Aiven using the avn CLI, with SASL_SSL authentication, Avro Schema Registry, and a working Java or Python producer/consumer example that reads from CSV and writes to Kafka.

IMPORTANT: This skill ALWAYS creates a fully working example (Java by default). Steps 1–3 are all mandatory. Never stop after creating the service — you MUST also build the example project, generate test data, and run the producer + consumer end-to-end.

Step 1: Prerequisites
1.1 Verify avn CLI login

Run the following to check if the user is logged in:

avn user info


If the command fails, instruct the user:

You are not logged in to the Aiven CLI. Please run:

  avn user login <your-email>

Then confirm when you are logged in.


STOP and wait for the user to confirm login before proceeding.

1.2 Required tools

Verify the following are installed:

avn (Aiven CLI) - At least version 4.7.0 or later is required.
jq (JSON processing)
For Java: java (17+), mvn
For Python: python3 (3.9+), pip

Missing Requirements Policy:

If a library or CLI tool (like avn) is missing, advise the user on how to install it (e.g., python3 -m pip install aiven-client for avn). However, check first if python3 is available before suggesting a pip command.
If a core language runtime (python3 or java) is requested but missing, interrupt the flow immediately. Do NOT advise the user on how to install programming languages.
Step 2: Create the Kafka Service and Export Environment Variables

Follow SERVICE_CREATION_AVN.md sections 1–4 in order:

Choose a region — ask the user with AskQuestion, mapping their choice to the EXACT CLOUD_NAME from the table in SERVICE_CREATION_AVN.md.
Choose a plan — default startup-4; never use free-0 or startup-2.
Run the setup script — a single command creates the service, users, ACLs, schema, extracts all connection details, and writes them to env.sh.
Source env.sh — loads KAFKA_HOST, KAFKA_PORT, SCHEMA_REGISTRY_URL, AVNADMIN_PASS, PRODUCER_PASSWORD, CONSUMER_PASSWORD into the shell.
bash scripts/setup_aiven_kafka.sh <name> <CLOUD_NAME> <plan> 4.1
source env.sh


CRITICAL: Do NOT read or cat env.sh in the agent context — it contains passwords. Only source it and verify passwords by ${#VAR} (length).

Step 3: Create and Run the Working Example

MANDATORY: This step is NOT optional. After the Kafka service is running and environment variables are exported, you MUST create a working producer/consumer example, compile/install it, generate test data, and run it end-to-end. Default language is Java unless the user explicitly requests Python.

3.1 Ask the user which language to use

Use the AskQuestion tool:

Prompt: "Which language for the producer/consumer example?"
Options:
  - Java (default, recommended)
  - Python


If the user requests a language other than Java or Python, warn them:

"Results with languages other than Java or Python are unpredictable. It is recommended to use Java or Python for reliable results."

If the user does not answer or skips, default to Java.

3.2 Copy templates into the workspace

The templates live under this skill's templates/ directory. They MUST be copied to the workspace root so the run scripts can find them at the expected relative paths.

# Copy from the skill directory into the workspace root
cp -r <SKILL_DIR>/templates/ <WORKSPACE_ROOT>/templates/
cp -r <SKILL_DIR>/scripts/  <WORKSPACE_ROOT>/scripts/


After copying, verify the files exist:

ls templates/order.avsc
ls templates/producer_consumer_java/Producer.java   # if Java
ls templates/producer_consumer_python/producer.py    # if Python
ls scripts/run_producer.sh scripts/run_consumer.sh

3.3 Generate test data

Run the data generator (no external dependencies):

python3 scripts/generate_orders.py


This creates orders.csv with 20 rows in the format id,user_id,product,price. Verify it was created:

wc -l orders.csv   # should show 21 (1 header + 20 data rows)

3.4 Build the project
Java (default)

Set up the Maven source tree and compile:

JAVA_DIR="templates/producer_consumer_java"
mkdir -p "$JAVA_DIR/src/main/java/com/aiven/demo"
cp "$JAVA_DIR/Producer.java" "$JAVA_DIR/src/main/java/com/aiven/demo/"
cp "$JAVA_DIR/Consumer.java" "$JAVA_DIR/src/main/java/com/aiven/demo/"
cp "$JAVA_DIR/Order.java"    "$JAVA_DIR/src/main/java/com/aiven/demo/"
mvn -f "$JAVA_DIR/pom.xml" package -DskipTests


Verify the JAR was created:

ls "$JAVA_DIR/target/kafka-orders-demo-1.0-SNAPSHOT.jar"


If compilation fails, check that java (17+) and mvn are installed.

Python (if selected)

Install dependencies:

python3 -m pip install -r templates/producer_consumer_python/requirements.txt


Verify the install succeeded:

python3 -c "import confluent_kafka; print(confluent_kafka.version())"

3.5 Run the producer (start FIRST)

The producer MUST run first to publish messages into Kafka. The consumer reads them afterwards (the consumer uses auto.offset.reset=earliest, so it will pick up all messages from the beginning of the topic regardless of when it starts).

bash scripts/run_producer.sh <java|python>


Wait for the producer to finish (it will print "Done. Produced 20 messages.").

3.6 Run the consumer

After the producer has finished, start the consumer to read and process the messages:

bash scripts/run_consumer.sh <java|python>


The consumer will read all 20 messages (starting from the earliest offset), write them to orders_completed.csv, and then exit (both Java and Python exit automatically after consuming the expected 20 records).

3.7 Verify output
python3 scripts/verify_output.py


This checks that orders_completed.csv has 20 rows with correct columns and all completed_at timestamps populated.

If verification fails, check:

The producer finished successfully before the consumer was started
Environment variables (KAFKA_HOST, KAFKA_PORT, etc.) are all set
The cert/ca.pem file exists
For Java: the JAR exists in templates/producer_consumer_java/target/
For Python: confluent_kafka is installed
Step 4: Teardown Information

DO NOT run teardown automatically. Instead, inform the user how to clean up when they are ready:

When you're done with the demo, you can tear down the service by running:

bash scripts/teardown.sh "$KAFKA_SERVICE"


This will delete the Aiven Kafka service, remove the local cert/ directory, and clean up generated CSV files.

For detailed avn CLI command reference and troubleshooting, see reference.md.

File Reference
File	Purpose
SERVICE_CREATION_AVN.md	Region/plan selection (interactive), then delegates to setup script
reference.md	avn CLI cheat sheet, region map, troubleshooting
templates/order.avsc	Avro schema for orders topic
templates/producer_consumer_java/	Java Producer + Consumer + pom.xml
templates/producer_consumer_python/	Python producer + consumer + requirements.txt
scripts/generate_orders.py	Generate orders.csv (20 rows)
scripts/setup_aiven_kafka.sh	Full setup: service, users, ACLs, schema, env.sh
scripts/run_producer.sh	Run producer (Java or Python)
scripts/run_consumer.sh	Run consumer (Java or Python)
scripts/verify_output.py	Validate orders_completed.csv
scripts/teardown.sh	Delete service and clean up
Weekly Installs
9
Repository
aiven-open/aive…s-bundle
GitHub Stars
1
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn