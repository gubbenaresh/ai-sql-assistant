from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="qwen3:4b",
    temperature=0,
)


response = llm.invoke(
    "Explain what SQL is in one simple sentence."
)


print(response.content)