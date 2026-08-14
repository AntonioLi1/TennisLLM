import json
import sys
import os
from pathlib import Path
from operator import attrgetter


folder_path = Path("param_tuning_results")

data_from_all_files = []
for file_path in folder_path.iterdir():
    if file_path.is_file():
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            all_scores = data.get("scores")
            all_configs = data.get("config")
            combined_data = all_scores | all_configs
            #print(f"combined {combined_data}")
            data_from_all_files.append(combined_data)

#print(data_from_all_files)
sorted_data = sorted(data_from_all_files, key=lambda x: x['avg_groundedness'], reverse=True)
print(f"sorted {sorted_data}")