import json
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from chunking import chunk_text
from embedder import embedder
from store import store

corpusURL = '../corpus/'

def build_pipeline(documents, chunk_size, overlap):
    chunks = chunk_text(documents, chunk_size,overlap)
    embedded_chunks = embedder(chunks)
    store(embedded_chunks)


