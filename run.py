from flask import Flask, flash, redirect, render_template, url_for, request
from flask_cors import CORS
import ibm_watson
from gtts import gTTS
import os
import re
import webbrowser
import smtplib
import requests,json
import urllib
import boto3
import os
import subprocess
import cv2
import googlemaps
from datetime import datetime
import analyze as az
from opencage.geocoder import OpenCageGeocode

  



#import assistant


app = Flask(__name__)

CORS(app)# to let the webapp know that this backend is ready to accept stuff.

@app.route('/')
def home():
    return render_template ('index.html')
@app.route('/useme.html')
def useme():
    return render_template ('useme.html')
@app.route('/map.html')
def map():
    return render_template ('map.html', value=value,loc=loc)
@app.route('/print/name', methods=['POST', 'GET'])
def get_names():

    if request.method == 'POST':
        resp_json = request.get_json()
        command = resp_json['text']
        if 'villa' in command or 'billa' in command:
            command= 'okay wheeler'
        else:
            command= command
    #print('You said: ' + command + '\n')
    assistant = ibm_watson.AssistantV1(
    version='2019-02-28',
    iam_apikey='u1N9ThXmpZUk_-1_F1AaAw-11BbBXFtCbonmmerHbnFI',
    url='https://gateway-wdc.watsonplatform.net/assistant/api'
    )

    response = assistant.message(
        workspace_id='7cb1c0fc-6e91-4b63-9e93-8a30028bd58e',
        input={
            'text': command #use the <text> we get with flask
        }
    ).get_result()


    a=response
    b=a['intents']
    if b==[]:
        intent= 'nothing'
    else:
        intent = b[0]['intent']
    print('the intent is:' , intent)
    def currentad():
        send_url = "http://api.ipstack.com/check?access_key=9a86bc5e18df530bd1ded7ff6620187d"
        geo_req = requests.get(send_url)
        geo_json = json.loads(geo_req.text)
        latitude = geo_json['latitude']
        longitude = geo_json['longitude']
        return [latitude,longitude]
    if intent=='weather':
        latt,long = currentad()
        endpoint = 'http://api.openweathermap.org/data/2.5/forecast?'
        api_key = 'e33c84cc9eb1157c533611a494f638a3'

        nav_request = 'lat={}&lon={}&APPID={}'.format(latt, long, api_key)
        reequest = endpoint + nav_request
        # Sends the request and reads the response.
        response = urllib.request.urlopen(reequest).read().decode('utf-8')
            # Loads response as JSON
        weather = json.loads(response)
        current_temp = weather['list'][0]['main']['temp']
        temp_c = current_temp - 273.15
        temp_c_str = str(int(temp_c)) + ' degree Celsius '
        descript_place = weather['list'][0]['weather'][0]['main']
        #print(descript_place + ' ' + temp_c_str)
        if descript_place == 'Clouds':
            descript_place = 'overcast'
        print('It is a little '+descript_place + ' and temperature outside is, ' + temp_c_str)
        
       #response = assistant.assistant(resp_json["test"])
        return json.dumps({"response": 'It is a little '+descript_place + ' and temperature outside is, ' + temp_c_str}), 200

    elif intent=='maps':
        #webbrowser.open('http:127.0.0.1:5000/map.html')
        #print('Done!')
        gmaps = googlemaps.Client(key='AIzaSyAMP6SIK4ruB5Tsl5qR6h54XDcl4FDl3HQ')
        SUBSCRIPTION_KEY_ENV_NAME = "bc20ced3c3014badbf34d1799e28f2a2"
        now = datetime.now()
        x = az.entity_extraction(SUBSCRIPTION_KEY_ENV_NAME,command)
        if x[1]=='Location' or x[1]=='Organization':
            c = x[0]
        else:
            return json.dumps({"response": 'Give me a specific destination'}), 200



        send_url = "http://api.ipstack.com/check?access_key=9a86bc5e18df530bd1ded7ff6620187d"
        geo_req = requests.get(send_url)
        geo_json = json.loads(geo_req.text)
        lat = geo_json['latitude']
        lon = geo_json['longitude']
        results = geocoder.reverse_geocode(lat, lon)
        print(lat+0.4,lon+0.4)
        #pprint(results[0]['formatted'])
        our_loc = str(results[0]['formatted'])
        print(our_loc)
        
        '''directions_result = gmaps.directions(our_loc,
                                     c,
                                     mode="walking",
                                     departure_time=now)'''
        directions_result = gmaps.directions('Hodson Hall, Baltimore, MD',
                                     c,
                                     mode="walking",
                                     departure_time=now)
        time = directions_result[0]['legs'][0]['duration']['text']
        dis = directions_result[0]['legs'][0]['distance']['text']
        start_loc_lat = dis = directions_result[0]['legs'][0]['start_location']['lat']
        start_loc_lng = dis = directions_result[0]['legs'][0]['start_location']['lng']
        end_loc_lat = dis = directions_result[0]['legs'][0]['end_location']['lat']
        end_loc_lng = dis = directions_result[0]['legs'][0]['end_location']['lng']
        

        instru = []
        for i in directions_result[0]['legs'][0]['steps']:
            instru.append(i['html_instructions']+" "+i['distance']['text'] + ' ' + i['duration']['text'] + " Moving from lat : " + str(i['start_location']['lat']) +" , lon : "+str(i['start_location']['lng']) + " to lat : " + str(i['end_location']['lat']) +" , lon : "+str(i['end_location']['lng']))
        webbrowser.open('http:127.0.0.1:5000/map.html')
        #print("distance isssshabdgyjasvkd", dis)
        global value
        value = 'ETA '+ str(time)+' :)'
        global loc
        loc= [start_loc_lat,start_loc_lng,end_loc_lat,end_loc_lng] 
        mytext = 'Opened in a new tab.'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)  
        myobj.save("welcome.mp3") 
        subprocess.call(['afplay','welcome.mp3'])
        return render_template('map.html'), json.dumps({"response": 'It openend on a new Tab'}), 200
        
    elif intent=='person':
        thisdict={
        1:"anand.jpeg",
        2:"sandeep.jpeg",
        3:"Akshay.jpeg",
        4:"prateek.jpeg",
        5:"goldy.jpeg",
        6:"diya.jpeg",
        7:"Akshat.jpeg"

            }
        n=5
        f=0

        ch='y'
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
                f=2
                for faceMatch in response['FaceMatches']:
                    f=1
                    nameee=''
                    for i in targetFile:
                        if i != '.':
                            nameee+=i
                        else:
                            break
                    return json.dumps({"response": 'This is' + ' ' + nameee + ', '+ ' who\'s come to visit you! '
                            }), 200
                    '''print('The face at ' +
                            str(position['Left']) + ' ' +
                            str(position['Top']) +
                            ' matches with ' + confidence + '% confidence')
                    print(str(thisdict[i].split(".jpeg")))'''
                imageSource.close()
                imageTarget.close()               
            if(f!=1):
                return json.dumps({"response": 'This person doesn\'t exist in our database. Would you like to add him? '
                            }), 200
                #print ( 'This person doesn\'t exist in our database, what is the name of this person?: ')
                #namee= input()+".jpeg"
                namee= "damn this wont work"
                namee= namee+ ".jpeg"
                n=n+1
                os.rename("test.jpeg", namee)
                d1={n:namee}
                thisdict.update(d1)
            elif (f==1):
                os.remove("test.jpeg")
                ch='n'

    elif intent=='text':
        new=[]
        camera = cv2.VideoCapture(0)
        return_value, image = camera.read()
        cv2.imwrite('test1.jpeg', image)
        del(camera)
    
        s3 = boto3.resource('s3')
        images=[('test1.jpeg','test'),]

        for image in images:
            file = open(image[0],'rb')
            object = s3.Object('aags-wheeler1',image[0])
            ret = object.put(Body=file,
                                Metadata={'Name':image[1]}
                                )



        bucket='aags-wheeler1'
        photo='test1.jpeg'
        client=boto3.client('rekognition')
        response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
        textDetections=response['TextDetections']

        stuff=' '
        for text in textDetections:
            if(' ' in text['DetectedText']):
                stuff+= text['DetectedText'] +'\n'
            
        print(stuff)

        return json.dumps({"response": stuff}), 200
        #talkToMe(str(text['DetectedText']))



        s3.Object('aags-wheeler1', 'test1.jpeg').delete()

    elif intent=='news':
        def NewsFromBBC():
            global new
            new=[] 
            main_url = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=e4313a22f54042c9aba095ce5354be51"
            open_bbc_page = requests.get(main_url).json() 
            article = open_bbc_page["articles"] 
            results = []
            for ar in article:
                results.append(ar["title"]) 
                
            for i in range(0,3):
                stuff= str(str((i+1)) +'. '+ results[i])
                new.append(stuff)
            return new
                #return json.dumps({"response": str(stuff)})
                #talkToMe(stuff)
        new = NewsFromBBC()
        news=' '
        for i in new:
            news+=i+',\n'+'\n'
        return json.dumps({"response": news})
    
    return json.dumps({"response": ''}), 200
if __name__=='__main__':
            #from pprint import pprint

    key = '9ceed27ef0e646188df1656457bdffa6'
    geocoder = OpenCageGeocode(key)

    webbrowser.open('http://127.0.0.1:5000/')
    app.run(debug=False)
