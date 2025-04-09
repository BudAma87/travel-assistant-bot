import streamlit as st
from app.graph_flow import build_graph
import app.langsmith_config  # for LangSmith tracing

st.set_page_config(page_title="🌍 Travel Assistant", layout="centered")

st.title("🌍 Travel Assistant Bot")
st.markdown("Plan your next trip with the power of AI 🧠")

destination = st.text_input("Where do you want to go?", "Paris")
days = st.slider("Trip Duration (in days)", 1, 14, 3)
budget = st.number_input("What's your budget (USD)?", min_value=100, max_value=10000, value=1000)

if st.button("Generate Itinerary"):
    with st.spinner("Planning your trip..."):
        app = build_graph()
        result = app.invoke({
            "destination": destination,
            "days": days,
            "budget": budget
        })
        itinerary = result.get("itinerary", "Sorry, couldn't generate a plan.")
        st.success("Here's your personalized itinerary:")
        st.markdown(f"```markdown\n{itinerary}\n```")
