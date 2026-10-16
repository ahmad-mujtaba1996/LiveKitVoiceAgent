import sys

from langchain_agent import lauki_agent

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    query = "What is the 5g coverage in Bengaluru?"
    result = lauki_agent.invoke({"messages": [{"role": "user", "content": query}]})
    print("Agent Response:", result["messages"][-1].content)
