import paho.mqtt.client as mqtt
from serial import Serial

ser=Serial('/dev/ttyACM1',9600)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    client.subscribe("wheeler")
    client.subscribe("wheeler")
 
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    if msg.payload == "forward":
        print("Asked to move forward")
        ser.write(b'1')
        


    if msg.payload == "backward":
        print("Asked to move backward")
        ser.write(b'2')
    
    if msg.payload == "left":
        print("Asked to move left")
        ser.write(b'3')
        
    if msg.payload == "right":
        print("Asked to move right")
        ser.write(b'4')    
 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()