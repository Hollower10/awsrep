from boto3.session import Session
from keys import ACCESS_KEY, SECRET_KEY



def conect_s3():
    session_aws= Session(ACCESS_KEY, SECRET_KEY)
    session_s3= session_aws.resource('s3')
    print("success")