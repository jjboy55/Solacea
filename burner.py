import streamlit as st
import sys
import asyncio
from controller.msftgraphrag import RGlobalSearch

video_path = "videos/msftgraphrag3d.mov"

st.video(video_path)
st.caption("MsftGraphRag Visualisation using noworneverev")
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
