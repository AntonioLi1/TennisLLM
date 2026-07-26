import os
import numpy as np
import json
from embedder import model


    
# #def load():
# embeddings = np.load('store/embeddings.npz')
# print("Keys in npz file:", embeddings.files)

# data = embeddings['embeddings']
# print("Embeddings shape:", data.shape)
# #print("first embeddings entry", data[0])

# with open('store/metadata.json', 'r') as f:
#     metadata = json.load(f)
# print("Number of metadata entries:", len(metadata))
# print("First entry:", metadata[0])


def load():
    embeddings = np.load('store/embeddings.npz')
    with open('store/metadata.json', 'r') as f:
        metadata = json.load(f)

    combined_data = []
    for embedding, meta in zip (embeddings['embeddings'], metadata):
        combined_data.append({
            'text': meta['text'],
            'source': meta['source'],
            'chunk_index': meta['chunk_index'],
            'embedding': embedding
        })

    return combined_data

    #print(combined_data[0])

def question_embedding(question):
    embedded_question = model.encode(question)
    return embedded_question

def cosine_similarity(vec_a, vec_b):
    return (np.dot(vec_a, vec_b)) / (np.linalg.norm(vec_a) * np.linalg.norm(vec_b))

def retrieval(question, n_results = 3):
    data = load()
    q_embedding = question_embedding(question)

    chunk_score_dict = []

    for chunk in data:
        similarity = cosine_similarity(chunk['embedding'], q_embedding)
        chunk_score_dict.append({
            'text': chunk['text'],
            'source': chunk['source'],
            'chunk_index': chunk['chunk_index'],
            'similarity_score': similarity
        })
    
    sorted_chunks = sorted(chunk_score_dict, key=lambda x: x['similarity_score'], reverse=True)
    return sorted_chunks[:n_results]

# if __name__ == "__main__":
#     question = "why does my forehand go into the net?"
#     results = retrieval(question)
    
#     print(f"Question: {question}\n")
#     for i, result in enumerate(results):
#         print(f"Rank {i+1} — Score: {result['similarity_score']:.3f}")
#         print(f"Source: {result['source']} (chunk {result['chunk_index']})")
#         print(f"Text: {result['text'][:150]}...")
#         print("---")


