import streamlit as st

from utils.pdf_reader import extract_text
from utils.text_splitter import split_text
from utils.vector_store import create_vector_store
from utils.search import search_chunks
from utils.qa_chain import generate_answer


st.set_page_config(
    page_title="StudyMate AI",
    page_icon="🎓",
    layout="centered"
)


# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []


st.title("🎓 StudyMate AI")
st.write("Your AI-Powered PDF Study Assistant")


# Upload PDF
uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)


if uploaded_file:

    # Process PDF only once
    if "vector_store" not in st.session_state:

        with st.spinner("Processing document..."):

            text = extract_text(uploaded_file)

            chunks = split_text(text)

            vector_store = create_vector_store(chunks)

            st.session_state.vector_store = vector_store


        st.success("✅ Document processed successfully!")


    # Show previous chat
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.write(message["content"])


    # Chat input
    question = st.chat_input(
        "Ask a question about your PDF"
    )


    if question:

        # User message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )


        with st.chat_message("user"):
            st.write(question)


        # Generate answer
        with st.chat_message("assistant"):

            with st.spinner("Thinking... 🤖"):

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


        # Save AI response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )


        # Sources
        with st.expander("📚 View Sources"):

            for doc in results:
                st.write(doc.page_content)
                st.divider()