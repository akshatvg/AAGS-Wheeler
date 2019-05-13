import boto3

if __name__ == "__main__":

    bucket='wheeler-aags'
    collectionId='MyCollection'
    fileName='akshat1.png'
    threshold = 70
    maxFaces=2

    client=boto3.client('rekognition')

  
    response=client.search_faces_by_image(CollectionId=collectionId,Image={'S3Object':{'Bucket':bucket,'Name':fileName}},FaceMatchThreshold=threshold,MaxFaces=maxFaces)

                                
    faceMatches=response['FaceMatches']
    print ('Matching faces')
    for match in faceMatches:
            print ('FaceId:' + match['Face']['FaceId'])
            print ('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")