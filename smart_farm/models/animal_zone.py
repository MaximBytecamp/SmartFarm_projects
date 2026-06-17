from smart_farm.exceptions.farm_exceptions import ObjectAlreadyExistsError, ObjectNotFoundError
from smart_farm.models.animal import Animal
from smart_farm.models.zone import Zone 

class Greenhouse(Zone):
    def __init__(self, zone_id: int, name: str) -> None:
        super().__init__(zone_id, name)
        self.animals: list[Animal] = []


    def add_animal(self, animal: Animal) -> str: 
        if animal in self.animals:
            raise ObjectAlreadyExistsError(f"Животное {animal.name} уже есть в загоне")

        self.animals.append(animal)
        return f"В загон {self.name} добавлено животное {animal.name}"



    def remove_animal(self, animal: Animal) -> str: 
        if animal not in self.animals:
            raise ObjectNotFoundError(f"Животное {animal.name} не найдено в загоне") 

        self.animals.remove(animal)
        return f"Из загона {self.name} удалено животное {animal.name}"


    def show_animals(self) -> str:
        if not self.animals:
            return "В загоне нет животных"

        return "\n".join(str(animal) for animal in self.animals)


    def get_average_animal_health(self) -> float:
        if not self.animals:
            return 0.0 

        return round(sum(animal.health_level for animal in self.animals) / len(self.animals), 1)


    def get_info(self) -> str:
        return (
            f"Загон {self.name}: животных {len(self.animals)}, "
            f"Датчиков {len(self.sensors)}, среднее здоровье {self.get_average_animal_health()}"
        )


    def __iter__(self):
        return iter(self.animals)
