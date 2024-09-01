

from src.finetunningDistilBertner.utils.common import read_yaml, create_directories
from src.finetunningDistilBertner.entity import DataIngestionConfig, DataValidationConfig
from src.finetunningDistilBertner.constant import PARAMS_PATH_FILE, CONFIG_PATH_FILE


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
    


        
        
