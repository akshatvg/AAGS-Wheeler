import boto3
import os
import cv2



camera = cv2.VideoCapture(0)
return_value, image = camera.read()
cv2.imwrite('test.jpeg', image)
del(camera)



thisdict={
    1:"akshat.jpeg",
    2:"prateek.jpeg",
    3:"anand.jpeg",
    4:"sandeep.jpeg",
    5:"goldy.jpeg"
    
    }
n=5
f=0



if __name__ == "__main__":

    sourceFile='test.jpeg'#from camera
    for i in range(1,n+1):
   # targetFile='anand.jpeg'
        targetFile= thisdict[i]
        client=boto3.client('rekognition')
   
        imageSource=open(sourceFile,'rb')
        imageTarget=open(targetFile,'rb')

        response=client.compare_faces(SimilarityThreshold=70,
                                      SourceImage={'Bytes': imageSource.read()},
                                      TargetImage={'Bytes': imageTarget.read()})
    
        for faceMatch in response['FaceMatches']:
            position = faceMatch['Face']['BoundingBox']
            confidence = str(faceMatch['Face']['Confidence'])
            f=1
            print('The face at ' +
                   str(position['Left']) + ' ' +
                   str(position['Top']) +
                   ' matches with ' + confidence + '% confidence')
            print(thisdict[i].split(".jpeg"))
        imageSource.close()
        imageTarget.close()               
    if(f!=1):
        print('This person doesn\'t exist in our databse, what is the name of this person?: ')
        namee= input()+".jpeg"
        n=n+1
        os.rename("test.jpeg", namee)
        d1={n:namee}
        thisdict.update(d1)
    elif (f==1):
        os.remove("test.jpeg")
    print(thisdict)