# Mini Agent Core

A lightweight AI Agent framework built from scratch using Python and Ollama.

Mini Agent Core is a local-first AI Agent project that demonstrates the core building blocks of modern AI agents:

- Local LLM integration (Qwen3 via Ollama)
- Tool Calling
- Persistent Memory
- Task Routing
- File Writing
- CLI Interface

This project is designed for learning and experimentation while gradually evolving into a more complete Agent Framework.

---

# Features

## Local LLM

Run Qwen3 completely locally using Ollama.

## Calculator Tool

Detect and execute mathematical expressions.

Example:

bash python main.py "123 * 456" 

Output:

text 56088 

---

## Note Writer Tool

Generate content and save it to a local file.

Example:

bash python main.py "写一份3天AI Agent学习计划并保存" 

Generated file:

text notes/agent_note.md 

---

## Persistent Memory

Store and recall information across sessions.

Save Memory:

bash python main.py "记住：我的项目叫 Mini Agent Core" 

Recall Memory:

bash python main.py "我的项目叫什么" 

Output:

text 记住：我的项目叫 Mini Agent Core 

---

## Project Structure

mini-agent-core/
├── agent/
│   ├── __init__.py
│   ├── core.py
│   ├── memory.py
│   ├── prompts.py
│   └── tools.py
│
├── main.py
├── requirements.txt
├── .env.example
└── README.md

---

# Installation

## 1. Clone Repository

bash git clone https://github.com/YiYun0305/mini-agent-core.git  cd mini-agent-core 

## 2. Create Virtual Environment

bash python3.12 -m venv .venv  source .venv/bin/activate 

## 3. Install Dependencies

bash pip install -r requirements.txt 

## 4. Install Ollama

Download and install Ollama:

https://ollama.com/download

## 5. Download Qwen3 Model

bash ollama pull qwen3:8b 

## 6. Verify Ollama

bash ollama run qwen3:8b 

If the model responds correctly, Ollama is ready.

---

# Usage

## Ask the Agent

bash python main.py "介绍一下AI Agent" 

---

## Calculator

bash python main.py "123 * 456" 

---

## Save Note

bash python main.py "写一份AI Agent学习计划并保存" 

---

## Memory

bash python main.py "记住：我的项目叫 Mini Agent Core"  python main.py "我的项目叫什么" 

---

# Current Architecture

text User Input       │       ▼ Task Router       │  ┌────┼────┐  ▼    ▼    ▼ LLM  Tool Memory       │       ▼ Response 

---

# Roadmap

## v0.1.0

- [x] Local Qwen3 Integration
- [x] Calculator Tool
- [x] Note Writer Tool
- [x] Persistent Memory
- [x] CLI Interface

## v0.2.0

- [ ] Tool Registry
- [ ] Tool Executor
- [ ] Multi Tool Routing

## v0.3.0

- [ ] File Tool
- [ ] Web Tool
- [ ] Conversation Memory

## v1.0.0

- [ ] MCP Integration
- [ ] Plugin Architecture
- [ ] Multi-Agent Support

---

# Tech Stack

- Python 3.12
- Ollama
- Qwen3 8B
- Typer
- Rich

---

# License

MIT License