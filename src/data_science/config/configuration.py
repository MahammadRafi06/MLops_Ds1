from src.data_science.constants import CONFIG_FILE_PATH, SCHEMA_FILE_PATH, PARAMS_FILE_PATH
from src.data_science.utils.common import read_yaml, create_dir, read_envfile
from src.data_science.entity.config_entity import (DataIngestionConfig,
                                                   DataValidationConfig, 
                                                   DataTransformationConfig,
                                                   ModelTrainerConfig,
                                                   ModelEvaluationConfig
                                                   )
from src.data_science.constants import CONFIG_FILE_PATH, SCHEMA_FILE_PATH, PARAMS_FILE_PATH
from src.data_science.utils.common import read_yaml, create_dir
from src.data_science.constants import CONFIG_FILE_PATH, SCHEMA_FILE_PATH, PARAMS_FILE_PATH
from src.data_science.utils.common import read_yaml, create_dir
import os 
from pathlib import Path
class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, schema_file_path= SCHEMA_FILE_PATH, params_file_path=PARAMS_FILE_PATH ):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)
        self.envs = read_envfile(Path(self.config.env_file_path))  
        create_dir([self.config.artifacts_root])
        
    def get_dataingestion_config(self)-> DataIngestionConfig:
        config = self.config.data_ingestion
        create_dir([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
              root_dir= config.root_dir,
              source_URL=config.source_URL,
              local_data_file=config.local_data_file ,
              unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    def get_datavalidation_config(self)-> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        create_dir([config.root_dir])
        data_validation_config = DataValidationConfig(
              root_dir= config.root_dir,
              STATUS_FILE=config.STATUS_FILE,
              unzip_data_dir=config.unzip_data_dir ,
              all_schema=schema
        )
        return data_validation_config
    
    def get_datatransformation_config(self)-> DataTransformationConfig:
        config = self.config.data_transformation
        create_dir([config.root_dir])
        data_transformation_config = DataTransformationConfig(
            root_dir= config.root_dir,
            data_path=config.data_path,
        )
        return data_transformation_config
    
    def get_modeltrainer_config(self)-> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN
        create_dir([config.root_dir])
        model_trainer_config = ModelTrainerConfig(
            root_dir= config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            alpha= params.alpha,
            l1_ratio = params.l1_ratio,
            target_column = schema.name 
        )
        return model_trainer_config
        
    def get_modelevaludation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        schema = self.schema.TARGET_COLUMN
        params = self.params.ElasticNet
        create_dir([config.root_dir])
        modelevaluation_config = ModelEvaluationConfig(
                root_dir= config.root_dir,
                test_data_path = config.test_data_path,
                model_path = config.model_path,
                metric_file_name = config.metric_file_name,
                all_params = params,
                mlflow_uri = self.envs["MLFLOW_TRACHING_URI"],
                target_column = schema
        )
        return modelevaluation_config