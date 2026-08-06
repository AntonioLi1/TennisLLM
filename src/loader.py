import os

def load_corpus(corpus_directory):
    documents = []
    for filename in os.listdir(corpus_directory):
        with open(os.path.join(corpus_directory, filename), 'r', encoding='utf-8') as file:
            documents.append({
                'text': file.read(),
                'source': filename
            })
    return documents

# if __name__ == "__main__":
#     documents = load_corpus('D:\Desktop\Projects\TennisLLM\corpus/')
    
#     for doc in documents:
#         print(f"Source: {doc['source']}")
#         print(f"Text preview: {doc['text'][:200]}")
#         print("---")