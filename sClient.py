import json
import random
import time
import datetime
from configparser import ConfigParser
from paho.mqtt import client as paho


class SensorClient:
    def __init__(self):
        config = ConfigParser()
        try:
            config.read('config.ini', 'UTF-8')
            self.client_id = config.get('settings', 'room_nr')
            self.broker_ip = config.get('settings', 'broker_ip')
            self.broker_port = config.getint('settings', 'broker_port')
            self.interval = config.getint('settings', 'interval')
            self.temperature_limit = config.getfloat('settings', 'temperature_limit')
            self.humid = False
        except Exception as e:
            raise e

        try:
            self.client = paho.Client(self.client_id)
            self.client.on_connect = on_connect
            self.client.on_publish = on_publish
            try:
                self.client.connect(self.broker_ip, self.broker_port)
            finally:
                self.client.disconnect()
        except Exception as e:
            raise e

        print('[--------------Config-------------]')
        print('Client-ID: ' + str(self.client_id))
        print('Broker-IP: ' + str(self.broker_ip))
        print('Broker-Port: ' + str(self.broker_port))
        print('Interval: ' + str(self.interval))
        print('Temperature-Limit: ' + str(self.temperature_limit))

    def run(self):
        try:
            print('[--------------Log----------------]')
            self.client.reconnect()

            while True:
                dump = json.dumps({"Test": str(random.randint(1, 1000)), "Test2": str(random.randint(1, 10000))})

                self.client.publish("data/sensorclient", dump)
                time.sleep(self.interval)
        finally:
            self.client.disconnect()


def on_connect(mqttc, userdata, rc):
    print(str(datetime.datetime.now()) + ': Connected with result code ' + str(rc))


def on_publish(client, userdata, mid):
    print(str(datetime.datetime.now()) + ': Message Published (Message-ID: ' + str(mid) + ')')
