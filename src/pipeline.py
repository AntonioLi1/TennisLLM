from loader import load_corpus
from chunk import chunk_text
from embedder import embedder
from store import store
from retrieval import retrieval
from generator import generator

corpusURL = 'D:\Desktop\Projects\TennisLLM\corpus/'
#corpusURL = '../corpus/'

documents = load_corpus(corpusURL)
chunks = chunk_text(documents)
embedded_chunks = embedder(chunks)
store(embedded_chunks)


print("type 'exit' to leave this chat.")

while True:

    question = input("Ask your tennis question! ")

    if question.lower() == 'exit':
        break

    retrieved = retrieval(question)

    response = generator(retrieved, question)

    print(f"response: {response}")


# print(f"total chunks: {len(embedded_chunks)}")
# print("--")

# for embedded_chunk in embedded_chunks:
#     print(f"Source: {embedded_chunk['source']} | Index: {embedded_chunk['chunk_index']} | Words: {len(embedded_chunk['text'].split())}")
#     print(embedded_chunk['text'][:100])
#     print(embedded_chunk['embedding'][:100])    
#     print("---")

