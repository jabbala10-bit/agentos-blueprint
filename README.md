# 🚀 AgentOS

### Safe, Deterministic, Production-Ready Agentic AI Systems

> Build AI agents that are **observable, controllable, and production-safe** — not just demos.

---

## ✨ Why AgentOS?

Most AI systems today are:

* ❌ Non-deterministic
* ❌ Hard to debug
* ❌ Unsafe in production
* ❌ Expensive at scale

**AgentOS fixes this.**

- ✅ Constraint-aware execution
- ✅ Full observability (cost, latency, actions)
- ✅ Deterministic agent workflows
- ✅ Production-first architecture

---

## Core System Architecture 
```bash
User Input
   ↓
Planner Agent (task decomposition)
   ↓
Constraint Engine (policy enforcement)
   ↓
Executor Agent (tool calls)
   ↓
Memory Layer (RAG / context)
   ↓
Response + Observability

```

## 🔥 Core Features

### 🛡️ Constraint Engine (Safety Layer)

* Policy-based execution control (DSL-driven)
* Blocks unsafe actions (delete, financial, etc.)
* Human-in-the-loop approvals
* Action-level enforcement (not just prompts)

#### Example
```yaml
policies:
  - name: allow_read
    action: read
    effect: allow

  - name: block_delete
    action: delete
    effect: deny

  - name: financial_requires_approval
    action: financial
    effect: require_approval

  - name: api_rate_limit
    action: external_api
    condition:
      max_calls_per_minute: 60
    effect: throttle
```
#### DSL Parser
```python
import yaml

class Policy:
    def __init__(self, name, action, effect, condition=None):
        self.name = name
        self.action = action
        self.effect = effect
        self.condition = condition or {}

def load_policies(path: str):
    with open(path, "r") as f:
        data = yaml.safe_load(f)

    return [Policy(**p) for p in data["policies"]]
```
####
```python
class ConstraintEngine:
    def __init__(self, policies):
        self.policies = policies

    def evaluate(self, action: str, metadata: dict):
        for policy in self.policies:
            if policy.action == action:
                return self._apply(policy, metadata)

        return {"status": "allow"}

    def _apply(self, policy, metadata):
        if policy.effect == "deny":
            return {"status": "blocked", "reason": policy.name}

        if policy.effect == "require_approval":
            return {"status": "pending_approval"}

        if policy.effect == "throttle":
            return {"status": "throttled"}

        return {"status": "allow"}
```

#### Action Interceptor (CRITICAL)
```python
class ActionInterceptor:
    def __init__(self, constraint_engine):
        self.engine = constraint_engine

    def execute(self, action, payload):
        decision = self.engine.evaluate(action, payload)

        if decision["status"] == "blocked":
            raise Exception(f"Blocked by policy: {decision['reason']}")

        if decision["status"] == "pending_approval":
            return {"status": "waiting_human"}

        return self._execute_action(action, payload)

    def _execute_action(self, action, payload):
        # call actual tool here
        return {"status": "success", "data": payload}
```

---

### 🤖 Multi-Agent System

* Planner Agent (task decomposition)
* Executor Agent (tool execution)
* Modular agent architecture
* Typed, structured communication (no string chaos)

#### Planner Agent
```python
class PlannerAgent:
    def plan(self, user_input: str):
        return {
            "tasks": [
                {"action": "read", "target": "knowledge_base"},
                {"action": "external_api", "target": "weather_api"}
            ]
        }
```

#### Executor Agent
```python
class ExecutorAgent:
    def __init__(self, interceptor):
        self.interceptor = interceptor

    def execute(self, plan):
        results = []

        for task in plan["tasks"]:
            result = self.interceptor.execute(
                action=task["action"],
                payload=task
            )
            results.append(result)

        return results
```

#### Orchestration Flow
```python
def run_agent_system(user_input):
    plan = planner.plan(user_input)
    result = executor.execute(plan)
    return result
```
---

### 🔍 Observability First

* Full trace of every action
* Cost per query tracking
* Latency monitoring (P95)
* Debuggable execution pipeline

#### Observability Hook
``` python
def log_event(event_type, payload):
    print(f"[LOG] {event_type}: {payload}")
```
---

### ⚡ Deterministic Execution

* No hidden behavior
* Every step logged + auditable
* Schema-validated outputs
* Reproducible workflows

---

### 🔗 Production-Ready API

* FastAPI-based service
* Dockerized deployment
* Scalable architecture
* Easy integration into existing systems

---

## 🧠 Architecture Overview

```text
User Input
   ↓
Planner Agent (task decomposition)
   ↓
Constraint Engine (policy enforcement)
   ↓
Executor Agent (tool execution)
   ↓
Memory / External APIs
   ↓
Response + Observability
```

---

## 🧩 System Components

### 1. Planner Agent

* Breaks user input into structured tasks
* Ensures predictable execution flow

### 2. Constraint Engine

* Central policy enforcement layer
* Evaluates every action before execution

### 3. Action Interceptor

* Gatekeeper for all agent actions
* Applies constraint decisions in real-time

### 4. Executor Agent

* Executes tasks via tools/APIs
* Handles retries, failures, fallbacks

### 5. Observability Layer

* Logs all inputs/outputs/actions
* Enables debugging + monitoring

---

## 🛠️ Tech Stack

| Layer            | Technology                        |
| ---------------- | --------------------------------- |
| API              | FastAPI                           |
| Runtime          | Python 3.11                       |
| Containerization | Docker                            |
| Policy Engine    | Custom DSL (YAML)                 |
| Testing          | Pytest                            |
| Orchestration    | Custom pipeline (LangGraph-ready) |

---

## 📁 Project Structure

```bashagentos/
│
├── README.md
├── docs/
│   ├── architecture.md
│   ├── adr/
│   │   ├── ADR-001-orchestration.md
│   │   ├── ADR-002-memory.md
│   │   └── ADR-003-constraint-engine.md
│   ├── runbook.md
│   └── hardening-report.md
│
├── apps/
│   ├── api/                  # FastAPI backend
│   ├── worker/               # Background jobs
│   └── dashboard/            # Observability UI (optional)
│
├── agentos/
│   ├── agents/
│   │   ├── planner.py
│   │   ├── executor.py
│   │   └── base.py
│   │
│   ├── orchestration/
│   │   ├── graph.py
│   │   └── router.py
│   │
│   ├── memory/
│   │   ├── short_term.py
│   │   ├── long_term.py
│   │   └── vector_store.py
│   │
│   ├── constraints/
│   │   ├── dsl.py
│   │   ├── parser.py
│   │   ├── engine.py
│   │   └── policies/
│   │       └── default.yaml
│   │
│   ├── observability/
│   │   ├── logger.py
│   │   └── tracing.py
│   │
│   ├── tools/
│   │   ├── base.py
│   │   └── registry.py
│   │
│   └── utils/
│       └── schema.py
│
├── tests/
│   ├── test_constraints.py
│   ├── test_agents.py
│   └── test_integration.py
│
├── scripts/
│   ├── run_local.sh
│   └── seed_data.py
│
├── infra/
│   ├── docker-compose.yml
│   └── terraform/
│
└── requirements.txt
```

---

## 🚀 Quick Start

### 1. Clone Repo

```bash
git clone https://github.com/yourname/agentos.git
cd agentos
```

### 2. Run with Docker

```bash
docker compose up --build
```

### 3. Test API

```bash
curl -X POST http://localhost:8000/run \
-H "Content-Type: application/json" \
-d '{"input": "get system info"}'
```

---

## 🛡️ Example Constraint Policy

```yaml
policies:
  - name: block_delete
    action: delete
    effect: deny

  - name: financial_requires_approval
    action: financial
    effect: require_approval

  - name: allow_read
    action: read
    effect: allow
```

---

## 🧪 Testing

```bash
pytest tests/
```

---

## 📊 What Makes This Different

| Feature          | Typical AI Apps | AgentOS           |
| ---------------- | --------------- | ----------------- |
| Safety           | ❌ Prompt-based  | ✅ Policy engine   |
| Debugging        | ❌ Hard          | ✅ Fully traceable |
| Control          | ❌ Limited       | ✅ Action-level    |
| Production Ready | ❌ No            | ✅ Yes             |

---

## 💡 Use Cases

* AI copilots with safety constraints
* Autonomous workflows with approvals
* Enterprise AI systems (finance, ops)
* RAG + Agent systems with guardrails
* Cost-optimized AI pipelines

---

## 🧭 Roadmap

* [ ] LangGraph integration
* [ ] Redis memory layer
* [ ] Vector DB (RAG support)
* [ ] Role-based access control (RBAC)
* [ ] Audit logs (Postgres)
* [ ] SaaS dashboard

---

## 🤝 Contributing

Pull requests welcome. For major changes, open an issue first.

---

## 📜 License

MIT License

---

## 🚀 Vision

> The future of AI is not just intelligent —
> it is **safe, observable, and controllable**.

AgentOS is the foundation for that future.
