


from src.finetunningDistilBertner.logging import logger
from src.finetunningDistilBertner.pipeline.data_ingestion_pipeline import DataIngestionPipeline




START_STAGE = "data ingestion"

try:
    data_ingestion  = DataIngestionPipeline()
    data_ingestion.run()
    logger.info(f'successfully execute :: {START_STAGE}')
except Exception as e:
    logger.error(f"Error in {START_STAGE} stage: {str(e)}")