A Retrieval-Augmented Coaching Assistant. 

Rather than providing customers with generic tennis advice, I built a RAG-based coaching assistant based on my own playing and coaching philosophies. 
The corpus currently includes 14 detailed documents and will continue to grow as I further broaden my knowledge. I was able to utilise this tool on my tennis coaching website 'sydneytennisacademy.au' for real student usage. It provided me with real feedback in terms of popular queries and which topics to provide further expertise. 

In an RAG, the weights of the LLM never changes. Each question is answered by retrieving the most relevant chunks and passing them to Claude as context. 
This allows the corpus to be instantly updateable, we can trace every answer back to its source, and maintain a low cost compared to fine tuning. 

Why Retrieval is not built with a vector database:
Most RAG's utilise Pinecone or Chroma, however at this corpus' scale I won't be requiring such services. I implemented the cosine similarity search directly in numpy by computing the dot product of two vectors divided by their magnitudes, then ranking all stored chunks by that score. This meant I understood exactly what the retrieval process involved, rather than relying on a library black box. 

Evaluation Methodology:
Using a 27-question evaluation set based on real student questions, I tracked the: source hit rate and groundedness. Source hit rate confirms if the retrieval found the correct document. Groundedness measures the expected themes and keywords in the generated answer. 
Baseline results (chunk size = 150, overlap = 30, top n results = 3, temperature = 0):
  Source Hit Rate = 100%
  Average Groundedness = 88.5%
For parameter tuning, I ran a grid search manipulating the chunk size, overlap percentage, and top n results, rebuilding the full pipeline for each configuration and re-running the evaluations set questions. I found the highest-performing configuration was:
chunk size = 150, overlap percentage = 45% and top n results = 5. This configuration provided results of:
  Source Hit Rate = 100%
  Average Groundedness = 91.2%
By increasing top n results, we have more chances to surface the correct chunk. This actually directly addressed a bug that will be mentioned below, where the right context was present but wasn't ranked highly enough. A higher overlap in chunking reducing the chances of important information being split across a chunk, which fixed an issue experienced previously. 

Key Bug Found Through Evaluation:
Chunk boundary content dilution. A question about the topspin forehand failed despite having the correct documents being retrieved. This was due to the separate chunking of the document's intro and because the term 'topspin' wasn't repeated throughout the corpus, the embedding lost the topic. By implementing 'contextual chunking' we were able to efficiently maintain the topics of chunks, leading to better retrieved results.
 
Tech Stack:
Python, sentence-transformers, numpy, Anthropic API (Claude Haiku), JSON-based storage

Future Work:
- Fine tuning: LoRA fine-tuning an open-weights model (Llama 3.2 / Mistral 7B) on a curated Q&A dataset derived from the evaluation set, compared against the current RAG-only approach.
- Expansion of corpus and topics to meet client demands
- I noticed the architecture doesn't guarantee cross-document retrieval for comparison questions, and the fix would be query decomposition — detecting comparison intent and retrieving separately per topic before combining
