import paho.mqtt.client as mqtt
import time

def lambda_handler(event, context):

    solace_url = "mr2j0vvhki1l0v.messaging.solace.cloud"
    solace_port = 20038
    solace_user = "solace-cloud-client"
    solace_passwd = "sd7rvjjkbdfu3grah9r5rqiqn6"

    solace_clientid = "test1"
    solace_pi_topic = "devices/+/events"
    #solace_pi_topic = "devices/#"

    qos = 1

    client = mqtt.Client(solace_clientid)  # Create instance of client with client ID “digi_mqtt_test”
    client.username_pw_set(solace_user, password=solace_passwd)  # set username and password
    client.on_connect = on_connect  # Define callback function for successful connection
    # client.connect(solace_url, solace_port, 60)  # Connect to (broker, port, keepalive-time)
    client.connect(solace_url, solace_port, 60)


    try:
        while True:
            client.subscribe(solace_pi_topic, qos)
            # print("after client.subscribe()")
            client.on_message = on_message  # Define callback function for receipt of a message
            client.loop_forever()  # Start networking daemon
            #time.sleep(1)
    except KeyboardInterrupt:
        print("exiting")
        client.disconnect()
        client.loop_stop()

    """
    return {
        'statusCode': 200,
        'body': on_message
    }
    """

def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker
    print("Connected with result code {0}".format(str(rc)))  # Print result of connection attempt


def on_message(client, userdata, msg):  # The callback for when a PUBLISH message is received from the server.
    # print ("on_message called")
    #response = str(msg.payload)
    print(str(msg.payload))  # Print a received msg

lambda_handler(1,1)