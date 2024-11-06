#!/bin/bash
echo "Starting the ETL pipeline..."

# Шаг 1: Загрузка исходного набора данных в S3
echo "Step 1: Uploading raw dataset to S3..."
bash ./mlops_labs/lab3/shell/first_load.sh

# Шаг 2: Извлечение данных из S3
echo "Step 2: Downloading dataset from S3..."
bash ./mlops_labs/lab3/shell/extract.sh

# Шаг 3: Трансформация данных
echo "Step 3: Transforming dataset..."
bash ./mlops_labs/lab3/shell/transform.sh

# Шаг 4: Загрузка обработанных данных в S3
echo "Step 4: Uploading transformed dataset to S3..."
bash ./mlops_labs/lab3/shell/load.sh

echo "ETL pipeline completed successfully."
