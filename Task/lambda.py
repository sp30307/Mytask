import boto3
import urllib.parse
#This function is used for copying file from source bucket to destination
def lambda_handler(event, context):
	source_bucket_name = urllib.parse.unquote(event['Records'][0]['s3']['bucket']['name'])
	source_bucket_objkey = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
	
	destination_bucket_name = 'shanbackup-s3bucket1'
	copy_source = {'Bucket': source_bucket_name, 'Key': source_bucket_objkey }
	s3 = boto3.client('s3')
	s3.copy_object(Bucket=destination_bucket_name, Key=source_bucket_objkey, CopySource=copy_source)
	
