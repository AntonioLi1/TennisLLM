from loader import load_corpus
from chunking import chunk_text
from embedder import embedder
from store import store
from retrieval import retrieval
from generator import generator

#corpusURL = 'D:\Desktop\Projects\TennisLLM\corpus/'
corpusURL = '../corpus/'

documents = load_corpus(corpusURL)
chunks = chunk_text(documents, 150, 45) 
embedded_chunks = embedder(chunks)
store(embedded_chunks)


print("type 'exit' to leave this chat.")

while True:

    question = input("Ask your tennis question! ")

    if question.lower() == 'exit':
        break

    retrieved = retrieval(question, 5) # defaulted to 5

    response = generator(retrieved, question)

    print(f"response: {response}")

