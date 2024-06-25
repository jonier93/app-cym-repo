import boto3
from credentials.keys import ACCESS_KEY, SECRET_KEY

def connection_s3():
    try:
        session_aws = boto3.session.Session(ACCESS_KEY, SECRET_KEY)
        s3_resource = session_aws.resource('s3')
        print("Connecting to S3")
    except Exception as err:
        print("Error", err)

def save_file(photo):
    try:
        photo_path = "/tmp/photo.JPG"
        photo.save(photo_path)
        print("Photo saved")
    except Exception as err:
        print("Error", err)
        