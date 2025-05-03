from src.data_science import logger
import pandas as pd
from src.data_science.entity.config_entity import(DataValidationConfig)
class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validate_all_columns(self):
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir, sep=";")
            all_cols = list(data.columns)
            all_types = {k:str(v) for k,v in data.dtypes.to_dict().items()}
            all_schema = self.config.all_schema
            for col,type in all_schema.items():
                if (col not in all_cols) or type != all_types[col]  :
                    validation_status = False
                    logger.info(f"Missing column {col} in input file or column type mismatch")
                    with open(self.config.STATUS_FILE, "w+") as f:
                        f.write(f" Issue with {col} in input data, setting Validation Status:{validation_status}")
                    break
            else:
                validation_status = True
                with open(self.config.STATUS_FILE, "w+") as f:
                    f.write(f"Validation Sucessful. Validation Status:{validation_status}")
                    logger.info(f"Input file passed validation")
        except Exception as e:
            raise e