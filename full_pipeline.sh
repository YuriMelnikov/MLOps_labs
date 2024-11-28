#!/bin/bash

bash docker-compose up -d

bash poetry install

bash chmod +x ./mlops_labs/lab4/src/modeling/shell/*.sh pipeline_final.sh preparation.sh src/shell/*.sh

bash ./mlops_labs/lab4/src/modeling/shell/first_load.sh

bash ./mlops_labs/lab4/src/modeling/shell/extract.sh

bash ./mlops_labs/lab4/src/modeling/shell/preprocess.sh

bash ./mlops_labs/lab4/src/modeling/shell/upload.sh
