import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

openai_llm = ChatOpenAI(model="gpt-4o-mini", api_key = OPENAI_API_KEY)
groq_llm = ChatGroq(model="llama-3.3-70b-versatile", api_key = GROQ_API_KEY)

search_tool = TavilySearchResults(max_results=2)

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

agent = create_react_agent(
    model = groq_llm,
    tools=[search_tool],
)

query = "What is the capital of France?"
state = {"messages": query}
response = agent.invoke(state)
messages = response.get("messages")
ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
print(ai_messages[-1])