import numpy as np

def store (embedded_chunks):

    temp_storage_embeddings = []
    for chunk in embedded_chunks:
        embedding = chunk['embedding']
        temp_storage_embeddings.append(embedding)
    
    embeddings_matrix = np.array(temp_storage_embeddings)
    np.savez('store/embeddings.npz', embeddings = embeddings_matrix)