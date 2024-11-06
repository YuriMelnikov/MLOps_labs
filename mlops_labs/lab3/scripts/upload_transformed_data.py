import boto3
import os
from botocore.exceptions import ClientError

MINIO_ENDPOINT = "http://localhost:9000"
MINIO_ROOT_USER = "YuriMelnikov"
MINIO_ROOT_PASSWORD = "admin1234"


def create_s3_client():
    return boto3.client(
        "s3",
        endpoint_url=MINIO_ENDPOINT,
        aws_access_key_id=MINIO_ROOT_USER,
        aws_secret_access_key=MINIO_ROOT_PASSWORD,
    )


def create_bucket_if_not_exists(client, bucket_name):
    try:
        client.head_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' already exists.")
    except ClientError as e:
        if e.response["Error"]["Code"] == "404":
            client.create_bucket(Bucket=bucket_name)
            print(f"Bucket '{bucket_name}' created successfully.")
        else:
            print(f"Failed to check/create bucket: {e}")
            raise


def upload_to_s3(client, bucket_name, file_path, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_path)
    try:
        client.upload_file(file_path, bucket_name, object_name)
        print(f"Uploaded {file_path} to bucket {bucket_name} as {object_name}.")
    except Exception as e:
        print(f"Failed to upload transformed data to S3: {e}")


if __name__ == "__main__":
    client = create_s3_client()
    bucket_name = "mybucket"
    create_bucket_if_not_exists(client, bucket_name)

    file_path = "./mlops_labs/lab3/data/transformed_titanic.csv"
    upload_to_s3(client, bucket_name, file_path, object_name="transformed_titanic.csv")
