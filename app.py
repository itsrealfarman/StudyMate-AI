import streamlit as st

from utils.pdf_reader import extract_text
from utils.text_splitter import split_text
from utils.vector_store import create_vector_store
from utils.search import search_chunks
from utils.qa_chain import generate_answer


# Page Configuration
st.set_page_config(
    page_title="StudyMate AI",
    page_icon="🎓",
    layout="centered"
)


# Session Memory
if "messages" not in st.session_state:
    st.session_state.messages = []

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None



# Sidebar
with st.sidebar:

    st.title("🎓 StudyMate AI")

    st.write(
        """
        AI-powered PDF Study Assistant.

        Built with:

        🔹 LangChain
        🔹 FAISS Vector Database
        🔹 HuggingFace Embeddings
        🔹 OpenAI GPT

        Upload a PDF and chat with your document.
        """
    )

    st.divider()


    if st.button("🧹 Clear Chat"):

        st.session_state.messages = []
        st.session_state.vector_store = None

        st.rerun()



# Main Header
st.title("🎓 StudyMate AI")

st.caption(
    "Chat with your documents using RAG + Generative AI"
)



# PDF Upload
uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)



if uploaded_file:


    st.info(
        f"📄 Loaded Document: {uploaded_file.name}"
    )


    # Create Vector Database
    if st.session_state.vector_store is None:


        with st.spinner(
            "Processing document... 🤖"
        ):

            text = extract_text(uploaded_file)

            chunks = split_text(text)

            vector_store = create_vector_store(chunks)

            st.session_state.vector_store = vector_store


        st.success(
            "✅ Document processed successfully!"
        )

        st.info(
            "📚 Your PDF is ready. Ask anything!"
        )



    # Chat History

    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):

            st.write(
                message["content"]
            )



    # User Question

    question = st.chat_input(
        "Ask a question about your PDF..."
    )



    if question:


        # Save user message

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )


        with st.chat_message("user"):

            st.write(question)



        # AI Response

        with st.chat_message("assistant"):


            with st.spinner(
                "Thinking... 🧠"
            ):


                results = search_chunks(
                    st.session_state.vector_store,
                    question
                )


                answer = generate_answer(
                    question,
                    results,
                    st.session_state.messages
                )


            st.write(answer)



        # Save AI message

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )



        # Sources

        with st.expander(
            "📚 View Sources"
        ):


            for index, doc in enumerate(results):


                st.markdown(
                    f"### Source {index + 1}"
                )


                st.write(
                    doc.page_content[:400] + "..."
                )


                st.divider()