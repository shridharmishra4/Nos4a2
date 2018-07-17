import os
import json


def load_json(json_file):
    if not os.path.exists(json_file):
        print("File does not exist: {}".format(json_file))
        return None

    with open(json_file, 'r') as f:
        file_contents = json.load(f)
    return file_contents
