# Wine Quality Prediction MLOps Pipeline

A complete end-to-end machine learning operations (MLOps) pipeline for predicting wine quality using the UCI Wine Quality dataset. This project demonstrates best practices in MLOps with automated data ingestion, validation, transformation, model training, evaluation, and deployment.

## 🍷 Project Overview

This project predicts the quality of red wine based on various physicochemical properties using an ElasticNet regression model. The system includes a web interface for real-time predictions and a complete MLOps pipeline for training and model management.

## 🏗️ Architecture

The project follows a modular MLOps architecture with the following components:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Data Ingestion │────│ Data Validation │────│Data Transformation│
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                        │
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Prediction    │────│ Model Evaluation│────│ Model Training  │
│    Pipeline     │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🚀 Features

- **Automated Data Pipeline**: Downloads and processes UCI Wine Quality dataset
- **Data Validation**: Schema validation and data quality checks
- **Model Training**: ElasticNet regression with hyperparameter tuning
- **Model Evaluation**: Comprehensive metrics and performance tracking
- **Web Interface**: User-friendly Flask web application
- **MLflow Integration**: Experiment tracking and model management
- **Docker Support**: Containerized deployment
- **Configuration Management**: YAML-based configuration system

## 📊 Dataset

The project uses the **UCI Wine Quality Dataset** (Red Wine) with the following features:

- **Fixed Acidity**: Tartaric acid content
- **Volatile Acidity**: Acetic acid content
- **Citric Acid**: Citric acid content
- **Residual Sugar**: Sugar content after fermentation
- **Chlorides**: Salt content
- **Free Sulfur Dioxide**: SO2 content
- **Total Sulfur Dioxide**: Total SO2 content
- **Density**: Wine density
- **pH**: Acidity/alkalinity level
- **Sulphates**: Potassium sulphate content
- **Alcohol**: Alcohol percentage

**Target**: Wine quality score (0-10)

## 🛠️ Technologies Used

- **Python 3.x**: Core programming language
- **Flask**: Web framework for the prediction interface
- **scikit-learn**: Machine learning library
- **MLflow**: ML lifecycle management
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **matplotlib**: Data visualization
- **Docker**: Containerization
- **YAML**: Configuration management

## 📁 Project Structure

```
├── app.py                          # Flask web application
├── main.py                         # Main pipeline execution
├── requirements.txt                # Python dependencies
├── Dockerfile                      # Docker configuration
├── config/
│   └── config.yaml                # Main configuration file
├── params.yaml                     # Model parameters
├── schema.yaml                     # Data validation schema
├── src/
│   └── data_science/
│       ├── components/             # Core ML components
│       │   ├── dataingestion.py
│       │   ├── datavalidation.py
│       │   ├── datatransformation.py
│       │   ├── modeltrainer.py
│       │   └── modelevaluation.py
│       ├── pipeline/               # ML pipelines
│       │   ├── dataingestionpipeline.py
│       │   ├── datavalidationpipeline.py
│       │   ├── datatransformationpipeline.py
│       │   ├── modeltraainerpipeline.py
│       │   ├── modelevaluaationpipeline.py
│       │   └── predictionpipeline.py
│       ├── config/                 # Configuration management
│       ├── entity/                 # Data entities
│       └── utils/                  # Utility functions
├── templates/                      # HTML templates
├── research/                       # Jupyter notebooks
└── artifacts/                      # Generated artifacts
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip package manager
- Git

### Installation

1. **Clone the repository**:
```bash
git clone <repository-url>
cd <repository-name>
```

2. **Create and activate virtual environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

### Running the Application

#### Option 1: Complete Pipeline Training + Web App

```bash
# Run the complete ML pipeline
python main.py

# Start the Flask web application
python app.py
```

#### Option 2: Direct Web App (using pre-trained model)

```bash
python app.py
```

The web application will be available at `http://localhost:5000`

### Using Docker

```bash
# Build Docker image
docker build -t wine-quality-app .

# Run container
docker run -p 5000:5000 wine-quality-app
```

## 📈 Usage

### Web Interface

1. Navigate to `http://localhost:5000`
2. Enter wine characteristics in the form
3. Click "Predict Quality" to get the prediction
4. View results on the results page

### API Endpoints

- `GET /`: Homepage with prediction form
- `POST /predict`: Submit wine characteristics for prediction
- `GET /train`: Trigger model retraining

### Training Pipeline

The training pipeline can be executed programmatically:

```python
from src.data_science.pipeline.dataingestionpipeline import DataIngestionTrainingPipeline
from src.data_science.pipeline.datavalidationpipeline import DataValidationTrainingPipeline
# ... other imports

# Run individual pipeline stages
data_ingestion = DataIngestionTrainingPipeline()
data_ingestion.initiate_data_ingestion()

# Or run the complete pipeline
python main.py
```

## ⚙️ Configuration

### Model Parameters (params.yaml)

```yaml
ElasticNet:
  alpha: 0.2      # Regularization strength
  l1_ratio: 0.1   # ElasticNet mixing parameter
```

### Pipeline Configuration (config/config.yaml)

The configuration file contains paths and settings for each pipeline stage:

- Data ingestion source URL
- Artifact storage locations
- Model parameters
- File paths and directories

## 📊 Model Performance

The model uses ElasticNet regression with the following characteristics:

- **Algorithm**: ElasticNet (combines L1 and L2 regularization)
- **Hyperparameters**: Alpha=0.2, L1_ratio=0.1
- **Evaluation Metrics**: Stored in `artifacts/model_evaluation/metric.json`

## 🔍 Research and Development

Jupyter notebooks for research and experimentation are available in the `research/` directory:

- `1-dataingestion.ipynb`: Data ingestion exploration
- `2-datavalidation.ipynb`: Data validation experiments
- `3-datatransformation.ipynb`: Data transformation analysis
- `4-model Trainer.ipynb`: Model training experiments
- `5-model_evaludation.ipynb`: Model evaluation analysis

## 🐳 Docker Deployment

The project includes Docker support for easy deployment:

```bash
# Build the image
docker build -t wine-quality-predictor .

# Run the container
docker run -p 5000:5000 wine-quality-predictor
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- UCI Machine Learning Repository for the Wine Quality dataset
- The open-source community for the amazing tools and libraries
- MLflow for experiment tracking capabilities

## 📞 Support

For questions or issues, please open an issue in the repository or contact the maintainers.

---

**Built with ❤️ for the MLOps community**