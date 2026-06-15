from abc import ABC, abstractmethod

from smart_farm.exceptions.farm_exceptions import ObjectNotFoundError
from smart_farm.models.animal import Animal
from smart_farm.models.plant import Plant 
from smart_farm.models.task import Task 

class Employee(ABC):
    def __init__(self, employee_id: int, name: str, position: str) -> None:
        self._id = employee_id
        self._name = name 
        self.position = position
        self.tasks: list[Task] = []

    @property
    def id(self) -> int:
        return self._id 
    

    @property
    def name(self) -> str:
        return self._name 
    
    def assign_task(self, task: Task) -> str:
        self.tasks.append(task)
        return f"{self.name}: назначена задача {task.title}"
    

    def complete_task(self, task: Task) -> str:
        if task not in self.tasks:
            return ObjectNotFoundError(f"Задача {task.title} не назначена сотруднику")
        
        return task.complete()


    @abstractmethod
    def work(self) -> str:
        "Return work description"

    
    def get_info(self) -> str:
        return f"{self.position.title()} {self.name}: задач {len(self)}"
    

    def __len__(self) -> int: 
        return len(self.tasks)
    

    def __str__(self) -> str:
        return self.get_info()


class Agronomist(Employee):
    def work(self) -> str:
        return f"{self.name} проверяет растение и состояние теплиц"
    
    def inspect_plant(self, plant: Plant):
        return plant.check_health()
    

    def water_plant(self, plant: Plant):
        return plant.water()
    


class Veterinarian(Employee):
    def work(self) -> str:
        return f"{self.name} осматривает животных и проводит лечение"
    
    
    def inspect_animal(self, animal: Animal) -> str:
        return animal.check_health()
    

    def heal_animal(self, animal: Animal) -> str:
        return animal.heal()
    

    def feed_animal(self, animal: Animal) -> str: 
        return animal.feed
    


    