from utils.llm import get_llm


def generate_answer(question, docs, chat_history=None):

    llm = get_llm()


    # PDF context
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )


    # Chat history
    history = ""

    if chat_history:

        for message in chat_history[-6:]:
            history += (
                f"{message['role']}: "
                f"{message['content']}\n"
            )


    prompt = f"""
You are StudyMate AI, an assistant that answers questions from documents.

Rules:
1. Answer only using the provided document context.
2. Use previous conversation only to understand references like "it", "this", "that".
3. Do not add information that is not present in the document.
4. If the answer is not available, say:
"I could not find this information in the document."

Previous Conversation:
----------------
{history}
----------------

Document Context:
----------------
{context}
----------------

Current Question:
{question}

Answer:
"""


    response = llm.invoke(prompt)

    return response.content