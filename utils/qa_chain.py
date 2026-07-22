from utils.llm import get_llm


def generate_answer(question, docs):

    llm = get_llm()

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are StudyMate AI, an assistant that answers questions from provided documents.

Use only the given context to answer the question.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content