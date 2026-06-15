from smart_farm.models.farm_object import FarmObject
from exceptions.farm_exceptions import InvalidHealthLevelError

class Animal(FarmObject):
    def __init__(
            self,
            object_id: int,
            name: str,
            animal_type: str,
            age: int, 
            health_level: int,
            is_hungry: bool
    ) -> None: 
        super().__init__(object_id, name)
        self.animal_type = animal_type
        self.age = age 
        self.health_level = health_level 
        self.is_hungry = is_hungry
        self._validate_health()

    
    def _validate_health(self) -> None:
        if not 0 <= self.health_level <= 100:
            raise InvalidHealthLevelError(
                f"Здоровье животного {self.name} должно быть от 0 до 100"
            )
        

    def feed(self) -> str:
        if not self.is_hungry:
            return f"{self.name}: животное не голодное"
        
        self.is_hungry = False 
        self.health_level = min(100, self.health_level + 5)

        return f"{self.name}: животное покормлено, здоровье {self.health_level}."
    

    def heal(self) -> str:
        self.health_level = min(100, self.health_level + 15)
        self._validate_health()
        return f"{self.name}: лечение выполнено, здоровье {self.health_level}"
    
    def check_health(self) -> str: 
        self._validate_health()

        messages = []

        if self.is_hungry:
            messages.append("Требует кормления")
        
        if self.health_level < 40:
            messages.append("Рекомендуется вызвать ветеринара")

        if not messages:
            return f"Состояние животного хорошее"
        
        return f"{self.name}: {", ".join(messages)}."
    

    def get_info(self) -> str:
        hunger = "голодное" if self.is_hungry else "не голодное"
        return (
            f"{self.animal_type.title()} {self.name}: возраст {self.age}, "
            f"здоровье: {self.health_level}, {hunger}"
        )
    

    def __str__(self) -> str:
        return f"{self.animal_type.title()} {self.name} - здоровье {self.health_level}"

        

