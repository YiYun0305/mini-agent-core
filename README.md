# Mini Agent Core

A lightweight local-first AI Agent Framework built with Python, Ollama, and Qwen.

Mini Agent Core demonstrates the core building blocks of an autonomous AI Agent:

- Local LLM Integration
- Tool Registry
- Tool Decorators
- Structured Memory
- Conversation History
- Planner
- Executor
- Dynamic Tool Selection
- Tool Chains
- Agent Loop

The project runs entirely locally using Ollama and Qwen models.

---

# Features

## Local LLM

Powered by:

- Ollama
- Qwen3:8B

No OpenAI API required.

---

## Structured Memory

Persistent JSON-based memory:

```json
{
  "project": "Mini Agent Core",
  "name": "Wang",
  "city": "Boston"
}
```

Examples:

```bash
python main.py "记住项目名：Mini Agent Core"
python main.py "我的项目叫什么"
```

---

## Conversation History

Short-term memory stored in:

```text
history.json
```

Supports contextual follow-up questions.

Example:

```bash
python main.py "我叫王"
python main.py "我刚才说我叫什么"
```

---

## Planner

The planner analyzes a task before execution.

Example:

```bash
python main.py "帮我制定一个14天学习AI Agent的计划"
```

Output:

```text
1. Learn AI Agent fundamentals
2. Build projects
3. Study memory systems
...
```

---

## Executor

Executes planned actions automatically.

Example:

```bash
python main.py "帮我写一份AI Agent学习计划并保存"
```

---

## Dynamic Tool Selection

The agent automatically selects tools based on task intent.

Current tools:

- calculator
- note_writer

Example:

```bash
python main.py "帮我计算 123 * 456 并保存结果"
```

Tool Chain:

```text
calculator
↓
note_writer
```

---

## Agent Loop

The core autonomous workflow:

```text
Goal
 ↓
Plan
 ↓
Execute
 ↓
Observe
 ↓
Summarize
```

Example Output:

```text
Agent Loop Completed

Steps:
1

Final Summary:
123 × 456 = 56088
Result saved successfully.
```

---

# Architecture

```text
User Input
    ↓
Agent Core
    ↓
Agent Loop
    ↓
Planner
    ↓
Executor
    ↓
Tool Selector
    ↓
Tool Chain
    ↓
Tool Registry
    ↓
Tools
```

Memory System:

```text
Memory.json
    ↓
Long-Term Memory

History.json
    ↓
Short-Term Memory
```

---

# Project Structure

```text
mini-agent-core/
│
├── agent/
│   ├── core.py
│   ├── memory.py
│   ├── history.py
│   ├── planner.py
│   ├── executor.py
│   ├── loop.py
│   ├── router.py
│   ├── registry.py
│   ├── tool_selector.py
│   ├── toolchain.py
│   └── tools.py
│
├── notes/
├── main.py
├── requirements.txt
└── README.md
```

---

# Installation

Clone repository:

```bash
git clone https://github.com/YiYun0305/mini-agent-core.git

cd mini-agent-core
```

Create virtual environment:

```bash
python3.12 -m venv .venv

source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Ollama:

```bash
brew install --cask ollama
```

Pull model:

```bash
ollama pull qwen3:8b
```

Run:

```bash
python main.py "你好"
```

---

# Roadmap

## Completed

- v0.1 Agent Core
- v0.2 Tool Registry
- v0.3 Tool Decorator
- v0.4 Structured Memory
- v0.5 Memory Context Injection
- v0.6 Conversation History
- v0.7 Planner
- v0.8 Executor
- v0.9 Dynamic Tool Chain
- v1.0 Agent Loop

## Future

- Multi-Agent Support
- MCP Integration
- Web Search Tool
- File Reader Tool
- Agent Workspace
- Long-Term Knowledge Base

---

# License

MIT License