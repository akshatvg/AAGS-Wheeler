import boto3

s3 = boto3.resource('s3')


images=[('try.jpg','Quote'),
       ]

for image in images:
    file = open(image[0],'rb')
    object = s3.Object('s3-wheeler',image[0])
    ret = object.put(Body=file,
                    Metadata={'Name':image[1]}
                    )