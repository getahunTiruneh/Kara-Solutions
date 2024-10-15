# Ethiopian Medical Businesses Data Warehouse
This GitHub repository features a project to build a data warehouse for Ethiopian medical business data scraped from the web and Telegram channels. It includes data scraping, cleaning, object detection using YOLO, and implementing ETL/ELT processes to enable efficient analysis and insights.

## Core Objectives

- **Data Centralization**: Collect and store data from multiple sources, including Telegram channels.
- **Efficient Data Processing**: Implement ETL/ELT frameworks for structured and unstructured data.
- **Object Detection Integration**: Use YOLOv5 for object detection in images.
- **Data Quality Assurance**: Ensure data accuracy and cleanliness using DBT.
  
## Project structure

The repository is organized into the following directories:

- **.github/workflows/**: Contains configuration files for GitHub Actions, facilitating continuous integration (CI) and automated testing workflows to ensure code quality.

- **.vscode/**: Configuration files for Visual Studio Code, optimizing the development environment and providing settings specific to this project.

- **Fast_API/**: Houses the implementation of the machine learning model API, enabling interaction with the model through RESTful endpoints. This is where the core business logic and model serving reside.
  
- **Kara_dbt/**: Contains the DBT (Data Build Tool) project files, including models, seeds, and configurations for transforming and documenting the data in the data warehouse. This directory supports the implementation of data quality assurance and transformation processes.

- **notebooks/**: Contains Jupyter notebooks utilized for data exploration, feature engineering, and preliminary modeling. These notebooks serve as documentation for the analytical processes and insights gained throughout the project.

- **scripts/**: Includes Python scripts for data preprocessing, feature extraction, and the implementation of the credit scoring model. This directory contains reusable code components that streamline data handling and modeling processes.

- **tests/**: Comprises unit tests designed to ensure the correctness and robustness of the implemented model and data processing logic. This directory is crucial for maintaining code quality and facilitating future development.

- **requirements.txt**: A file listing the dependencies and libraries required for the project, making it easier to set up the environment.

- **README.md**: The main documentation file that provides an overview of the project, installation instructions, usage guidelines, and other essential information.


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
