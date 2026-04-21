from utils.embeddings import get_embeddings

def retrieve(query, vectorstore):
    query = "return policy warranty " + query  # ✅ keyword boost
    query_embedding = get_embeddings([query])[0]
    results = vectorstore.search(query_embedding)
    return results

