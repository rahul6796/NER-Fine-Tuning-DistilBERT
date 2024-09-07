


from src.finetunningDistilBertner.logging import logger
from src.finetunningDistilBertner.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.finetunningDistilBertner.pipeline.data_validation_pipeline import DataValidationPipeline
from src.finetunningDistilBertner.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.finetunningDistilBertner.pipeline.model_trainer_pipeline import ModelTrainerPipeline



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



START_STAGE = "data Transformation"

try:
    data_transformation  = DataTransformationPipeline()
    data_transformation.run()
    logger.info(f'successfully execute :: {START_STAGE}')
except Exception as e:
    logger.error(f"Error in {START_STAGE} stage: {str(e)}")



START_STAGE = "model trainer"

try:
    data_transformation  = DataTransformationPipeline()
    data_transformation.run()
    logger.info(f'successfully execute :: {START_STAGE}')
except Exception as e:
    logger.error(f"Error in {START_STAGE} stage: {str(e)}")
