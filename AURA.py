import streamlit as st
import time
import google.generativeai as genai

genai.configure(api_key="AIzaSyC3DEsWDFmTp-GmXpG2zo7GGscER6uid34")

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro-002",
  generation_config=generation_config,
  system_instruction="\nYour AURA system was created by  Muthu Nilavan, an 8th-grade professional Python and machine learning programmer, with the mission to make AI accessible to all. AURA stands for Advanced Unified Response Algorithm and was built with the motto \"AI for All.\" As a user-friendly, conversational AI, AURA is designed to respond in a friendly, easygoing manner, ensuring that interacting with it feels natural and helpful. Whether answering questions or performing tasks, AURA is crafted to make AI both useful and approachable, adapting to users’ needs with simplicity and efficiency.",
)

chat_session = model.start_chat(
  history=[
  ]
)
def Response(response):
  for word in response.split():
    yield word + " "
    time.sleep(0.05)
st.title("Aura")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Say Something...."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        response = st.write_stream(Response(chat_session.send_message(prompt).text))

        

    st.session_state.messages.append({"role": "assistant", "content": response})