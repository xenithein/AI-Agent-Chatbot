import streamlit as st

st.set_page_config(page_title="AI Agent Chatbot", page_icon=":robot_face:", layout="centered")
st.title("AI Agent Chatbot")
st.write("Interact with various AI models to get responses based on your queries.")

system_prompt = st.text_area("Define Your AI Agent", placeholder="Enter system prompt here...", height=70)

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "llama-3.3-70b-8192", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("Select Model Provider", ["Groq", "OpenAI"])

if provider == "Groq":
    selected_model = st.selectbox("Select Model", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select Model", MODEL_NAMES_OPENAI)

allow_web_search = st.checkbox("Allow Web Search")

user_query = st.text_area("Enter Your Query", placeholder="Ask Anything...", height=150)

API_URL = "http://127.0.0.1:8000/chat"

if st.button("Ask Agent"):
    if user_query.strip():
        import requests
        payload={
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"**{response_data}**")
