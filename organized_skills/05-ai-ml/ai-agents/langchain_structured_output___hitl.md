---
title: langchain structured output & hitl
url: https://skills.sh/langchain-ai/langchain-skills/langchain-structured-output-&-hitl
---

# langchain structured output & hitl

skills/langchain-ai/langchain-skills/LangChain Structured Output & HITL
LangChain Structured Output & HITL
Installation
$ npx skills add https://github.com/langchain-ai/langchain-skills --skill 'LangChain Structured Output & HITL'
SKILL.md
Structured Output: Transform unstructured model responses into validated, typed data
Human-in-the-Loop: Add human oversight to agent tool calls, pausing for approval

Key Concepts:

response_format: Define expected output schema
with_structured_output(): Model method for direct structured output
human_in_the_loop_middleware: Pauses execution for human decisions
Use Case	Use Structured Output?
Extract contact info, dates	Yes
Form filling	Yes
API integration	Yes
Open-ended Q&A	No
Structured Output

class ContactInfo(BaseModel): name: str email: str = Field(pattern=r"^[^@]+@[^@]+.[^@]+$") phone: str

agent = create_agent(model="gpt-4", response_format=ContactInfo)

result = agent.invoke({ "messages": [{"role": "user", "content": "Extract: John Doe, john@example.com, (555) 123-4567"}] }) print(result["structured_response"])

ContactInfo(name='John Doe', email='john@example.com', phone='(555) 123-4567')
</python>
<typescript>
Extract contact information from text using a Zod schema with email validation.
```typescript
import { ChatOpenAI } from "@langchain/openai";
import { z } from "zod";

const ContactInfo = z.object({
  name: z.string(),
  email: z.string().email(),
  phone: z.string(),
});

const model = new ChatOpenAI({ model: "gpt-4" });
const structuredModel = model.withStructuredOutput(ContactInfo);

const response = await structuredModel.invoke(
  "Extract: John Doe, john@example.com, (555) 123-4567"
);
console.log(response);
// { name: 'John Doe', email: 'john@example.com', phone: '(555) 123-4567' }


class Movie(BaseModel): """Movie information.""" title: str = Field(description="Movie title") year: int = Field(description="Release year") director: str rating: float = Field(ge=0, le=10)

model = ChatOpenAI(model="gpt-4") structured_model = model.with_structured_output(Movie)

response = structured_model.invoke("Tell me about Inception") print(response)

Movie(title="Inception", year=2010, director="Christopher Nolan", rating=8.8)
</python>
<typescript>
Get movie details as a validated Zod object using withStructuredOutput().
```typescript
import { ChatOpenAI } from "@langchain/openai";
import { z } from "zod";

const Movie = z.object({
  title: z.string().describe("Movie title"),
  year: z.number().describe("Release year"),
  director: z.string(),
  rating: z.number().min(0).max(10),
});

const model = new ChatOpenAI({ model: "gpt-4" });
const structuredModel = model.withStructuredOutput(Movie);

const response = await structuredModel.invoke("Tell me about Inception");
// { title: "Inception", year: 2010, director: "Christopher Nolan", rating: 8.8 }


class Classification(BaseModel): category: Literal["urgent", "normal", "low"] sentiment: Literal["positive", "neutral", "negative"] confidence: float = Field(ge=0, le=1)

</python>
<typescript>
Define a classification schema with constrained enum values using z.enum().
```typescript
import { z } from "zod";

const Classification = z.object({
  category: z.enum(["urgent", "normal", "low"]),
  sentiment: z.enum(["positive", "neutral", "negative"]),
  confidence: z.number().min(0).max(1),
});


class Address(BaseModel): street: str city: str state: str zip: str

class Person(BaseModel): name: str age: int = Field(gt=0) email: str address: Address tags: List[str] = Field(default_factory=list)

</python>
</ex-complex-nested-schema>

---

## Human-in-the-Loop

<ex-basic-hitl-setup>
<python>
Set up an agent with HITL middleware that pauses before sending emails for approval.
```python
from langchain.agents import create_agent, human_in_the_loop_middleware
from langgraph.checkpoint.memory import MemorySaver
from langchain.tools import tool

@tool
def send_email(to: str, subject: str, body: str) -> str:
    """Send an email."""
    return f"Email sent to {to}"

agent = create_agent(
    model="gpt-4",
    tools=[send_email],
    checkpointer=MemorySaver(),  # Required for HITL
    middleware=[
        human_in_the_loop_middleware(
            interrupt_on={
                "send_email": {"allowed_decisions": ["approve", "edit", "reject"]},
            }
        )
    ],
)


const sendEmail = tool( async ({ to, subject, body }) => Email sent to ${to}, { name: "send_email", description: "Send an email", schema: z.object({ to: z.string(), subject: z.string(), body: z.string() }), } );

const agent = createReactAgent({ llm: model, tools: [sendEmail], checkpointer: new MemorySaver(), // Required for HITL interruptBefore: ["send_email"], });

</typescript>
</ex-basic-hitl-setup>

<ex-running-with-interrupts>
<python>
Run the agent, detect an interrupt, then resume execution after human approval.
```python
from langgraph.types import Command

config = {"configurable": {"thread_id": "session-1"}}

# Step 1: Agent runs until it needs to call tool
result1 = agent.invoke({
    "messages": [{"role": "user", "content": "Send email to john@example.com"}]
}, config=config)

# Check for interrupt
if "__interrupt__" in result1:
    print(f"Waiting for approval: {result1['__interrupt__']}")

# Step 2: Human approves
result2 = agent.invoke(
    Command(resume={"decisions": [{"type": "approve"}]}),
    config=config
)


const config = { configurable: { thread_id: "session-1" } };

// Step 1: Agent runs until it needs to call tool const result1 = await agent.invoke({ messages: [{ role: "user", content: "Send email to john@example.com" }] }, config);

// Check for interrupt if (result1.interrupt) { console.log(Waiting for approval: ${result1.__interrupt__}); }

// Step 2: Human approves const result2 = await agent.invoke( new Command({ resume: { decisions: [{ type: "approve" }] } }), config );

</typescript>
</ex-running-with-interrupts>

<ex-editing-tool-arguments>
<python>
Edit the tool arguments before approving when the original values need correction.
```python
# Human edits the arguments
result2 = agent.invoke(
    Command(resume={
        "decisions": [{
            "type": "edit",
            "args": {
                "to": "alice@company.com",  # Fixed email
                "subject": "Project Meeting - Updated",
                "body": "...",
            },
        }]
    }),
    config=config
)


Structured Output:

Schema structure: Any valid Pydantic/Zod model
Field validation: Types, ranges, regex, etc.

HITL:

Which tools require approval
Allowed decisions per tool (approve, edit, reject)
CORRECT

print(result["structured_response"])

</python>
<typescript>
With withStructuredOutput, response IS the structured data.
```typescript
const response = await structuredModel.invoke("...");
console.log(response);  // Directly the parsed object

CORRECT

class Data(BaseModel): date: str = Field(description="Date in YYYY-MM-DD format") amount: float = Field(description="Amount in USD")

</python>
<typescript>
Add field descriptions to guide the model on expected formats.
```typescript
// WRONG
const Data = z.object({ date: z.string(), amount: z.number() });

// CORRECT
const Data = z.object({
  date: z.string().describe("Date in YYYY-MM-DD format"),
  amount: z.number().describe("Amount in USD"),
});

CORRECT

class Data(BaseModel): items: List[str] = Field(default_factory=list)

</python>
</fix-not-using-correct-type-hints>

<fix-missing-checkpointer>
<python>
HITL middleware requires a checkpointer to persist state.
```python
# WRONG
agent = create_agent(model="gpt-4", tools=[send_email], middleware=[human_in_the_loop_middleware({...})])

# CORRECT
agent = create_agent(
    model="gpt-4", tools=[send_email],
    checkpointer=MemorySaver(),  # Required
    middleware=[human_in_the_loop_middleware({...})]
)


// CORRECT const agent = createReactAgent({ llm: model, tools: [sendEmail], checkpointer: new MemorySaver(), // Required interruptBefore: ["send_email"] });

</typescript>
</fix-missing-checkpointer>

<fix-no-thread-id>
<python>
Always provide thread_id when using HITL to track conversation state.
```python
# WRONG
agent.invoke(input)  # No config!

# CORRECT
agent.invoke(input, config={"configurable": {"thread_id": "user-123"}})

CORRECT

from langgraph.types import Command agent.invoke(Command(resume={"decisions": [{"type": "approve"}]}), config=config)

</python>
<typescript>
Use Command class to resume execution after an interrupt.
```typescript
// WRONG
await agent.invoke({ resume: { decisions: [...] } });

// CORRECT
import { Command } from "@langchain/langgraph";
await agent.invoke(new Command({ resume: { decisions: [{ type: "approve" }] } }), config);

Weekly Installs
–
Repository
langchain-ai/la…n-skills
GitHub Stars
643
First Seen
–