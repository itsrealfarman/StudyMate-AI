import streamlit as st

from utils.pdf_reader import extract_text
from utils.text_splitter import split_text
from utils.vector_store import create_vector_store
from utils.search import search_chunks
from utils.qa_chain import generate_answer


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="🎓",
    layout="centered"
)

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "current_pdf" not in st.session_state:
    st.session_state.current_pdf = None


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.title("🎓 StudyMate AI")
    st.caption("AI-powered PDF Study Assistant")

    st.divider()

    st.markdown("### 🚀 Tech Stack")

    st.markdown("""
- 🦜 LangChain
- 🗄️ FAISS
- 🤗 HuggingFace Embeddings
- 🤖 GPT-4o-mini
- 🎈 Streamlit
""")

    st.divider()

    st.markdown("### 📖 How to Use")

    st.markdown("""
1. Upload a PDF
2. Wait for processing
3. Ask questions
4. View AI answers
5. Check sources
""")

    st.divider()

    if st.button("🧹 Clear Chat", use_container_width=True):

        st.session_state.messages = []
        st.session_state.vector_store = None
        st.session_state.current_pdf = None

        st.rerun()

    st.divider()

    st.caption("Made with ❤️ by Farman Ali")


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🎓 StudyMate AI")

st.caption(
    "AI-powered PDF Chatbot using Retrieval-Augmented Generation (RAG)"
)


# --------------------------------------------------
# Upload PDF
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

if uploaded_file is None:

    st.info("""
👋 **Welcome to StudyMate AI!**

### 🚀 Features

- 📄 Upload any PDF
- 💬 Ask questions
- 🧠 AI-generated answers
- 📚 Source references

### 💡 Example Questions

- Summarize this PDF
- What are the key topics?
- Explain the conclusion.
- Give me important points.
""")

    st.success(
        "Supports lecture notes, books, research papers and PDFs."
    )

    st.stop()


# --------------------------------------------------
# Show Selected PDF
# --------------------------------------------------

st.info(f"📄 Loaded Document: **{uploaded_file.name}**")


# --------------------------------------------------
# Process PDF
# --------------------------------------------------

if (
    st.session_state.vector_store is None
    or st.session_state.current_pdf != uploaded_file.name
):

    with st.spinner("📄 Processing PDF..."):

        text = extract_text(uploaded_file)

        chunks = split_text(text)

        st.session_state.vector_store = create_vector_store(chunks)

        st.session_state.current_pdf = uploaded_file.name

        st.session_state.messages = []

    st.success("✅ Document processed successfully!")

    st.info("📚 Your PDF is ready. Ask anything!")


# --------------------------------------------------
# Welcome Message
# --------------------------------------------------

if len(st.session_state.messages) == 0:

    st.info("""
💡 **Try asking:**

• Summarize this PDF

• What are the key topics?

• Explain the conclusion.

• Give important points.
""")


# --------------------------------------------------
# Chat History
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])


# --------------------------------------------------
# Chat Input
# --------------------------------------------------

question = st.chat_input(
    "Ask a question about your PDF..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.write(question)

    with st.chat_message("assistant"):

        with st.spinner("🤖 Thinking..."):

            results = search_chunks(
                st.session_state.vector_store,
                question
            )

            if not results:

                st.warning(
                    "No relevant information found in the document."
                )

                st.stop()

            try:

                answer = generate_answer(
                    question,
                    results,
                    st.session_state.messages
                )

            except Exception:

                st.error(
                    "❌ Failed to contact the AI model. Please try again."
                )

                st.stop()

        st.write(answer)

        with st.expander("📚 View Sources"):

            for index, doc in enumerate(results):

                st.markdown(
                    f"**Source {index + 1}**"
                )

                st.markdown(
                    "> " + doc.page_content[:600]
                )

                st.divider()

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "© 2026 Farman Ali • Powered by LangChain + FAISS + OpenAI"
)