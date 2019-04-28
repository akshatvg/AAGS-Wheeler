import boto3

BUCKET = "wheeler-aags"
KEY = "akshat1.png"
collectionId='MyCollection'
	
client=boto3.client('rekognition')

    #Create a collection
print('Creating collection:' + collectionId)
#response=client.create_collection(CollectionId=collectionId)

def search_faces_by_image(bucket, key, collection_id, threshold=80, region="ap-south-1"):
	rekognition = boto3.client("rekognition", region)
	response = rekognition.search_faces_by_image(
		Image={
			"S3Object": {
				"Bucket": "wheeler-aags",
				"Name": "akshat1.png",
			}
		},
		CollectionId=collection_id,
		FaceMatchThreshold=threshold,
	)
	return response['FaceMatches']

for record in search_faces_by_image(BUCKET, KEY, collectionId):
	face = record['Face']
	print( "Matched Face ({}%)".format(record['Similarity']))
	print( "  FaceId : {}".format(face['FaceId']))
	print ("  ImageId : {}".format(face['ExternalImageId']))
