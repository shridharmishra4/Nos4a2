import os
from django.conf import settings
from .properties_utils import load_json


class WordEmbeddingsProperties:
    def __init__(self):
        self.config_file = os.path.join(settings.CONFIG_FOLDER, "word_embedding_properties.json")
        embedding_properties = load_json(self.config_file)
        self.glove_file = embedding_properties["Glove_Path"]
        self.embedding_dimensions = embedding_properties["embedding_dimensions"]

