import youtube_assistant as yt 
import streamlit as st
import textwrap

st.title("Yotube assistant 🚀")

with st.sidebar:
    with st.form(key="my_form"):
        url = st.text_area(label="Enter the youtube video url ", max_chars=50)                  # taking video url
        query = st.text_area(label="Ask me question related to video",max_chars=100)             # asking question related to video
        openai_api_key = st.text_input(label="Openai api key", type="password")                 # getting api key from user
        submit_button = st.form_submit_button(label="submit")                                   # sumbitting the form 


if query and url:
            if not openai_api_key:
                   st.info("Please enter your key")
                   st.stop()
            else:
                db = yt.yotube_url_to_vector_db(url)
                result = yt.get_response_from_query(db,query)
                st.subheader("Answer : ")
                st.write(textwrap.fill(result, width=80))
