from abc import ABC, abstractmethod

from smart_farm.exceptions.farm_exceptions import ObjectAlreadyExistsError
from smart_farm.models.sensor import Sensor 

class Zone(ABC):
    def __init__(self, zone_id: int, name: str) -> None:
        self._id = zone_id
        self._name = name 

        self.sensors: list[Sensor] = []

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name
    
    def add_sensor(self, sensor: Sensor) -> str:
        if sensor in self.sensors:
            raise ObjectAlreadyExistsError(f"Датчик {sensor.name} уже есть в этом зоне")
        
        self.sensors.append(sensor)

        return f"В зону {self.name} добавлен датчик {sensor.name}"
    

    def show_sensors(self) -> str:
        if not self.sensors:
            return "Датчики не добавлены"
        
        return "\n".join(sensor.get_info() for sensor in self.sensors)
    
    @abstractmethod
    def get_info(self) -> str:
        """Return zone information"""

    
    def __len__(self) -> int:
        return len(self.sensors)
    

    def __str__(self) -> str:
        return self.get_info()

