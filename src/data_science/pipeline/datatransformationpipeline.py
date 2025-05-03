from src.data_science.config.configuration import (ConfigurationManager)
from src.data_science.entity.config_entity import (DataTransformationConfig)
from src.data_science import logger
from src.data_science.components.datatransformation import DataTransformation
from pathlib import Path
# try:
#     config = ConfigurationManager()
#     data_transofrmation_config = config.get_datatransformation_config()
#     data_transofrmation = DataTransformation(data_transofrmation_config)
#     data_transofrmation.train_test_splitting()
# except Exception as e:
#     raise e 


STAGE_NAME = "Data transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def initiate_data_transformation(self):
        config = ConfigurationManager()
        data_validation_status = config.get_datavalidation_config()
        try:
            with open(Path(data_validation_status.STATUS_FILE), "r") as f:
                content = f.read().split()
                if 'True' in content[-1]:
                    data_transofrmation_config = config.get_datatransformation_config()
                    data_transofrmation = DataTransformation(data_transofrmation_config)
                    data_transofrmation.train_test_splitting()
                else:
                    logger.exception("Schema validation failed Skipping this step")     
        except Exception as e :
            logger.exception(e)
                

# if __name__=="__main__":
#     try:
#         logger.info(f">>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<<<<<")
#         obj = DataTransformationTrainingPipeline()
#         obj.initiate_data_transformation()
#         logger.info(f">>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<<<<<\n\nx===================x")
#     except Exception as e:
#         logger.exception(e)
#         raise e
     