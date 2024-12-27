import json

INPUT_FILE = "input.json"

def task(json_data) -> float:
    sum = 0
    for score_weight_dict in json_data:
        sum += score_weight_dict["score"] * score_weight_dict["weight"]
    return round(sum,3)

with open(INPUT_FILE) as f:
    json_data = json.load(f)
print(task(json_data))
