import boto3
from decimal import Decimal
import json
import urllib

BUCKET = "wheeler-aags"
KEY = "akshat1.jpg"
IMAGE_ID = KEY # S3 key as ImageId
COLLECTION = "wheeler_aags"

dynamodb = boto3.client('dynamodb', "ap-south-1")
s3 = boto3.client('s3')


#rekognition.create_collection(CollectionId=COLLECTION)

def update_index(tableName,faceId, fullName):
	response = dynamodb.put_item(
	TableName="wheeler_aags",
	Item={
		'RekognitionId': {'S': faceId},
		'FullName': {'S': fullName}
		}
	)
	print(response)
def index_faces(bucket, key, collection_id, image_id=None, attributes=(), region="ap-south-1"):
	rekognition = boto3.client("rekognition", region)
	response = rekognition.index_faces(
		Image={
			"S3Object": {
				"Bucket": bucket,
				"Name": key,
			}
		},
		CollectionId=collection_id,
		ExternalImageId="akshat",
	    DetectionAttributes=attributes,
	)
	if response['ResponseMetadata']['HTTPStatusCode'] == 200:
		faceId = response['FaceRecords'][0]['Face']['FaceId']
		print(faceId)
		ret = s3.head_object(Bucket=bucket,Key=key)
		personFullName = ret['Metadata']['fullname']
		#print(ret)
		print(personFullName)
		update_index('wheeler_aags',faceId,personFullName)

	# Print response to console.
	print(response)
	return response['FaceRecords']


for record in index_faces(BUCKET, KEY, COLLECTION, IMAGE_ID):
	face = record['Face']
	# details = record['FaceDetail']
	print( "Face ({}%)".format(face['Confidence']))
	print("  FaceId: {}".format(face['FaceId']))
	print( "  ImageId: {}".format(face['ImageId']))