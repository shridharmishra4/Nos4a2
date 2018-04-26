import os

from django.conf import settings
from .properties_utils import load_json


class ValidationProperties:
    def __init__(self):
        self.config_file = os.path.join(settings.CONFIG_FOLDER, "validation_properties.json")
        validation_properties = load_json(self.config_file)
        self.validation_type = validation_properties["ValidationType"]