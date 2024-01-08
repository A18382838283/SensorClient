from sClient import SClientController

client = SClientController()
client.refresh()

print(client.model.temperature)
print(client.model.humidity)
