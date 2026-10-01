from langchain_ollama import ChatOllama 


LLM = ChatOllama(
    model="qwen3:4b",
    temperature=0
)

response = LLM.invoke(
    "Explain what SQL is in one simple sentence."
)

print(response.content) 