import requests,json
import urllib
def currentad():

    send_url = "http://api.ipstack.com/check?access_key=9a86bc5e18df530bd1ded7ff6620187d"
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    latitude = geo_json['latitude']
    longitude = geo_json['longitude']
    return [latitude,longitude]

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
print(descript_place + ' ' + temp_c_str)