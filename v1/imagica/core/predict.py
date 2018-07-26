import numpy as np
import logging
from .pre_processing import PreProcessor
from .model_loader import ModelLoader

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

class InstancePredictor:
    def __init__(self, model):
        self.model = model


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

    def prediction(self, document):
        model = ModelLoader.load_model()
        prediction_instance = InstancePredictor(model)
        model_prediction = prediction_instance.predict(document)
        return model_prediction
        #write_to_db()
        #write_message()