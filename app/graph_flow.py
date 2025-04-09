from typing import TypedDict
from langgraph.graph import StateGraph
from app.llm_logic import get_llm_chain

class TravelState(TypedDict):
    destination: str
    days: int
    budget: int
    itinerary: str

def extract_info(state: TravelState) -> TravelState:
    return {
        "destination": state.get("destination", "Paris"),
        "days": state.get("days", 3),
        "budget": state.get("budget", 1000),
        "itinerary": ""
    }

def check_budget(state: TravelState) -> dict:
    if state["budget"] < 500:
        return {"status": "too_low"}
    return {"status": "ok"}

def generate_itinerary(state: TravelState) -> TravelState:
    chain = get_llm_chain()
    result = chain.invoke({
        "destination": state["destination"],
        "days": state["days"],
        "budget": state["budget"]
    })
    state["itinerary"] = result
    return state

def build_graph():
    graph = StateGraph(state_schema=TravelState)
    graph.add_node("extract_info", extract_info)
    graph.add_node("check_budget", check_budget)
    graph.add_node("generate_itinerary", generate_itinerary)

    graph.set_entry_point("extract_info")
    graph.add_edge("extract_info", "check_budget")
    graph.add_conditional_edges("check_budget", {
        "ok": "generate_itinerary",
        "too_low": "extract_info"
    })

    return graph.compile()
