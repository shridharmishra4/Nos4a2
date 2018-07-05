import os
import datetime

import keras.backend as K

from .model_architectures import ModelArchitectures
from .pre_processing import PreProcessor
from .services.services_registry import ServiceRegistry

model_architecture_identifier = None
models_folder = None


class ModelTrainer:
    def __init__(self):
        self.services_registry = ServiceRegistry()

    def train(self):
        K.clear_session()

        model_architecture = ModelArchitectures(model_architecture_identifier).get_model()
        time_at_train = datetime.datetime.now().strftime("%Y=%m-%d--%H-%M-%S")
        current_models_folder = os.path.join(models_folder, f"models_{time_at_train}")

        if not os.path.exists(current_models_folder):
            os.makedirs(current_models_folder)

        models_weights_file = os.path.join(current_models_folder, f"models_{time_at_train}.h5")
        model_config_file = os.path.join(current_models_folder, f"models_{time_at_train}.json")

        fold_number = 0

        train_df, embeddings_index, tokenized_indices, mapping = PreProcessor()

        print("Nothing here")
