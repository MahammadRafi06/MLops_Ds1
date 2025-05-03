from urllib import request
from src.data_science import logger
import zipfile
import os 
from src.data_science.entity.config_entity import (DataIngestionConfig)
from src.data_science.config.configuration import (ConfigurationManager)
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,header = request.urlretrieve(url=self.config.source_URL, filename=self.config.local_data_file)
            logger.info(f"{self.config.local_data_file} downloaded") 
        else: 
            logger.info(f"{self.config.local_data_file} already exists and size if {os.path.getsize(self.config.local_data_file)}")
    def extract_zipfile(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file) as zip_ref:
            zip_ref.extractall(unzip_path)
            
