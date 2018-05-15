from .services.services_registry import ServiceRegistry


class ModelTrainer:
    def __init__(self):
        self.services_registry = ServiceRegistry()

    def train(self):
        pass
