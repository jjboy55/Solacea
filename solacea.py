import streamlit as st

import asyncio
from controller.msftgraphrag import RGlobalSearch


st.title("🏥 Colon Cancer Decision Support System")
with st.sidebar:
    st.image("videos/Blue Modern Project Presentation.png")
    st.markdown("## Here are some questions to ask me 🩺 ##")

    questions = [
        "A Stage III patient is ctDNA positive post-surgery. What does the research suggest regarding adjuvant chemotherapy?"
        "How does **ctDNA positivity** after surgery affect treatment decisions in **Stage III** cancer patients?",
        "What is the significance of being **ctDNA positive** for a **Stage III** cancer patient post-surgery?",
        "What role does **ctDNA** play in determining the need for **adjuvant chemotherapy** in cancer treatment?",
        "What are the implications of **ctDNA detection** after surgery in **Stage III** cancer?",
        "How does **ctDNA positivity** influence the likelihood of recommending **adjuvant chemotherapy** for **Stage III** patients?",
    ]

    for question in questions:
        st.write(f"- {question}")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if "model" not in st.session_state:
    st.session_state["model"] = "gpt-4o-mini"

if "responder" not in st.session_state:
    st.session_state["responder"] = RGlobalSearch()
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    # Renders the chat message of either user or ai in container
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Hey Doc! Got a question?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        global_search = RGlobalSearch()
        response = asyncio.run(st.session_state["responder"].get_response(prompt))
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
