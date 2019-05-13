from gtts import gTTS
import speech_recognition as sr
import os
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
import paho.mqtt.publish as publish


import pyttsx3


def talkToMe(audio):

    print(audio)
    for line in audio.splitlines():
        engine = pyttsx3.init()
        engine.say("say"+ audio)
        engine.runAndWait()
        #os.system("say " + audio)

def currentad():

    send_url = "http://api.ipstack.com/check?access_key=9a86bc5e18df530bd1ded7ff6620187d"
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    latitude = geo_json['latitude']
    longitude = geo_json['longitude']
    return [latitude,longitude]


def myCommand():
   

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')


    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand()

    return command


def assistant(command):
    
    if 'ok' in command:
        talkToMe('how can i help you?')
        os.system('\a')
        command= myCommand()
        

        if 'open maps' in command:
            reg_ex = re.search('open maps (.*)', command)
            url = 'https://www.google.com/maps'
            if reg_ex:
                subreddit = reg_ex.group(1)
                url = url + 'r/' #+ subreddit
            webbrowser.open(url)
            print('Done!')

        elif 'open ' in command:
            reg_ex = re.search('open (.+)', command)
            if reg_ex:
                domain = reg_ex.group(1)
                url = 'https://www.' + domain
                webbrowser.open(url)
                print('Done!')
            else:
                pass

        elif 'what\'s up' in command:
            talkToMe('Just doing my thing')
        elif 'tell me a joke' in command:
            res = requests.get(
                    'https://icanhazdadjoke.com/',
                    headers={"Accept":"application/json"}
                    )
            if res.status_code == requests.codes.ok:
                talkToMe(str(res.json()['joke']))
            else:
                talkToMe('oops!I ran out of jokes')

        elif 'current weather' in command:
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
        elif 'who' in command:
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
                    g=1
    
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
                            confidence = faceMatch['Face']['Confidence']
                            f=1
                            if(g==1):
                           
                                talkToMe('this is' + str(thisdict[i].split(".jpeg")) + 'with ' + "%.2f" % confidence +' % confidence')
                                g=0
                                 
                            else:
                                talkToMe('please wait..') 
                        imageSource.close()
                        imageTarget.close()             
                    if(f!=1):
                        talkToMe('This person doesn\'t exist in our databse, what is the name of this person?: ')
                        #namee= input()+".jpeg"
                        namee= myCommand()
                        flag='no'
                        n=n+1
                        while( flag=='no'):
                            talkToMe('is this '+namee+' ?')
                            flag=myCommand()
                            if(flag=='yes' or flag=='yeah' or flag=='yea'):
                                namee= namee+ ".jpeg"
                                os.rename("test.jpeg", namee)
                                d1={n:namee}
                                thisdict.update(d1)
                    elif (f==1):
                        os.remove("test.jpeg")
                        ch='n'
        elif 'news'  in command:
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
            if __name__ == '__main__':
                NewsFromBBC()
        elif 'voice' in command:
            m=0
            command=myCommand()
                
            if('forward' in command):
                publish.single("wheeler","forward",hostname="test.mosquitto.org")
                        
            elif('backward' in command):
                publish.single("wheeler","backward",hostname="test.mosquitto.org")
            elif('left' in command):
                publish.single("wheeler","left",hostname="test.mosquitto.org")
            elif('right' in command):
                publish.single("wheeler","right",hostname="test.mosquitto.org")
            elif('stop' in command):
                publish.single("wheeler","stop",hostname="test.mosquitto.org")
                
    
                
        
        elif 'read' in command:
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
            
        
        elif 'bye' in command:
            talkToMe('See ya soon! bye    bye byebyebyee')
            exit()
    else:
            talkToMe('I don\'t know what you mean!')
            
            
    

    

talkToMe('I am ready for your command')


while True:
    '''namee= 'chair'
    test= 'ok' +namee'''
    command= myCommand()
    assistant(command)
