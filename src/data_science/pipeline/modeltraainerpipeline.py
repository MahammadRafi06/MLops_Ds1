from src.data_science.config.configuration import (ConfigurationManager)
from src.data_science import logger
from src.data_science.components.modeltrainer import ModelTrainer

STAGE_NAME = "Model Training stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass
    def initiate_model_training(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_modeltrainer_config()
        data_transofrmation = ModelTrainer(model_trainer_config)
        data_transofrmation.model_training()