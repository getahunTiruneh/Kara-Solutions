# Ethiopian Medical Businesses Data Warehouse
This GitHub repository features a project to build a data warehouse for Ethiopian medical business data scraped from the web and Telegram channels. It includes data scraping, cleaning, object detection using YOLO, and implementing ETL/ELT processes to enable efficient analysis and insights.

## Core Objectives

- **Data Centralization**: Collect and store data from multiple sources, including Telegram channels.
- **Efficient Data Processing**: Implement ETL/ELT frameworks for structured and unstructured data.
- **Object Detection Integration**: Use YOLOv5 for object detection in images.
- **Data Quality Assurance**: Ensure data accuracy and cleanliness using DBT.
  
## Project structure

he repository is organized into the following directories:

- **.github/workflows/**: Configuration files for GitHub Actions to enable continuous integration (CI) and automated testing.

- **.vscode/**: Visual Studio Code configuration files for optimizing the development environment.

- **Fast_API/**: Implementation of the machine learning model API, providing RESTful endpoints for model interaction.

- **Kara_dbt/**: DBT (Data Build Tool) project files for data transformation and documentation, ensuring data quality.

- **database/**: Scripts and configurations for managing PostgreSQL connections and interactions.

- **notebooks/**: Jupyter notebooks for data exploration, feature engineering, and preliminary modeling.

- **scripts/**: Python scripts for data preprocessing, feature extraction, and credit scoring model implementation.

- **tests/**: Unit tests to ensure the correctness and robustness of the model and data processing logic.

- **requirements.txt**: Lists dependencies and libraries required for the project setup.

- **README.md**: Main documentation file with an overview of the project, installation instructions, and usage guidelines.


## Installation Instructions

### Setting Up the Environment
Ensure you have the necessary dependencies installed:

```bash
# Install essential libraries
pip install opencv-python
pip install torch torchvision  # for PyTorch-based YOLO
pip install tensorflow          # for TensorFlow-based YOLO
pip install fastapi uvicorn     # for FastAPI
pip install dbt                 # for data transformation
```

1. Clone the Repository:
>>>>
    git clone https://github.com/getahunTiruneh/Kara-Solutions.git`

    cd Kara-Solutions
>>>>

2. Set up the Virtual Environment:

Create a virtual environment to manage the project's dependencies:

**For Windows: bash**

>>>
    python3 -m venv .venv

    source .venv/Scripts/activate  
>>>


3. Install Dependencies:

Install the required Python packages by running:
>>>
    pip install -r requirements.txt
>>>
## Tasks

- **Task 1**: Scraping Data from Telegram Channels
- **Task 2**: Data Transformation using DBT
- **Task 3**: Object Detection using YOLO
- **Task 4**: FastAPI Integration

## Contributing
 We welcome contributions to improve the project. Please follow the steps below to contribute:

- Fork the repository.
- Create a new branch for your feature or bugfix.
- Submit a pull request with a detailed explanation of your changes.
