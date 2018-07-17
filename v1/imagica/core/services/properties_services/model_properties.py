import os
import json

from django.conf import settings

from .properties_utils import load_json


class ModelProperties:
    def __init__(self):
        self.config_file = os.path.join(settings.CONFIG_FOLDER, "model_params.json")
        model_params = load_json(self.config_file)
        self.random_state = model_params["RandomState"]

