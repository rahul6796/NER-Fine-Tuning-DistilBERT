

from src.finetunningDistilBertner.entity import DataTransformationConfig
import os
from transformers import AutoTokenizer
from datasets import load_from_disk







class DataTransformation:

    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)



    def align_labels_with_tokens(self, labels, word_ids):
        new_labels = []
        current_word = None
        for word_id in word_ids:
            if word_id != current_word:
                current_word = word_id
                label = -100 if word_id is None else labels[word_id]
                new_labels.append(label)
            elif word_id is None:
                new_labels.append(-100)
            else:
                label = labels[word_id]
                if label % 2 == 1:
                    label += 1
                new_labels.append(label)

        return new_labels 
    
    
    def tokenize_and_align_label(self, example):

        tokenized_inputs = self.tokenizer(example['tokens'],
                                          truncation=True,
                                          is_split_into_words=True)
        
        all_labels = example['ner_tags']
        new_labels = []

        for i, labels in enumerate(all_labels):
            word_ids = tokenized_inputs.word_ids(batch_index=i)
            new_labels.append(self.align_labels_with_tokens(labels, word_ids))

        tokenized_inputs['labels'] = new_labels

        return tokenized_inputs
    

    def convert(self):
        conll2003 = load_from_disk(self.config.data_path)
        
        conll2003_dilbert = conll2003.map(
            self.tokenize_and_align_label,
            batched=True,
            remove_columns=conll2003["train"].column_names)
        
        conll2003_dilbert.save_to_disk(os.path.join(self.config.root_dir,"conll203"))

