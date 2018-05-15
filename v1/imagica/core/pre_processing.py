
class PreProcessor:
    def __init__(self, tokenizers, max_lengths, class_mapping_number_name):
        self.tokenizers = tokenizers
        self.max_lengths = max_lengths
        self.class_mapping_number_name = class_mapping_number_name

    def tokenize_pad_sentences(self, input_texts):
        pass

    def make_X_char(self, char_sequences):
        pass


class PreProcessingGenerator:
    pass