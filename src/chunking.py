import os

def chunk_text(documents, chunk_size, overlap):
    chunked_document = []
    for document in documents:
        text_pointer_start = 0
        text_pointer_end = 0
        chunk_index = 0

        text = document['text']
        words = text.split()
        length = len(words)
        cleaned_doc_name = document['source'].removesuffix(".txt").replace("_", " ")
        #print(f"CLEANED DOC NAME: {cleaned_doc_name}")
        while text_pointer_start < length:

            text_pointer_end = text_pointer_start + chunk_size
            if text_pointer_end > length:
                text_pointer_end = length
            
            # print(f"text_pointer_start: {type(text_pointer_start)}")
            # print(f"text_pointer_end: {type(text_pointer_end)}")

            chunk_words = words[text_pointer_start:text_pointer_end]
            chunk_body = ' '.join(chunk_words)
            chunked_text = f"{cleaned_doc_name}: {chunk_body}"

            #print(f"chunked text: {chunked_text} \n")
            chunked_document.append({
                'text': chunked_text,
                'source': document['source'],
                'chunk_index': chunk_index
            })
            text_pointer_start += (chunk_size - overlap)
            chunk_index = chunk_index + 1
            # print(f"text_pointer_startEND: {type(text_pointer_start)}")
            # print(f"text_pointer_endEND: {type(text_pointer_end)}")

    return chunked_document




        
