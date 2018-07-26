from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer


class PreProcessor:
    def __init__(self, tokenizers, max_lengths, class_mapping_number_name):
        self.tokenizers = tokenizers
        self.max_lengths = max_lengths
        self.class_mapping_number_name = class_mapping_number_name

    @staticmethod
    def tokenize_pad_sentences(self, input_texts):
        outputs = []
        for self.tokenizers, self.max_lengths, input_texts in zip(self.tokenizers.values(), self.max_lengths,
                                                                  input_texts):
            X = self.tokenizers.text_to_sequences(X, maxlen=self.max_lengths)
            X = sequence.pad_sentences(X, maxlen=self.max_lengths)
            outputs.append(X)
        return outputs

    def make_X_char(self, char_sequences):
        pass


class PreProcessingGenerator:
    pass
