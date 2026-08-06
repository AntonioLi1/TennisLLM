from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

SYSTEM_PROMPT = """You are a tennis coaching assistant built on the 
knowledge and methodology of an elite tennis coach. Answer questions 
using ONLY the provided context. If the context doesn't contain enough 
information to answer confidently, say so rather than guessing. Always 
explain WHY a technique works, not just what to do."""

def generator(sorted_chunks, question):
    client = Anthropic(
        api_key = os.environ.get("ANTHROPIC_API_KEY")
    )

    context = "\n\n---\n\n".join(chunk['text'] for chunk in sorted_chunks)


    response = client.messages.create(
        max_tokens=1024,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {question}"
            }
        ],
        system=SYSTEM_PROMPT,
        model="claude-haiku-4-5",
    )

    return response.content[0].text

