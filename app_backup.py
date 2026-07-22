import streamlit as st

from utils.pdf_reader import extract_text
from utils.text_splitter import split_text
from utils.vector_store import create_vector_store
from utils.search import search_chunks
from utils.qa_chain import generate_answer
st.set_page_config(
    page_title="StudyMate AI",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 StudyMate AI")
st.write("Your AI-Powered Study Assistant")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:

    text = extract_text(uploaded_file)

    chunks = split_text(text)

    vector_store = create_vector_store(chunks)

    st.success("PDF Loaded Successfully!")
    st.success("Vector Database Created!")

    st.subheader("Extracted Text")
    st.write(text[:2000])

    st.subheader("Chunks")
    st.write(f"Total Chunks: {len(chunks)}")
    st.write(chunks[0])

    question = st.text_input("Ask a question about your PDF")

    if question:

        results = search_chunks(vector_store, question)

        answer = generate_answer(question, results)

        st.subheader("🤖 StudyMate AI Answer")

        st.write(answer)

        st.subheader("📚 Sources")

        for doc in results:
            st.write(doc.page_content)
            st.write("---")