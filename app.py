import streamlit as st
import time
from src.helper import get_pdf_text, get_chunks, get_vector_store, get_conversational_chain

def user_input(user_question):
    response = st.session_state.conversational({"question": user_question})
    st.session_state.chatHistory = response['chat_history']
    for i, message in enumerate(st.session_state.chatHistory):
        if i % 2 == 0:
            st.write(f"**User:** {message.content}")    
        else:
            st.write(f"**Reply:** {message.content}")


def main():
    st.set_page_config( page_title="Info Retrieval Gen AI")
    st.header("Information Retrieval with Generative AI")
    
    user_question = st.text_input("Ask a question about the uploaded documents:", placeholder="Type your question here...")
    
    if 'conversational' not in st.session_state:
        st.session_state.conversational = None
    if 'chatHistory' not in st.session_state:
        st.session_state.chatHistory = None
    if user_question:
        user_input(user_question)

    


    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload PDF Documents and click submit",accept_multiple_files=True,label_visibility="collapsed")
        if st.button("Submit", type="primary", use_container_width=True):
            with st.spinner("Processing..."):
                time.sleep(2)
                raw_text = get_pdf_text(pdf_docs)
                chunks = get_chunks(raw_text)
                vector_store = get_vector_store(chunks)
                st.session_state.conversational  = get_conversational_chain(vector_store)  

                st.success("Files uploaded successfully!")
                

if __name__ == "__main__":
    main()