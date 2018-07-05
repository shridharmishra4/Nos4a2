import os
import json
import logging

import numpy as np
import pickle as pkl
import tensorflow as tf

from keras.models import model_from_json

from .pre_processing import PreProcessor
from .utilities import Utilities

parallelize = False
text_column = None
tag_column = None
char_text_column = None
max_len = 100
char_in_model = False
models_folder = None
num_folds = 4
word_tokenizer_pkl = None
word_trainable_tokenizer_pkl = None


class Model:
    def __init__(self, models, tokenizers, graph, class_mapping_number_name):
        self.models = models
        self.tokenizers = tokenizers
        self.graph = graph
        self.class_mapping_number_name = class_mapping_number_name
        self.pre_processor = PreProcessor(tokenizers=tokenizers, max_lengths=[max_len],
                                          class_mapping_number_name=class_mapping_number_name)
        self.class_mapping_name_number = dict()
        for column in self.class_mapping_number_name:
            self.class_mapping_name_number[column] = {value: key for key, value in
                                                      self.class_mapping_number_name[tag_column].items()}
        self.num_classes = len(self.class_mapping_number_name[tag_column])

    def predict(self, document):

        input_text = document[text_column]
        input_text = " ".join(map(str, input_text.values))

        logging.info("Input Sentence: {}".format(input_text))

        word_length = len(input_text.split(' '))

        X_input = self.pre_processor.tokenize_pad_sentences([[input_text]])

        if char_in_model:
            X_input_char = self.pre_processor.make_X_char([document[char_text_column].tolist()])

        y_pred = None

        for model in self.models:
            with self.graph.as_default():
                if char_in_model:
                    if y_pred is None:
                        y_pred = model.predict(X_input, X_input_char)
                    else:
                        y_pred += model.predict(X_input, X_input_char)

                else:
                    if y_pred is None:
                        y_pred = model.predict(X_input)
                    else:
                        y_pred += model.predict(X_input)

        y_pred = np.argmax(y_pred, axis=2)
        y_pred = y_pred.flatten()

        y_pred = y_pred[-word_length:]

        return y_pred


class ModelLoader:
    @staticmethod
    def load_model():
        all_models_folder = [os.path.join(models_folder, d)
                             for d in os.listdir(models_folder)
                             if os.path.isdir(os.path.join(models_folder, d))]

        last_trained_models_folder = max(all_models_folder, key=os.path.getmtime)
        time_at_train = last_trained_models_folder.split('_')[-1]
        model_config_file = os.path.join(last_trained_models_folder, f'models_{time_at_train}.json')

        if os.path.exists(model_config_file):
            logging.debug("Loading model config file {}".format(model_config_file))
            with open(model_config_file, 'r') as file:
                model_json = file.read()

        else:
            print("Model config file not found: {}".format(model_config_file))
            return None

        model = model_from_json(model_json)
        if parallelize:
            model = Utilities.multi_gpu_model(model, 2)

        models = []
        for fold in range(num_folds):
            model_weights_file = os.path.join(last_trained_models_folder, f'models_{time_at_train}_{fold}.h5')
            logging.debug("Loading model weights file {}".format(model_weights_file))

            model.load_weights(model_weights_file)
            models.append(model)

        with open(word_tokenizer_pkl, 'rb') as f:
            word_tokenizer = pkl.load(f)

        with open(word_trainable_tokenizer_pkl, 'rb') as f:
            word_trainable_tokenizer = pkl.load(f)

        tokenizers = {
            "Word": word_tokenizer,
            "WordTrainable": word_trainable_tokenizer
        }

        graph = tf.get_default_graph()

        with open(os.path.join(last_trained_models_folder, f"data_{time_at_train}"), 'r') as file:
            mapping = json.load(file)

        model = Model(models=models, tokenizers=tokenizers, graph=graph, class_mapping_number_name=mapping)

        return model


class InstancePredictor:
    def __init__(self, model):
        self.model = model

    def prediction(self, document):
        model_prediction = self.model.predict(document)
        return model_prediction
        #write_to_db()
        #write_message() 