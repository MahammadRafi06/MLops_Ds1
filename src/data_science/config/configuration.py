from src.data_science.constants import CONFIG_FILE_PATH, SCHEMA_FILE_PATH, PARAMS_FILE_PATH
from src.data_science.utils.common import read_yaml, create_dir
from src.data_science.entity.config_entity import (DataIngestionConfig)
class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, schema_file_path= SCHEMA_FILE_PATH, params_file_path=PARAMS_FILE_PATH ):
        
        self.config = read_yaml(CONFIG_FILE_PATH)
        self.params = read_yaml(PARAMS_FILE_PATH)
        self.schema = read_yaml(PARAMS_FILE_PATH)
        
        create_dir([self.config.artifacts_toot])
        
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