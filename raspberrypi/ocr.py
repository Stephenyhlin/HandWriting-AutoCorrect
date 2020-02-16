from PIL import Image
import pytesseract
import argparse
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import json
import time

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",
    help="path to input image to be OCR'd", default="uwu.tif")
args = vars(ap.parse_args())

img = Image.open(args["image"])
text = pytesseract.image_to_string(img)
print(text)

solace_url = "mr2j0vvhki1l0v.messaging.solace.cloud"
solace_port = 20038
solace_user = "solace-cloud-client"
solace_passwd = "sd7rvjjkbdfu3grah9r5rqiqn6"

solace_clientid = "raspi_client"
solace_pi_topic = "project/ocr"

client = mqtt.Client(solace_clientid)
client.username_pw_set(username=solace_user,password=solace_passwd)
client.connect(solace_url,port=solace_port)

payload = json.dumps({"text": text}, indent=4)
print(payload)
client.publish(solace_pi_topic, payload, qos=1)
time.sleeps(5)

client.loop_stop()
client.disconnect()
