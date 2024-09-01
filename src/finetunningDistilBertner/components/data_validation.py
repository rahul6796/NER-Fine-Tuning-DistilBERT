


from src.finetunningDistilBertner.config.configuration import DataValidationConfig
import os 


class DataValidation:

    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_the_files(self)->bool:

        validation_status = None 
        
        all_files = os.listdir(os.path.join('artifacts', 'data_ingestion', 'conll2003'))

        for file in all_files:
            
            if file not in self.config.ALL_REQUIRED_FIELS:
                validation_status = False
                with open(self.config.STATUS_FIEL, 'w') as f:
                    f.write(f'{validation_status}')
            else:
                validation_status = True
                with open(self.config.STATUS_FIEL, 'w') as f:
                    f.write(f'{validation_status}')
        return validation_status
