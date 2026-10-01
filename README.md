# 🤖 AI SQL Assistant

An AI-powered application that allows users to upload CSV or Excel files
and ask questions about their data using natural language.

## Project Goal

The user should not need to know SQL.

The application will:

1. Accept a CSV or Excel file
2. Load the data
3. Store the data in DuckDB
4. Understand the user's natural-language question
5. Generate SQL using a local LLM
6. Execute the SQL
7. Return the answer in natural language

## Current Progress

### Day 1

- Project structure created
- Python virtual environment created
- Streamlit installed
- LangChain installed
- DuckDB installed
- Ollama installed
- Local Qwen3 4B model configured
- Basic Streamlit application created
- LangChain + Ollama connection tested

## Tech Stack

- Python
- Streamlit
- Pandas
- DuckDB
- LangChain
- Ollama
- Qwen3
- Git
- GitHub

## Architecture

```text
User
 ↓
Streamlit
 ↓
LangChain
 ↓
Local LLM
 ↓
SQL
 ↓
DuckDB
 ↓
Result
 ↓
Natural Language Answer