import os

def chunk_text(documents, chunk_size = 150, overlap=30):
    chunked_document = []


    for document in documents:
        text_pointer_start = 0
        text_pointer_end = 0
        chunk_index = 0

        text = document['text']
        words = text.split()
        length = len(words)

        while text_pointer_start < length:
            text_pointer_end = text_pointer_start + chunk_size
            if text_pointer_end > length:
                text_pointer_end = length
            
            chunk_words = words[text_pointer_start:text_pointer_end]
            chunked_text = ' '.join(chunk_words)
            
            chunked_document.append({
                'text': chunked_text,
                'source': document['source'],
                'chunk_index': chunk_index
            })
            text_pointer_start += (chunk_size - overlap)
            chunk_index = chunk_index + 1

    return chunked_document




        
