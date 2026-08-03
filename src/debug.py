# from retrieval import retrieval

# results = retrieval("how do I move to hit an overhead?", n_results=3)

# for r in results:
#     print(f"Source: {r['source']} | Chunk: {r['chunk_index']} | Score: {r['similarity_score']:.3f}")
#     print(r['text'][:150])
#     print("---")

from loader import load_corpus
from chunk import chunk_text

documents = load_corpus('../corpus/')
chunks = chunk_text(documents)

smash_chunks = [c for c in chunks if c['source'] == 'smashes.txt']
for c in smash_chunks:
    print(f"Chunk {c['chunk_index']}:")
    print(c['text'])
    print("===")