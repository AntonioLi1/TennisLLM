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

results = []


for item in eval_data:
    question = item['question']
    source = item['source']
    keywords = item['expected_keywords']

    retrieved = retrieval(question, 5)
    response = generator(retrieved, question)

    # groundedness — does the FINAL ANSWER contain the expected keywords?
    themes_found_in_answer = [kw for kw in keywords if kw.lower() in response.lower()]
    groundedness_score = len(themes_found_in_answer) / len(keywords)

    # retrieval check — did the right document get retrieved at all?
    retrieved_sources = [r['source'] for r in retrieved]
    source_hit = source in retrieved_sources

    results.append({
        'question': question,
        'source_hit': source_hit,
        'groundedness_score': groundedness_score,
        'themes_missing': [kw for kw in keywords if kw not in themes_found_in_answer]
    })

    print(f"{question[:50]:<52} | hit: {source_hit} | score: {groundedness_score:.2f} | missing: {[kw for kw in keywords if kw not in themes_found_in_answer]}")

avg_source_hit = sum(result['source_hit'] for result in results) / len(results)
avg_groundedness = sum(result['groundedness_score'] for result in results) / len(results)
output_data = {
    "config": {
        "chunk_size": 150,
        "overlap_percentage": 0.45,
        "n_results": 5
    },
    "scores": {
        "avg_source_hit": avg_source_hit,
        "avg_groundedness": avg_groundedness
    },
    "results" : results
}

script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, 'evaluation.json')
with open(output_path, 'w') as f:
    json.dump(output_data, f, indent=2)
