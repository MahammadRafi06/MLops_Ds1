import os
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from src.data_science.entity.config_entity import ModelEvaluationConfig
from src.data_science.utils.common import save_json
from pathlib import Path
from src.data_science import logger
class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def evalauation_metric(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    
    def model_evaluation(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        test_x = test_data.drop(columns=[self.config.target_column.name], axis=1)
        test_y = test_data[self.config.target_column.name]
        
        mlflow.set_tracking_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        logger.info(f"uri is is {self.config.mlflow_uri}: uri type is {tracking_url_type_store}")
        with mlflow.start_run():
            predicted_qualities = model.predict(test_x)
            rmse, mae, r2 = self.evalauation_metric(test_y, predicted_qualities)
            
            scores = {"rmse":rmse, "mae":mae, "r2":r2}
            
            save_json(path=Path(self.config.metric_file_name), data=scores)
            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse",rmse)
            mlflow.log_metric("mae",mae)
            mlflow.log_metric("r2",r2)
            
            tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme
            
            if tracking_uri_type_store != "file":
                mlflow.sklearn.log_model(model, "model1", registered_model_name="Best ElaticNet", input_example=test_x)
            else:
                mlflow.sklearn.log_model(model, "model1")