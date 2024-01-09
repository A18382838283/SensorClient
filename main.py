from sClient import SClientController
import time

client = SClientController()

while True:
    client.refresh()
    print(client.model.temperature)
    print(client.model.humidity)
    time.sleep(client.model.interval)