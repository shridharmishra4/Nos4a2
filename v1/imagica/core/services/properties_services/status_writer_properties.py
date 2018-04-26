import os

from django.conf import settings
from .properties_utils import load_json


class StatusWriterConfig:
    def __init__(self):
        self.config_file = os.path.join(settings.CONFIG_FOLDER, "status_writer_config.json")
        status_writer_config = load_json(self.config_file)
        self.writer_type = status_writer_config["WriterType"]
