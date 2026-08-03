import json
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from retrieval import retrieval
from generator import generator
import re


with open('eval_set.json', 'r') as file:
    eval_data = json.load(file)

#print(type(eval_data))

for item in eval_data:
    question = item['question']
    source = item['source']
    keywords = item['expected_keywords']

    retrieved = retrieval(question)
    response = generator(retrieved, question)

    pattern = re.compile(r'\b(' + '|'.join(keywords) + r')\b', re.IGNORECASE)
    matches = pattern.findall(response)
    themes_found = [kw for kw in keywords if kw.lower() in response.lower()]


    print(len(matches) / len(keywords))
