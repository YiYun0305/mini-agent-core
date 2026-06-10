# Mini Agent Core

A lightweight local-first AI Agent Framework built with Python, Ollama, and Qwen.

Mini Agent Core demonstrates how modern autonomous AI agents are built from the ground up.

Core capabilities include:

- Local LLM Integration
- Structured Memory
- Conversation History
- Planning
- Execution
- Dynamic Tool Selection
- Tool Chains
- Agent Loop
- Web Search
- Search Quality Filtering
- Debug Tracing

The project runs entirely locally using Ollama and Qwen models.

No OpenAI API required.

---

# Features

## Local LLM

Powered by:

- Ollama
- Qwen3:8B

Example:

```bash
python main.py "你好"
```

---

## Structured Memory

Persistent JSON-based memory.

Example:

```json
{
  "project": "Mini Agent Core",
  "name": "Wang",
  "city": "Boston"
}
```

Save memory:

```bash
python main.py "记住项目名：Mini Agent Core"
python main.py "记住姓名：Wang"
```

Recall memory:

```bash
python main.py "我的项目叫什么"
python main.py "我叫什么"
```

---

## Conversation History

Short-term memory stored in:

```text
history.json
```

Supports contextual follow-up conversations.

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

Example output:

```text
1. Learn AI Agent fundamentals
2. Study memory systems
3. Build simple agents
4. Explore planning workflows
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
- web_search

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

## Web Search

The agent can retrieve real-world information using web search.

Current capabilities:

- Query Rewriting
- Search Result Filtering
- Source Quality Scoring
- Time Context Awareness
- Search Result Summarization

Examples:

```bash
python main.py "OpenAI最近有什么新闻"

python main.py "今天英伟达股价是多少"

python main.py "波士顿大学地址在哪里"

python main.py "美国签证为什么check很久"
```

---

## Search Quality

Introduced in v1.6.

Features:

- Search Result Filtering
- Trusted Source Scoring
- Outdated Content Detection
- Higher Quality Context for LLM Summaries

Examples of preferred sources:

- Reuters
- BBC
- AP News
- Government Websites (.gov)
- Universities (.edu)
- Official Company Websites

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

Status:
success

Steps:
1

Final Summary:
123 × 456 = 56088

Result saved to:
notes/agent_output_1.md
```

---

## Debug Mode

View the complete execution trace.

Example:

```bash
python main.py --debug "OpenAI最近有什么新闻"
```

Shows:

- Task Routing
- Tool Selection
- Query Rewriting
- Search Results
- Tool Execution
- Final Output

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
Tools
```

Tool Workflow:

```text
User Query
    ↓
Query Rewriter
    ↓
Web Search
    ↓
Search Filter
    ↓
LLM Summary
```

Memory System:

```text
memory.json
    ↓
Long-Term Memory

history.json
    ↓
Short-Term Memory
```

---

# Project Structure

```text
mini-agent-core/
│
├── agent/
│
├── core.py
├── planner.py
├── executor.py
├── loop.py
├── memory.py
├── history.py
├── registry.py
├── router.py
├── tool_selector.py
├── toolchain.py
├── tools.py
│
├── query_rewriter.py
├── search_filter.py
├── time_context.py
├── debug_trace.py
│
├── notes/
│
├── memory.json
├── history.json
│
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

# Version History

## v0.1

- Agent Core

## v0.2

- Tool Registry

## v0.3

- Tool Decorator

## v0.4

- Structured Memory

## v0.5

- Memory Context Injection

## v0.6

- Conversation History

## v0.7

- Planner

## v0.8

- Executor

## v0.9

- Dynamic Tool Chain

## v1.0

- Agent Loop

## v1.2

- Web Search

## v1.3

- LLM Query Rewriter

## v1.4

- Debug Trace

## v1.4.2

- Save Result Awareness
- Auto Output Files

## v1.5

- Single Summary Mode
- Loop Result Fallback

## v1.6

- Search Quality
- Search Result Filter
- Source Quality Scoring
- Outdated Content Filtering

---

# Roadmap

## v1.6.1

Search Intent Detection

- Determine when web search is required
- Reduce hallucinations
- Improve factual accuracy

## v1.6.2

Source Ranking

- Trust score system
- Official source prioritization

## v1.6.3

Confidence Scoring

- Answer confidence estimation
- Better uncertainty handling

## v2.0

- Multi-Agent Support
- Reflection Loop
- Re-Planning
- MCP Integration
- Long-Term Knowledge Base

---

# License

MIT License
