from smart_farm.models.farm_object import FarmObject
from exceptions.farm_exceptions import InvalidHealthLevelError


class Plant(FarmObject):
    growth_stages = [
        "семя",
        "росток",
        "растение",
        "цветение",
        "плодоношение"
    ]

    def __init__(
            self,
            object_id: int,
            plant_type: str,
            growth_stage: str,
            health_level: int,
            water_required: bool,
    ) -> None:
        super().__init__(object_id, plant_type)
        if growth_stage not in self.growth_stages:
            growth_stage = self.growth_stages[0]

        self.growth_stage = growth_stage
        self.health_level = health_level
        self.water_required = water_required
        self._validate_health()


    def _validate_health(self) -> None:
        if not 0 <= self.health_level <= 100:
            raise InvalidHealthLevelError(
                f"Здоровье растения {self.name} должно быть от 0 до 100"
            )
        
    def water(self) -> str:
        if not self.water_required:
            return f"{self.name} полив сейчас не требуется"
        
        self.water_required = False 
        self.health_level = min(100, self.health_level + 5)

        return f"{self.name}: растение полито, здоровье {self.health_level}"
    

    def grow(self) -> str:
        current_index = self.growth_stages.index(self.growth_stage)

        if current_index == len(self.growth_stages) - 1:
            return f"{self.name} растение уже на этапе плодоношения"

        self.growth_stage = self.growth_stages[current_index + 1]      

        return f"{self.name}: новый этап роста - {self.growth_stage}"
    

    def check_health(self) -> str:
        self._validate_health()

        if self.health_level < 40:
            return f"{self.name}: здоровье низкое, требуется уход."
        
        if self.water_required:
            return f"{self.name} требуется полив"
        
        return f"{self.name} состояние хорошее."
    

    def get_info(self) -> str:
        water_status = "нужен полив" if self.water_required else "полив не нужен"

        return (
            f"Растение {self.name}, этап {self.growth_stage}, "
            f"здоровье {self.health_level}, {water_status}"
        )
    

    def __str__(self) -> str:
        return f"{self.name} - здоровье {self.health_level}"
    
    def __lt__(self, other: "Plant") -> bool:
        return self.health_level < other.health_level
    