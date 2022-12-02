import boto3
import urllib.parse

def lambda_handler(event, context):
	src_bucket_name = urllib.parse.unquote(event['Records'][0]['s3']['bucket']['name'])
	src_bucket_objkey = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
	
	destination_bucket = 'shanbackup-s3bucket1'
	copy_source = {'Bucket': src_bucket_name, 'Key': src_bucket_objkey }
	s3 = boto3.client('s3')
	s3.copy_object(Bucket=destination_bucket, Key=src_bucket_objkey, CopySource=copy_source)
	
