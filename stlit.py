import streamlit as st
from google import genai as M
robo = M.Client(api_key=st.secrets["MY_API"]
mychat = robo.chats.create(model="gemini-flash-lite-latest")
##st.title("My AI")
##question = st.text_input("Ask Question")
##if st.button("Send"):
##    response = mychat.send_message(question)
##    st.write(response.text)

st.markdown(
  """
  <h1 style='text-align: center;'> Python AI Assistant</h1>
  <p style='text-align: center; font-size:18px;'>
    Ask any GK question.
  </p>
  """,
  unsafe_allow_html=True,
)

response_placeholder = st.empty()
question = st.text_input("", placeholder="Entry your Question")
col1, col2, col3 = st.columns((4, 1, 4))

with col2:
    send = st.button("Send")


if send:
    response = mychat.send_message(question)
    response_placeholder.write(response.text)


  


 
