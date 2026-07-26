import numpy as np
import json
import os


def store (embedded_chunks):

    temp_storage_embeddings = []
    for chunk in embedded_chunks:
        embedding = chunk['embedding']
        temp_storage_embeddings.append(embedding)
    
    embeddings_matrix = np.array(temp_storage_embeddings)
    os.makedirs('store', exist_ok=True)
    np.savez('store/embeddings.npz', embeddings = embeddings_matrix)

    metadata = []
    for chunk in embedded_chunks:
        metadata.append({
            'text': chunk['text'],
            'source': chunk['source'],
            'chunk_index': chunk['chunk_index']
        })
    
    with open('store/metadata.json', 'w') as f:
        json.dump(metadata, f)
    
    print(f"Saved {len(embedded_chunks)} chunks to store/")