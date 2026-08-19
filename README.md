A Retrieval-Augmented Coaching Assistant. 

Rather than providing customers with generic tennis advice, I built a RAG-based coaching assistant based on my own playing and coaching philosophies. 
The corpus currently includes 14 detailed documents and will continue to grow as I further broaden my knowledge. 

The weights of the LLM never changes. Each question is answered by retrieving the most relevant chunks and passing them to Claude as context. 
This allows the corpus to be instantly updateable, we can trace every answer back to its source, and maintain a low cost compared to fine tuning. 

Why Retrieval is not built with a vector database:
Most RAG's utilise Pinecone or Chroma, however at this corpus' scale I won't be requiring such services. I implemented the cosine similarity search directly in numpy by computing the dot product of two vectors divided by their magnitudes, then ranking all stored chunks by that score. This meant I understood exactly what the retrieval process involved, rather than relying on a library black box. 
