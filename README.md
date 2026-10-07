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

                 USER
                  │
                  │ Upload CSV / Excel
                  ↓
              Streamlit
                  │
                  ↓
             Load Dataset
                  │
                  ↓
                DuckDB
                  │
                  │
User: "What are the
top 5 products by sales?"
                  │
                  ↓
              LangChain
                  │
                  ↓
           Ollama + Qwen3:4B
                  │
                  │ Generate SQL
                  ↓
          SELECT product,
                 SUM(sales)
          FROM data
          GROUP BY product
          ORDER BY SUM(sales) DESC
          LIMIT 5;
                  │
                  ↓
               DuckDB
                  │
                  │ Execute SQL
                  ↓
                Result
                  │
                  ↓
           Qwen3:4B / LangChain
                  │
                  ↓
       "The top 5 products are..."
                  │
                  ↓
              Streamlit
                  │
                  ↓
                 USER


### Day 2

- Added CSV file upload
- Added Excel file upload
- Added Pandas data processing
- Added dataset preview
- Added dataset information
- Added schema detection
- Added DuckDB integration
- Added persistent local DuckDB database
- Added SQL execution
- Added database tests                 