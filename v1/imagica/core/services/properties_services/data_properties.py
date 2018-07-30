import os
from django.conf import settings
from .properties_utils import load_json


class DataProperties:
    def __init__(self):
        self.config_file = os.path.join(settings.CONFIG_FOLDER, "data_properties.json")
        data_properties = load_json(self.config_file)
        self.source_type = data_properties["SourceType"]