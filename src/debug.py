from retrieval import retrieval
from loader import load_corpus
from chunking import chunk_text

results = retrieval("Explain movement in tennis for me?", n_results=5)

for r in results:
    print(f"Source: {r['source']} | Chunk: {r['chunk_index']} | Score: {r['similarity_score']:.3f}")
    print(r['text'][:150])
    print("---")

# from loader import load_corpus
# from chunk import chunk_text

# documents = load_corpus('../corpus/')
# chunks = chunk_text(documents)

# smash_chunks = [c for c in chunks if c['source'] == 'smashes.txt']
# for c in smash_chunks:
#     print(f"Chunk {c['chunk_index']}:")
#     print(c['text'])
#     print("===")
# corpusURL = 'D:\Desktop\Projects\TennisLLM\corpus/'

# documents = load_corpus(corpusURL)
# chunks = chunk_text(documents)