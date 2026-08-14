import json
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from retrieval import retrieval
from generator import generator
import re


def run_evaluation(n_results):
    with open('eval_set.json', 'r') as file:
        eval_data = json.load(file)

    #print(type(eval_data))

    results = []

    for item in eval_data:
        question = item['question']
        source = item['source']
        keywords = item['expected_keywords']

        retrieved = retrieval(question, n_results)
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

    return results
