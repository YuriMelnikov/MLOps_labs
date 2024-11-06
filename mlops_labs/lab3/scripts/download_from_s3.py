import boto3
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


def download_from_s3(client, bucket, filename, download_path):
    try:
        response = client.get_object(Bucket=bucket, Key=filename)
        with open(download_path, "wb") as f:
            f.write(response["Body"].read())
        print(f"Successfully downloaded {filename} from {bucket} to {download_path}")
    except Exception as e:
        print(f"Failed to download from S3: {str(e)}")


if __name__ == "__main__":
    client = create_s3_client()
    bucket_name = "mybucket"
    create_bucket_if_not_exists(client, bucket_name)

    object_name = "titanic.csv"
    download_path = "./mlops_labs/lab3/data/titanic.csv"
    download_from_s3(client, bucket_name, object_name, download_path)
