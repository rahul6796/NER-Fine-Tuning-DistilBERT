

from src.finetunningDistilBertner.config.configuration import ConfigManager
from src.finetunningDistilBertner.components.data_transformation import DataTransformation



class DataTransformationPipeline:

    def __init__(self) -> None:
        pass

    def run(self):
        config = ConfigManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()
        
