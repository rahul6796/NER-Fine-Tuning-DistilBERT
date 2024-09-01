


from src.finetunningDistilBertner.logging import logger
from src.finetunningDistilBertner.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.finetunningDistilBertner.pipeline.data_validation_pipeline import DataValidationPipeline




START_STAGE = "data ingestion"

try:
    data_ingestion  = DataIngestionPipeline()
    data_ingestion.run()
    logger.info(f'successfully execute :: {START_STAGE}')
except Exception as e:
    logger.error(f"Error in {START_STAGE} stage: {str(e)}")





START_STAGE = "data Validation"

try:
    data_validation  = DataValidationPipeline()
    data_validation.run()
    logger.info(f'successfully execute :: {START_STAGE}')
except Exception as e:
    logger.error(f"Error in {START_STAGE} stage: {str(e)}")