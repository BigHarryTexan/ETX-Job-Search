import json
import os

DATA_FILE = "data/last_run.json"

def load_last_run():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_current_run(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def diff(new, old):
    old_set = {(o["source"], o["title"]) for o in old}
    return [n for n in new if (n["source"], n["title"]) not in old_set]

