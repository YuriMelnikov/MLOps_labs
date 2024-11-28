#!/bin/bash

poetry run python mlops_labs/lab4/src/modeling/train.py --data-path mlops_labs/lab4/data/processed/preprocessed_data.csv --params mlops_labs/lab4/configs/hyperparams.yaml
