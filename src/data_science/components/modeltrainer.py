from src.data_science import logger
import pandas as pd
from sklearn.linear_model import ElasticNet
import joblib
import os
from src.data_science.entity.config_entity import ModelTrainerConfig
class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    
    def model_training(self):
        train_data = pd.read_csv(self.config.train_data_path, sep=",")
        test_data = pd.read_csv(self.config.test_data_path, sep=",")
        train_x = train_data.drop(columns=[self.config.target_column], axis=1)
        train_y = train_data[self.config.target_column]
        test_x = test_data.drop(columns=[self.config.target_column], axis=1)
        test_y = test_data[self.config.target_column]
        logger.info(f"Training Starting")
        model = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        model.fit(train_x, train_y)
        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))
        logger.info(f"Model saved to {os.path.join(self.config.root_dir, self.config.model_name)}")
        