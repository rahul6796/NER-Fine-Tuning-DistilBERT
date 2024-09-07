

from src.finetunningDistilBertner.entity import ModelTrainerConfig
from transformers import AutoModelForTokenClassification, AutoTokenizer
from transformers import DataCollatorForTokenClassification
from transformers import TrainingArguments, Trainer
from datasets import load_dataset, load_from_disk

import os 
import numpy as np 
import evaluate

metric = evaluate.load("seqeval")



class ModelTrainer:

    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        self.raw_datasets = load_from_disk(self.config.raw_data_path)

    def get_labels_names(self):
        
        ner_feature = self.raw_datasets["train"].features["ner_tags"]
        label_names = ner_feature.feature.names
        return label_names


    def get_labels(self):
        label_names = self.get_labels_names()
        labels = self.raw_datasets["train"][0]["ner_tags"]
        labels = [label_names[i] for i in labels]
        return labels


    def train(self):
        
        label_names = self.get_labels_names()
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        tokenized_datasets = load_from_disk(self.config.data_path)

        data_collector = DataCollatorForTokenClassification(tokenizer=tokenizer)
        id2label = {i: label for i, label in enumerate(label_names)}
        label2id = {v: k for k, v in id2label.items()}

        model = AutoModelForTokenClassification.from_pretrained(self.config.model_ckpt,
                                                                id2label=id2label,
                                                                label2id=label2id)

        args = TrainingArguments(output_dir = self.config.root_dir,
                                evaluation_strategy="epoch",
                                save_strategy="epoch",
                                learning_rate=2e-5,
                                num_train_epochs=3,
                                weight_decay=0.01)
        
    
        trainer = Trainer(
            model=model,
            args=args,
            train_dataset=tokenized_datasets["train"],
            eval_dataset=tokenized_datasets["validation"],
            data_collator=data_collector,
            compute_metrics=self.compute_metrix,
            tokenizer=tokenizer,
        )
        trainer.train()

        # Save model
        model.save_pretrained(os.path.join(self.config.root_dir,"ner-distilbert"))
        
        # Save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))


    def compute_metrix(self, eval_preds):
        label_names = self.get_labels_names()
        logits, labels = eval_preds
        predictions = np.argmax(logits, axis=-1)

        true_labels = [[label_names[l] for l in label if l != -100] for label in labels]

        true_predictions = [
        [label_names[p] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)]

        all_metrics = metric.compute(
            predictions=true_predictions,
            references=true_labels
        )

        return {
        "precision": all_metrics["overall_precision"],
        "recall": all_metrics["overall_recall"],
        "f1": all_metrics["overall_f1"],
        "accuracy": all_metrics["overall_accuracy"],
    }
        





        





