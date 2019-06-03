from gtts import gTTS
import speech_recognition as sr
import os
import pyttsx3
import re
import webbrowser
import smtplib
import requests,json
import urllib
import boto3
import os
import cv2
from pyzomato import Pyzomato
p= Pyzomato('263457c3373e779946164cef05a88eb0')

def talkToMe(audio):

    print(audio)
    for line in audio.splitlines():
        engine = pyttsx3.init()
        engine.say("say"+ audio)
        engine.runAndWait()
        os.system("say " + audio)

def currentad():

    send_url = "http://api.ipstack.com/check?access_key=9a86bc5e18df530bd1ded7ff6620187d"
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    latitude = geo_json['latitude']
    longitude = geo_json['longitude']
    return [latitude,longitude]


def myCommand():
   
    import ibm_watson
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening..')
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        if 'villa' in command:
            command='okay wheeler'
        print('You said: ' + command + '\n')

        assistant = ibm_watson.AssistantV1(
            version='2019-02-28',
            iam_apikey='u1N9ThXmpZUk_-1_F1AaAw-11BbBXFtCbonmmerHbnFI',
            url='https://gateway-wdc.watsonplatform.net/assistant/api'
        )

        response = assistant.message(
            workspace_id='7cb1c0fc-6e91-4b63-9e93-8a30028bd58e',
            input={
                'text': command
            }
        ).get_result()


        a=response
        b=a['intents']
        if b==[]:
            intent= 'nothing'
        else:
            intent = b[0]['intent']
        


    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        intent = myCommand()

    return intent


def assistant(intent):
    
    if intent=='greeting': # if intent =='greeting':
        talkToMe('how can i help you?')
        os.system('\a')
        intent= myCommand()
        

        if intent=='maps':
            reg_ex = re.search('open maps (.*)', command)
            url = 'https://www.google.com/maps'
            if reg_ex:
                subreddit = reg_ex.group(1)
                url = url + 'r/' #+ subreddit
            webbrowser.open(url)
            print('Done!')

        elif intent=='open':
            reg_ex = re.search('open (.+)', command)
            if reg_ex:
                domain = reg_ex.group(1)
                url = 'https://www.' + domain
                webbrowser.open(url)
                print('Done!')
            else:
                pass

        
        elif intent=='joke':
            res = requests.get(
                    'https://icanhazdadjoke.com/',
                    headers={"Accept":"application/json"}
                    )
            if res.status_code == requests.codes.ok:
                talkToMe(str(res.json()['joke']))
            else:
                talkToMe('oops!I ran out of jokes')

        elif intent=='weather':
            '''reg_ex = re.search('current weather in (.*)', command)
            if reg_ex:
                city = reg_ex.group(1)#give name
                weather = Weather()
                location = weather.lookup_by_location(city)
                condition = location.condition()
                #print((city, condition.text(), (int(condition.temp())-32)/1.8))
                talkToMe('The Current weather in %s is %s The tempeture is %.1f degree' % (city, condition.text(), (int(condition.temp())-32)/1.8))'''
            latt,long = currentad()
            endpoint = 'http://api.openweathermap.org/data/2.5/forecast?'
            api_key = 'e33c84cc9eb1157c533611a494f638a3'

            nav_request = 'lat={}&lon={}&APPID={}'.format(latt, long, api_key)
            request = endpoint + nav_request
            # Sends the request and reads the response.
            response = urllib.request.urlopen(request).read().decode('utf-8')
                # Loads response as JSON
            weather = json.loads(response)
            current_temp = weather['list'][0]['main']['temp']
            temp_c = current_temp - 273.15
            temp_c_str = str(int(temp_c)) + ' degree Celsius '
            descript_place = weather['list'][0]['weather'][0]['main']
            #print(descript_place + ' ' + temp_c_str)
            talkToMe('The Current weather is '+descript_place + ' and temperature is ' + temp_c_str)
        elif intent=='person':
            thisdict={
            1:"akshat.jpeg",
            2:"prateek.jpeg",
            3:"anshu.jpeg",
            4:"sandeep.jpeg",
            5:"goldy.jpeg"
    
                }
            n=5
            f=0

            ch='y'
            chcounter=0
            if __name__ == "__main__":
                while(ch=='y'):
    
                    camera = cv2.VideoCapture(0)
                    return_value, image = camera.read()
                    cv2.imwrite('test.jpeg', image)
                    del(camera)


                    sourceFile='test.jpeg'#from camera
                    for i in range(1,n+1):
       # targetFile='anand.jpeg'
                        targetFile= thisdict[i]
                        client=boto3.client('rekognition')

                        imageSource=open(sourceFile,'rb')
                        imageTarget=open(targetFile,'rb')

                        response=client.compare_faces(SimilarityThreshold=70,SourceImage={'Bytes': imageSource.read()},TargetImage={'Bytes': imageTarget.read()})

                        for faceMatch in response['FaceMatches']:
                            position = faceMatch['Face']['BoundingBox']
                            confidence = str(faceMatch['Face']['Confidence'])
                            f=1
                            talkToMe('The face at ' +
                                   str(position['Left']) + ' ' +
                                   str(position['Top']) +
                                   ' matches with ' + confidence + '% confidence')
                            talkToMe(str(thisdict[i].split(".jpeg")))
                        imageSource.close()
                        imageTarget.close()               
                    if(f!=1):
                        talkToMe('This person doesn\'t exist in our databse, what is the name of this person?: ')
                        #namee= input()+".jpeg"
                        namee= myCommand()
                        namee= namee+ ".jpeg"
                        n=n+1
                        os.rename("test.jpeg", namee)
                        d1={n:namee}
                        thisdict.update(d1)
                    elif (f==1):
                        os.remove("test.jpeg")
                        ch='n'
        elif intent=='text':
            camera = cv2.VideoCapture(0)
            return_value, image = camera.read()
            cv2.imwrite('test1.jpeg', image)
            del(camera)
        
            s3 = boto3.resource('s3')
            images=[('test1.jpeg','test'),]

            for image in images:
                file = open(image[0],'rb')
                object = s3.Object('s3-wheeler',image[0])
                ret = object.put(Body=file,
                                    Metadata={'Name':image[1]}
                                    )


            if __name__ == "__main__":

                bucket='s3-wheeler'
                photo='test1.jpeg'
                client=boto3.client('rekognition')
                response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
                textDetections=response['TextDetections']
   
    
                for text in textDetections:
                    if(' ' in text['DetectedText']):
                        talkToMe(str(text['DetectedText']))



            s3.Object('s3-wheeler', 'test1.jpeg').delete()

       
        elif intent=='news':
            def NewsFromBBC():
                main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=e4313a22f54042c9aba095ce5354be51"
                open_bbc_page = requests.get(main_url).json() 
                article = open_bbc_page["articles"] 
                results = []
                talkToMe('The top headlines are,') 
                for ar in article:
                    results.append(ar["title"]) 
                    
                for i in range(0,3):
                    stuff= str((i+1)) +' '+ results[i]
                    talkToMe(stuff)
            NewsFromBBC()
            
    elif intent=='bye':
        talkToMe('See ya soon! bye    bye byebyebyee')
        exit()

    else:
        talkToMe('did not catch that, please repeat yourself')

    

talkToMe('Hi! i am Wheeler, your virtual assistant. start with \'okay wheeler\' ')


while True:
    '''namee= 'chair'
    test= 'ok' +namee'''
    intent= myCommand()
    assistant(intent)

