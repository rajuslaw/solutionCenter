from langgraph.graph import StateGraph, END
from langchain.schema.messages import HumanMessage
from typing import TypedDict, List, Optional
from tachyon_client import query_tachyon_llm_structured
from tools import get_invoice_data, get_travel_details


class AgentState(TypedDict):
    messages: List
    intent: Optional[str]
    entities: dict
    tool_result: Optional[str]

def llm_node(state: AgentState) -> AgentState:
    query = state["messages"][-1].content
    structured_result = query_tachyon_llm_structured(query)
    return {
        **state,
        "intent": structured_result.get("intent", "unknown"),
        "entities": structured_result.get("entities", {})
    }

def tool_node(state: AgentState) -> AgentState:
    intent = state["intent"]
    entities = state["entities"]
    
    if intent == "get_invoice_data":
        result = get_invoice_data(entities.get("invoice_id"))
    elif intent == "get_travel_details":
        result = get_travel_details(entities.get("date"))
    else:
        result = "Sorry, I couldn't understand your request."
    
    return {
        **state,
        "tool_result": result
    }

graph = StateGraph(AgentState)
graph.add_node("llm", llm_node)
graph.add_node("tool", tool_node)
graph.set_entry_point("llm")
graph.add_edge("llm", "tool")
graph.add_edge("tool", END)

app = graph.compile()

# Run example
query = "Please send invoice INV-7890"
response = app.invoke({"messages": [HumanMessage(content=query)]})

print("🔍 Intent:", response["intent"])
print("🧠 Entities:", response["entities"])
print("✅ Tool Output:", response["tool_result"])
