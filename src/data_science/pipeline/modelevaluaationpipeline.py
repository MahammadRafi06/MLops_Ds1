from src.data_science.config.configuration import (ConfigurationManager)
from src.data_science import logger
from src.data_science.components.modelevaluation import ModelEvaluation

STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    def initiate_evaluation_training(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_modelevaludation_config()
        data_evaluation = ModelEvaluation(model_evaluation_config)
        data_evaluation.model_evaluation()