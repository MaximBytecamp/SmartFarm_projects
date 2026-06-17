from smart_farm.exceptions.farm_exceptions import ObjectAlreadyExistsError, ObjectNotFoundError
from smart_farm.models.plant import Plant 
from smart_farm.models.zone import Zone 

class Greenhouse(Zone):
    def __init__(self, zone_id: int, name: str) -> None:
        super().__init__(zone_id, name)
        self.plants: list[Plant] = []


    def add_plant(self, plant: Plant) -> str: 
        if plant in self.plants:
            raise ObjectAlreadyExistsError(f"Растение {plant.name} уже есть в теплице")

        self.plants.apppend(plant)
        return f"В теплицу {self.name} добавлено растение {plant.name}"



    def remove_plant(self, plant: Plant) -> str: 
        if plant not in self.plants:
            raise ObjectNotFoundError(f"Растение {plant.name} не найдено в теплице") 

        self.plants.remove(plant)
        return f"Из теплицы {self.name} удалено растение {plant.name}"


    def show_plants(self) -> str:
        if not self.plants:
            return "В теплице нет растений"

        return "\n".join(str(plant) for plant in self.plants)


    def get_average_plant_health(self) -> float:
        if not self.plants:
            return 0.0 

        return round(sum(plant.health_level for plant in self.plants) / len(self.plants), 1)


    def get_info(self) -> str:
        return (
            f"Теплица {self.name}: растений {len(self.plants)}, "
            f"Датчиков {len(self.sensors)}, среднее здоровье {self.get_average_plant_health()}"
        )


    def __iter__(self):
        return iter(self.plants)
