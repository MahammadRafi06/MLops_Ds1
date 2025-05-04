from src.data_science import logger
from src.data_science.pipeline.dataingestionpipeline import DataIngestionTrainingPipeline
from src.data_science.pipeline.datavalidationpipeline import DataValidationTrainingPipeline
from src.data_science.pipeline.datatransformationpipeline import DataTransformationTrainingPipeline
from src.data_science.pipeline.modeltraainerpipeline import ModelTrainingPipeline
from src.data_science.pipeline.modelevaluaationpipeline import ModelEvaluationPipeline
logger.info("Welcome to our data science project")

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"<<<<<STAGE {STAGE_NAME} started <<<<<<<<<<<\n\nx===================x")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f"<<<<<STAGE {STAGE_NAME} completed <<<<<<<<<<<\n\nx===================x")
except Exception as e:
    logger.exception(e)
    raise e  



STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<<<<<\n\nx===================x")
    obj = DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<<<<<\n\nx===================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data transformation stage"
try:
    logger.info(f">>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<<<<<\n\nx===================x")
    obj = DataTransformationTrainingPipeline()
    obj.initiate_data_transformation()
    logger.info(f">>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<<<<<\n\nx===================x")
except Exception as e:
    logger.exception(e)
    raise e  


STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f">>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<<<<<\n\nx===================x")
    obj = ModelTrainingPipeline()
    obj.initiate_model_training()
    logger.info(f">>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<<<<<\n\nx===================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f">>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<<<<<\n\nx===================x")
    obj = ModelEvaluationPipeline()
    obj.initiate_evaluation_training()
    logger.info(f">>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<<<<<\n\nx===================x")
except Exception as e:
    logger.exception(e)
    raise e