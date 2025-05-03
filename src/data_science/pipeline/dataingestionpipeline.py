from src.data_science.config.configuration import (ConfigurationManager)
from src.data_science.entity.config_entity import (DataIngestionConfig)
from src.data_science import logger
from src.data_science.components.dataingestion import DataIngestion

try:
    config = ConfigurationManager()
    data_ingestion_config = config.get_dataingestion_config()
    data_ingestion = DataIngestion(data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.extract_zipfile()
except Exception as e:
    raise e 


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def initiate_data_ingestion(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_dataingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zipfile()
