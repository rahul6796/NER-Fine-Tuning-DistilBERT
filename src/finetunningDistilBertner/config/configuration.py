

from src.finetunningDistilBertner.utils.common import read_yaml, create_directories
from src.finetunningDistilBertner.entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
from src.finetunningDistilBertner.constant import PARAMS_PATH_FILE, CONFIG_PATH_FILE
from src.finetunningDistilBertner.entity import ModelTrainerConfig


class ConfigManager:

    def __init__(self, 
            config_filepath = CONFIG_PATH_FILE,
            params_filepath = PARAMS_PATH_FILE
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        
        config =  self.config.data_ingestion
        
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_file_path=config.local_file_path,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    

    def get_data_validation(self)->DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FIEL=config.STATUS_FIEL,
            ALL_REQUIRED_FIELS=config.ALL_REQUIRED_FIELS
        )
        
        return data_validation_config
    

    def get_data_transformation_config(self)->DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name=config.tokenizer_name

        )

        return data_transformation_config
    

    def get_model_trainer_config(self)-> ModelTrainerConfig:
        config = self.config.model_trainer
        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            raw_data_path = config.raw_data_path,
            data_path=config.data_path,
            model_ckpt=config.model_ckpt
        )

        return model_trainer_config
    




        
        
