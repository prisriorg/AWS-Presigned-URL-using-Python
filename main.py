import boto3
from botocore.client import Config
import os

def create_presigned_url_e2(bucket_name, object_name, access_key, secret_key, endpoint_url, expiration=36000):
    
    
    # Create a session with iDrive e2 credentials
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )

    # Initialize the S3 client with the iDrive e2 endpoint
    s3_client = session.client(
        's3',
        endpoint_url=endpoint_url
    )
    
    try:
        # Generate the presigned URL
        # response = s3_client.generate_presigned_url('put_object',
                                                    # Params={'Bucket': bucket_name, 'Key': object_name},
                                                    # ExpiresIn=expiration)
        current_directory = os.getcwd()
        download_path = os.path.join(current_directory, object_name)
        response = s3_client.download_file(bucket_name, object_name, download_path)
    except Exception as e:
        print(f"Error generating presigned URL: {e}")
        return None

    return response

# Example usage
bucket_name = 'your_bucket_name'
object_name = 'your-filename'
access_key = 'your-access-key'
secret_key = 'your-secret-key'
endpoint_url = 'your-endpoint-url'
url = create_presigned_url_e2(bucket_name, object_name, access_key, secret_key, endpoint_url)

if url:
    print(f'Presigned URL: {url}')
