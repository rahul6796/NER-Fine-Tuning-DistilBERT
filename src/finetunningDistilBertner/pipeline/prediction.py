

from src.finetunningDistilBertner.config.configuration import ConfigManager
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline



class PredictonPipeline:

    def __init__(self):
        self.config = ConfigManager().get_model_prediction_config()


    def predict(self, text):

        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)


        pipe  = pipeline(task='token-classification',
                         tokenizer=tokenizer,
                         model=self.config.model_path,
                         aggregation_strategy="simple")
        
        output = pipe(text)
        return output