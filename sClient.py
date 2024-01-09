import paho.mqtt.client as mqtt
from tkinter import Tk
from configparser import ConfigParser


class SClientModel(object):
    def __init__(self):
        self._room_nr = ""
        self._broker_ip = ""
        self._broker_port = ""
        self._interval = 0
        self._temperature = 0.0
        self._temperature_limit = 0.0
        self._humidity = False

    @property
    def room_nr(self):
        pass

    @room_nr.setter
    def room_nr(self, value: str):
        self._room_nr = value

    @room_nr.getter
    def room_nr(self) -> str:
        return self._room_nr

    @property
    def broker_ip(self):
        pass

    @broker_ip.setter
    def broker_ip(self, value: str):
        self._broker_ip = value

    @broker_ip.getter
    def broker_ip(self) -> str:
        return self._broker_ip

    @property
    def broker_port(self):
        pass

    @broker_port.setter
    def broker_port(self, value: str):
        self._broker_port = value

    @broker_port.getter
    def broker_port(self) -> str:
        return self._broker_port

    @property
    def interval(self):
        pass

    @interval.setter
    def interval(self, value: int):
        self._interval = value

    @interval.getter
    def interval(self) -> int:
        return self._interval

    @property
    def temperature(self):
        pass

    @temperature.setter
    def temperature(self, value: float):
        self._temperature = value

    @temperature.getter
    def temperature(self) -> float:
        return self._temperature

    @property
    def temperature_limit(self):
        pass

    @temperature_limit.setter
    def temperature_limit(self, value: float):
        self._temperature_limit = value

    @temperature_limit.getter
    def temperature_limit(self) -> float:
        return self._temperature_limit

    @property
    def humidity(self):
        pass

    @humidity.setter
    def humidity(self, value: bool):
        self._humidity = value

    @humidity.getter
    def humidity(self) -> bool:
        return self._humidity


class SClientView(Tk):
    pass


class SClientController(object):
    def __init__(self):
        self._model = SClientModel()
        self._view = SClientView()
        self.init()
        self.init_model()
        self.init_view()

        client_id = "SensorClient-" + self.model.room_nr
        print("ClientID: " + client_id)

        try:
            self.client = mqtt.Client(client_id)
            self.client.connect(self.model.broker_ip)
        except Exception as e:
            raise e

    def init(self):
        pass

    def init_model(self):
        self.refresh()

    def init_view(self):
        pass

    def refresh(self):
        config = ConfigParser()
        try:
            config.read("config.ini")
            self.model.room_nr = config.get('settings', 'room_nr')
            self.model.broker_ip = config.get('settings', 'broker_ip')
            self.model.broker_port = config.get('settings', 'broker_port')
            self.model.interval = config.getint('settings', 'interval')
            self.model.temperature_limit = config.getfloat('settings', 'temperature_limit')
        except Exception as e:
            raise e


    @property
    def model(self):
        pass

    @model.setter
    def model(self, value: SClientModel):
        self._model = value

    @model.getter
    def model(self) -> SClientModel:
        return self._model

    @property
    def view(self):
        pass

    @view.setter
    def view(self, value: SClientView):
        self._view = value

    @view.getter
    def view(self) -> SClientView:
        return self._view
