import os
import logging

import pickle as pkl

from .utilities import Utilities
from .pre_processing import PreProcessingGenerator

common_words_file = ""
text_column = None


class SpecialWordsDBIO:
    def get_latest_result(self):
        pass

    def write_result(self, result):
        pass


class SpecialWordsFolderIO:
    def get_latest_result(self):
        pass

    def write_result(self, result):
        pass


class SpecialWordsIO:
    def __init__(self, special_words_config):
        self.special_words_config = special_words_config

    def get_latest_result(self):
        pass

    def write_result(self):
        pass


class SpecialWordsGenerator:
    def __init__(self):
        self.pre_processing_generator = PreProcessingGenerator()
        self.special_words_io = SpecialWordsIO()

    def create_special_words(self):
        embeddings_index = Utilities.load_embeddings()
        logging.debug(f"Found {len(embeddings_index)} word vectors")
        embeddings_words = set(embeddings_index.keys())
        with open(common_words_file, 'wb') as f:
            pkl.dump(embeddings_words, f)

        special_words = None
        self.special_words_io.write_result(special_words)

    def get_special_words(self):
        result = self.special_words_io.get_latest_result()
        if result is None:
            self.create_special_words()
        else:
            return result

        result = self.special_words_io.get_latest_result()
        if result is None:
            return {
                "Error": "Unable to create special words"
            }
        return result

    def get_special_words_lite(self):
        result = self.special_words_io.get_latest_result()
        if result is None:
            return {
                "Error": "Create special words with /specialWords"
            }
        return result
