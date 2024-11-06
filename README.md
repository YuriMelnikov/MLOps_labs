MLOps_Labs

## Setup

1. Установить зависимости через Poetry:

   ```bash
   poetry install

   ```

2. Запустить контейнер Docker с minio:

   ```bash
   docker-compose up -d

   ```

3. Установить права доступа:

   ```bash
   chmod +x mlops_labs/lab3/shell/*.sh pipeline.sh

   ```

4. Установить pre-commit:

   ```bash
   pre-commit install

   ```

5. Запустить pipeline.sh:

   ```bash
   ./pipeline.sh

   ```

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

==============================

Performing laboratory work on MLOps

## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── mlops_labs            <- Main project directory for MLOps tasks and labs.
    │   └── lab3/
    │       ├── __init__.py    <- Initialization file to make `lab3` a Python package.
    │       │
    │       ├── data/
    │       │   ├── titanic.csv             <- Raw titanic dataset for processing and transformations.
    │       │   └── transformed_titanic.csv <- Processed dataset after transformations.
    │       │
    │       ├── scripts/                   <- Python scripts for specific ETL and data handling steps.
    │       │   ├── download_from_s3.py    <- Script for downloading data from an S3-compatible storage.
    │       │   ├── transform_data.py      <- Script for transforming the titanic dataset as part of the ETL pipeline.
    │       │   ├── upload_to_s3.py        <- Script to upload the initial dataset to S3 storage.
    │       │   └── upload_transformed_data.py <- Script to upload the transformed dataset back to S3.
    │       │
    │       └── shell/                    <- Shell scripts for individual ETL steps and data pipeline operations.
    │           ├── extract.sh            <- Script for extracting data as part of the ETL process.
    │           ├── first_load.sh         <- Script to perform initial data load to S3.
    │           ├── load.sh               <- Script for loading data into the final destination.
    │           └── transform.sh          <- Script for data transformation tasks.
    │
    ├── docker-compose.yaml    <- Docker Compose configuration for setting up services like MinIO for local S3 storage.
    │
    ├── pipeline.sh            <- Main shell script for running the full ETL pipeline, calling the scripts in sequence.
    │
    ├── pyproject.toml         <- Poetry configuration file, managing dependencies and project metadata.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

---

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
