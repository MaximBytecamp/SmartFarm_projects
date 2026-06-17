from exceptions.farm_exceptions import ObjectAlreadyExistsError
from models.animal_zone import AnimalZone
from models.greenhouse import Greenhouse
from models.storage import Storage
from models.task import Task
from models.zone import Zone 

class Farm:
    def __init__(self, title: str, storage: Storage | None = None) -> None:
        self.title = title
        self.zones: list[Zone] = []
        self.employees = []
        self.storage = storage if storage is not None else Storage()
        self.tasks: list[Task] = []



    def add_zone(self, zone: Zone) -> str:
        if zone in self.zones:
            raise ObjectAlreadyExistsError(f"Зона {zone.name} уже добавлена")

        self.zones.append(zone)
        return f"Добавлена зона: {zone.name}"


    def add_employee(self, employee) -> str:
        if employee in self.employees:
            raise ObjectAlreadyExistsError(f"Сотрудник {employee.name} уже добавлен")

        self.employees.append(employee)
        return f"Добавлена сотрудник: {employee.name}"


    def add_task(self, task: Task) -> str:
        if task in self.tasks:
            raise ObjectAlreadyExistsError(f"Задача {task.title} уже добавлен")

        self.tasks.append(task)
        self.tasks.sort()
        return f"Добавлена задача: {task.title}"


    def show_zones(self) -> str:
        if not self.zones:
            return "На ферме нет зон"

        return "\n".join(str(zone) for zone in self.zones)

    def show_employees(self) -> str:
        if not self.employees:
            return "На ферме нет сотрудников"

        return "\n".join(str(employee) for employee in self.employees)


    def show_tasks(self) -> str:
        if not self.tasks:
            return "На ферме нет задач"

        return "\n".join(str(task) for task in self.tasks)

    def get_farm_info(self) -> str:
        return (
            f"Ферма {self.title}: зон {len(self.zones)}, "
            f"сотрудников {len(self.employees)}, задач {len(self.tasks)}"
        )

    def __len__(self) -> int:
        return len(self.zones)

    def __len__(self) -> int:
        return len(self.tasks)

    