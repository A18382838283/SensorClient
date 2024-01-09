import sys
from tkinter import Tk


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
        self._model = SClientModel()  # model
        self._view = SClientView()  # view
        self.init()  # init

    def init(self):
        self.init_model()
        self.init_view()

    def init_model(self):
        try:
            file = open("client.config")
            try:
                self.model.room_nr = file.readline().rstrip()
                self.model.broker_ip = file.readline().rstrip()
                self.model.broker_port = file.readline().rstrip()
                self.model.interval = int(file.readline().rstrip())
            finally:
                file.close()
        except FileNotFoundError as fnf:
            raise fnf

    def init_view(self):
        pass

    def refresh(self):
        self.model.temperature = 0.0
        self.model.humidity = False

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
