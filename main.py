from src.data_science import logger
from src.data_science.pipeline.dataingestionpipeline import DataIngestionTrainingPipeline
logger.info("Welcome to our data science project")

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"<<<<<STAGE {STAGE_NAME} started <<<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f"<<<<<STAGE {STAGE_NAME} completed <<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e  