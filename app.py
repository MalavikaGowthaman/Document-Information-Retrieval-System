import streamlit as st
import PyPDF2
from src.helper import get_pdf_text, get_docx_text, get_txt_text, get_text_chunks, get_conversational_chain, get_vector_store
from io import BytesIO

st.set_page_config(page_title="Information Retrieval", page_icon="🔍")
st.header("📚 Information Retrieval System 📚")


def user_input(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chatHistory = response['chat_history']
    for i, message in enumerate(st.session_state.chatHistory):
        if i%2 == 0:
            st.write("User: ", message.content)
        else:
            st.write("Reply: ", message.content)

def process_files(uploaded_files):
    text = ""
    for uploaded_file in uploaded_files:
        file_bytes = uploaded_file.read()
        file_type = uploaded_file.type
        file_io = BytesIO(file_bytes)  # Convert bytes to a file-like object
        
        if file_type == "application/pdf":
            text += get_pdf_text(file_io)
        elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            text += get_docx_text(file_io)
        elif file_type == "text/plain":
            text += get_txt_text(file_io)
    return text


def main():
 user_question = st.text_input("Ask a Question from the Files")
 if "conversation" not in st.session_state:
    st.session_state.conversation = None
 if "chatHistory" not in st.session_state:
    st.session_state.chatHistory = None
 
 if user_question:
    user_input(user_question)

#  with st.sidebar:
st.title("Menu:")
# pdf_docs = st.file_uploader("Upload Your Files and Click on the Submit & Process Button", accept_multiple_files= True)
uploaded_files = st.file_uploader("Upload Your Files (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"], accept_multiple_files=True)
if st.button("Submit & Process"):
 with st.spinner("Processing..."):
    raw_text = process_files(uploaded_files)
    if raw_text:
       text_chunks = get_text_chunks(raw_text)
       vector_store = get_vector_store(text_chunks)
       st.session_state.conversation = get_conversational_chain(vector_store)
       st.success("Processing Complete")
    else:
       st.error("Uploaded files are empty or not supported.")


if __name__ =='__main__':
 main()

