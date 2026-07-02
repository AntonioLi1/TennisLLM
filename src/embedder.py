from sentence_transformers import SentenceTransformer 

model = SentenceTransformer('all-MiniLM-L6-v2')

def embedder(text_chunks):

    texts = [chunk['text'] for chunk in text_chunks]
    embeddings = model.encode(texts)

    for i, chunk in enumerate(text_chunks):
        chunk['embedding'] = embeddings[i]

    return text_chunks


