from abc import ABC, abstractmethod 

class Sensor(ABC):
    def __init__(self, sensor_id: int, name: str, value: float, unit: str) -> None:
        self._id = sensor_id
        self._name = name 
        self.value = value 
        self.unit = unit 

    @property
    def id(self) -> int:
        return self._id 
    

    @property
    def name(self) -> str:
        return self._name 
    

    def read_value(self) -> float:
        return self.value 
    

    @abstractmethod
    def check_status(self) -> str:
        """Return sensor status."""

    def get_info(self) -> str:
        return f"{self.name}: {self.value}{self.unit} - {self.check_status()}"
    

    def __str__(self) -> str:
        return self.get_info()
    

class TemperatureSensor(Sensor):
    def check_status(self) -> str:
        if self.value < 15:
            return "холодно"
        
        elif self.value < 70:
            return "нормально"
        
        return "слишком жарко"
    

class HumiditySensor(Sensor):
    def check_status(self) -> str:
        if self.value < 30:
            return "слишком сухо"
        
        elif self.value <= 70:
            return "нормально"
        
        return "слишком влажно" 