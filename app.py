from utils.pdf_reader import extract_text
from utils.text_splitter import split_text
import streamlit as st

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

    st.success("PDF Loaded Successfully!")

    st.subheader("Extracted Text")
    st.write(text[:2000])

    st.subheader("Chunks")
    st.write(f"Total Chunks: {len(chunks)}")
    st.write(chunks[0])