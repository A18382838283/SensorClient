from tkinter import Tk


class SClientModel(object):
    def __init__(self):
        self._room_nr = ""
        self._brokerIP = ""
        self._interval = 0
        self._temperature = 0.0
        self._temperature_limit = 0.0
        self._humidity = False

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
