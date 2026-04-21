from utils.loader import load_pdf
from utils.splitter import split_documents
from utils.embeddings import get_embeddings
from utils.vectordb import VectorStore
from utils.retriever import retrieve
from utils.rag_chain import generate_answer

def process_pdf(file_path):
    docs = load_pdf(file_path)
    chunks = split_documents(docs)

    texts = [doc.page_content for doc in chunks]

    embeddings = get_embeddings(texts)

    vectorstore = VectorStore(len(embeddings[0]))
    vectorstore.add(embeddings, texts)

    return vectorstore

def ask_question(vectorstore, query, chat_history):
    retrieved_docs = retrieve(query, vectorstore)

    context = "\n\n".join([f"Chunk {i+1}: {doc}" for i, doc in enumerate(retrieved_docs)])

    answer = generate_answer(query, context, chat_history)

    return answer, retrieved_docs

