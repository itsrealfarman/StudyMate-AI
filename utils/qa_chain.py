from utils.llm import get_llm


def generate_answer(question, docs):

    llm = get_llm()

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are StudyMate AI, an intelligent PDF question answering assistant.

Rules:
1. Answer only using the provided context.
2. Do not use outside knowledge.
3. If the answer is not available in the context, say:
"I could not find this information in the document."
4. Give a clear and concise explanation.

Context:
----------------
{context}
----------------

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content