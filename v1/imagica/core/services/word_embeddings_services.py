from .properties_services import WordEmbeddingsProperties
import logging
import tqdm
import numpy as np

EmbeddingProperties = WordEmbeddingsProperties()

class EmbedddingServices:
    @staticmethod
    def load_embeddings():
        embedding_index = []
        loading_not_possible = []
        logging.debug("Loading Word Embeddings")
        with open(EmbeddingProperties.glove_file,encoding="latin") as embedding_file:
            for line in tqdm(embedding_file):
                values = line.split()
                word = values[0]
                try:
                    coefs = np.asarray(values[1:], dtype="float32")
                    assert len(coefs) == WordEmbeddingsProperties.embedding_dimensions["Word"]["NonTrainable"]
                    embedding_index[word] = coefs
                except(AssertionError,ValueError):
                    logging.debug("Loading Word Embeddings{}".format(word))
                    loading_not_possible.append(word)
        logging.debug("Could not load count{}".format(len(loading_not_possible)))
        logging.debug("Found {} word vectors".format(len(embedding_index)))
        return embedding_index