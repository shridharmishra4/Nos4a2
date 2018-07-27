from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer
from .services.properties_services import data_properties
from sklearn.preprocessing import StandardScaler


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
    def __init__(self,all_files_df):
        self.all_files_df = all_files_df

    def load_text_labels(self):
        return

    def create_standard_scalers(self):
        standard_scaling_values = dict()
        standard_scalers = dict()

        ##TODO decide variable name
        for field in fields_to_be_standardized:
            standard_scaling_values[field] = list()
            self.all_files_df.apply(standard_scaling_values[field].extend)
            standard_scalers[field] = StandardScaler()

    def make_char_mapping(texts):
        all_chars = {''}
        for text in texts:
            for word_char_set in map(set,text.split(' ')):
                all_chars.update(word_char_set)
        char_mapping = {key: value for value, key in enumerate(sorted(list(all_chars)))}
        return char_mapping


    pass
