from sentence_transformers import SentenceTransformer

# Load model once (fast after first time)
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embeddings(texts):
    return model.encode(texts)
