from loader import load_corpus
from chunk import chunk_text
from embedder import embedder

corpusURL = 'D:\Desktop\Projects\TennisLLM\corpus/'

documents = load_corpus(corpusURL)
chunks = chunk_text(documents)
embedded_chunks = embedder(chunks)

print(f"total chunks: {len(embedded_chunks)}")
print("--")

for embedded_chunk in embedded_chunks:
    print(f"Source: {embedded_chunk['source']} | Index: {embedded_chunk['chunk_index']} | Words: {len(embedded_chunk['text'].split())}")
    print(embedded_chunk['text'][:100])
    print(embedded_chunk['embedding'][:100])
    print("---")