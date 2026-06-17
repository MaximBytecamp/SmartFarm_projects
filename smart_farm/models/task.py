from exceptions.farm_exceptions import InvalidTaskPriorityError

class Task:
    available_priorites = ("низкий", "средний", "высокий")
    priority_order = {"высокий": 0, "средний": 1, "низкий": 2}

    def __init__(self, title: str, descrpition: str, priority: str) -> None:
        if priority not in self.available_priorites:
            raise InvalidTaskPriorityError(
                f"Приоритет {priority} недоступен. Используйте: "
                f"{", ".join(self.available_priorites)}" 
            )
        
        self.title = title 
        self.description = descrpition
        self.priority = priority
        self.is_completed = False 

    
    def complete(self) -> str:
        self.is_completed = True 
        return f"Задача выполнена: {self.title}"
    
    def get_task_info(self) -> str:
        status = "выполнено" if self.is_completed else "не выполнено"

        return f"{self.title} [{self.priority}] - {status}"
    

    def __str__(self) -> str: 
        status = "готово" if self.is_completed else "в работе"
        return f"{self.title} [{self.priority}] - {status}"
    
    def __eq__(self, other: object) -> bool: 
        if not isinstance(other, Task):
            return False 
        
        return self.title == other.title 
    

    def __lt__(self, other: "Task") -> bool:
        return self.priority_order[self.priority] < self.priority_order[other.priority]

