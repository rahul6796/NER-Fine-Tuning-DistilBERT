
from src.finetunningDistilBertner.config.configuration import ConfigManager
from src.finetunningDistilBertner.components.data_validation import DataValidation





class DataValidationPipeline:

    def __init__(self) -> None:
        pass


    def run(self):
        config = ConfigManager()
        data_validation_config = config.get_data_validation()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_the_files()
