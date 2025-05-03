from src.data_science import logger
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from src.data_science.entity.config_entity import DataTransformationConfig
class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path, sep=";")
        train,test = train_test_split(data, test_size=.2)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        
        logger.info("Splitted data into train and test")
        logger.info(f"number of records in training data : {train.shape[0]}")
        logger.info(f"number of records in test data : {test.shape[0]}")
        
        print( f"number of records in training data : {train.shape[0]}")
        print( f"number of records in test data : {test.shape[0]}")
    