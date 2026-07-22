def search_chunks(vector_store, question):

    docs = vector_store.similarity_search(
        question,
        k=3
    )

    return docs