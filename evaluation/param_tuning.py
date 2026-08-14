import json
import sys
import os
from build_pipeline import build_pipeline
from run_evaluation import run_evaluation
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from loader import load_corpus
corpusURL = '../corpus/'

documents = load_corpus(corpusURL)

for chunk_size in [50,100,150,200]:
    for overlap_percentage in [0.2, 0.3, 0.45]:
        overlap = int(chunk_size * overlap_percentage)
        print(f"pass1: {chunk_size}")
        
        build_pipeline(documents, chunk_size, overlap)

        print("pass2")


        for n_results in [3,5]:
            print("pass3")

            results = run_evaluation(n_results)

            avg_source_hit = sum(result['source_hit'] for result in results) / len(results)
            avg_groundedness = sum(result['groundedness_score'] for result in results) / len(results)
            output_data = {
                "config": {
                    "chunk_size": chunk_size,
                    "overlap_percentage": overlap_percentage,
                    "n_results": n_results
                },
                "scores": {
                    "avg_source_hit": avg_source_hit,
                    "avg_groundedness": avg_groundedness
                },
                "results" : results
            }

            script_dir = os.path.dirname(os.path.abspath(__file__))
            results_dir = os.path.join(script_dir, 'param_tuning_results')
            os.makedirs(results_dir, exist_ok=True)
            filename = f"chunk{chunk_size}_overlap{overlap_percentage}_n{n_results}.json"
            output_path = os.path.join(results_dir, filename)
            
            with open(output_path, 'w') as f:
                json.dump(output_data, f, indent=2)
            print("pass4")