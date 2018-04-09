import os
import json
import datetime

from django.conf import settings
from pymongo import MongoClient


def load_json(json_file):
    if not os.path.exists(json_file):
        print("File does not exist: {}".format(json_file))
        return None

    with open(json_file, 'r') as f:
        file_contents = json.load(f)
    return file_contents


class ModelProperties:
    def __init__(self):
        self.config_file = os.path.join(settings.CONFIG_FOLDER, "model_params.json")
        model_params = json.load(self.config_file)
        self.random_state = model_params["RandomState"]


class ValidationProperties:
    def __init__(self):
        self.config_file = os.path.join(settings.CONFIG_FOLDER, "validation_properties.json")
        validation_properties = load_json(self.config_file)
        self.validation_type = validation_properties["ValidationType"]


class DataProperties:
    def __init__(self):
        self.config_file = os.path.join(settings.CONFIG_FOLDER, "data_properties.json")
        data_properties = load_json(self.config_file)
        self.source_type = data_properties["SourceType"]


class StatusWriterConfig:
    def __init__(self):
        self.config_file = os.path.join(settings.CONFIG_FOLDER, "status_writer_config.json")
        status_writer_config = load_json(self.config_file)
        self.writer_type = status_writer_config["WriterType"]


class WordEmbeddingsProperties:
    pass
