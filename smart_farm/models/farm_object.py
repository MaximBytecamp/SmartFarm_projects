from abc import ABC, abstractmethod


class FarmObject(ABC):
    def __init__(self, object_id: int, name: str) -> None:
        self._id = object_id
        self._name = name 

    @property
    def id(self) -> int:
        return self._id 
    
    @property
    def name(self) -> str: 
        return self._name 
    

    def __str__(self) -> str:
        return f"{self.name} (id={self.id})"

    @abstractmethod
    def get_info(self) -> str:
        """Return object details"""
