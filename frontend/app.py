import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(
    page_title="TailorTalk Drive Assistant",
    page_icon="📁",
    layout="centered"
)

st.title("📁 TailorTalk Drive Assistant")
st.caption("Search Google Drive files using natural language")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


user_input = st.chat_input("Ask something like: find all pdf reports")

if user_input:
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        response = requests.post(
            BACKEND_URL,
            json={"message": user_input}
        )

        bot_response = response.json()["response"]

    except Exception:
        bot_response = "Backend connection failed. Make sure FastAPI server is running."

    st.session_state.chat_history.append({
        "role": "assistant",
        "content": bot_response
    })

    with st.chat_message("assistant"):
        st.markdown(bot_response)
