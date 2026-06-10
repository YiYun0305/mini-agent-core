# Mini Agent Core

A lightweight AI Agent framework built from scratch using Python and Ollama.

## Features

- Local LLM powered by Qwen3 via Ollama
- Calculator Tool
- Note Writer Tool
- Persistent Memory
- Task Routing
- CLI Interface

## Project Structure

mini-agent-core/
├── agent/
│   ├── core.py
│   ├── memory.py
│   └── tools.py
├── notes/
├── main.py
├── requirements.txt
└── README.md


## Installation

bash git clone https://github.com/YOUR_USERNAME/mini-agent-core.git  cd mini-agent-core  python3.12 -m venv .venv  source .venv/bin/activate  pip install -r requirements.txt 

## Usage

### Ask the Agent

bash python main.py "What is an AI Agent?" 

### Calculator Tool

bash python main.py "123 * 456" 

### Save Note

bash python main.py "写一份3天AI Agent学习计划并保存" 

### Memory

bash python main.py "记住：我的项目叫 Mini Agent Core"  python main.py "我的项目叫什么" 

## Current Features

- Local Qwen3 Integration
- Calculator Tool
- Note Writer Tool
- Persistent Memory
- CLI Interface

## Roadmap

- [x] Local LLM
- [x] Calculator Tool
- [x] Note Writer Tool
- [x] Persistent Memory
- [ ] Tool Registry
- [ ] Multi Tool Router
- [ ] Conversation Memory
- [ ] MCP Support

## License

MIT