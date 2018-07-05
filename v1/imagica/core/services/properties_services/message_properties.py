import os

from django.conf import settings

from .properties_utils import load_json


class InternalMessageProperties:
    def __init__(self):
        self.config_file = os.path.join(settings.CONFIG_FOLDER, "message_properties.json")
        message_properties = load_json(self.config_file)["Internal"]
        self.message_host = message_properties["MQHost"]
        self.message_port = message_properties["MQPort"]
        self.exchange_name = message_properties["ExchangeName"]
        self.routing_keys = message_properties["RoutingKeys"]


class ExternalMessageProperties:
    def __init__(self):
        self.config_file = os.path.join(settings.CONFIG_FOLDER, "message_properties.json")
        message_properties = load_json(self.config_file)["External"]
        self.message_host = message_properties["MQHost"]
        self.message_port = message_properties["MQPort"]
        self.exchange_name = message_properties["ExchangeName"]
        self.routing_keys = message_properties["RoutingKeys"]
