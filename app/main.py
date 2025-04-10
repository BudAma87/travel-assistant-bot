from app.graph_flow import build_graph
import app.langsmith_config

if __name__ == "__main__":
    app = build_graph()
    result = app.invoke({
        "destination": "Paris",
        "days": 3,
        "budget": 1000
    })
    print("Trip Plan:\n", result.get("itinerary"))

