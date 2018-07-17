import os

os.environ['CUDA_VISIBLE_DEVICES'] = "1"

import numpy as np
import tensorflow as tf

config = tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)

from keras.layers.recurrent import LSTM
from keras.layers.cudnn_recurrent import CuDNNLSTM
from keras.layers import TimeDistributed, Dense, Input, Bidirectional, Dropout, BatchNormalization, merge, Conv1D, \
    MaxPooling1D, Activation
from keras.layers.embeddings import Embedding
from keras.models import Model
from tqdm import tqdm

from .services.properties_services import ModelProperties


class ModelArchitectures:
    def __init__(self, model_identifier):
        self.identifier = model_identifier
        self.model_properties = ModelProperties()

    def model_bilstm(self, embeddings_index, tokenized_indices, num_classes):
        embeddings_matrix = np.zeros(len(tokenized_indices["WordTrainable"]) + 1,
                                     self.model_properties.embedding_dim["Word"]["Trainable"])
        for word, i in tqdm(tokenized_indices["WordTrainable"].items()):
            embeddings_vector = embeddings_index.get(word)
            if embeddings_vector is not None:
                embeddings_matrix[i] = embeddings_vector

        word_input_layer = Input(shape=(self.model_properties.max_len,))
        word_layer = Embedding(input_dim=len(tokenized_indices["WordTrainable"]) + 1,
                               output_dim=self.model_properties.embedding_dim["Word"]['Trainable'],
                               weights=[embeddings_matrix], input_length=self.model_properties.max_len, mask_zero=True,
                               trainable=False)(word_input_layer)
        word_layer = Dropout(self.model_properties.dropout)(word_layer)

        merge_layer = word_layer
        merge_layer = BatchNormalization()(merge_layer)

        merge_layer = Bidirectional(LSTM(150, return_sequences=True))(merge_layer)
        merge_layer = Dropout(self.model_properties.dropout)(merge_layer)
        merge_layer = BatchNormalization()(merge_layer)

        layer = TimeDistributed(Dense(num_classes))(merge_layer)
        output_layer = Activation('softmax')(layer)
        model = Model(inputs=[word_input_layer], outputs=[output_layer])
        return model

    def model_multi_bilstm(self, embeddings_index, tokenized_indices, num_classes):
        pass

    def model_multi_embedding_multi_bilstm(self, embeddings_index, word_index, num_classes):
        pass

    def model_updated_multi_embedding_multi_bilstm(self, embeddings_index, tokenized_indices, num_classes):
        pass

    def model_char_multi_bilstm(self, embeddings_index, tokenized_indices, num_classes):
        pass

    def model_bilstm_crf(self,embeddings_index, tokenized_indices, num_classes):
        pass

    def get_model(self):
        model_architectures = {
            "bilstm": self.model_bilstm,
            "multi_bilstm": self.model_multi_bilstm,
            "char_multi_bilstm": self.model_char_multi_bilstm,
            "multi_embedding_multi_bilstm": self.model_multi_embedding_multi_bilstm,
            "bilstm_crf": self.model_bilstm_crf,
            "updated_multi_embedding_multi_bilstm": self.model_updated_multi_embedding_multi_bilstm
        }

        return model_architectures[self.identifier]