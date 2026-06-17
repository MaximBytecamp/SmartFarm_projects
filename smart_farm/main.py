from models.farm import Farm
from models.greenhouse import Greenhouse
from models.animal_zone import AnimalZone
from models.plant import Plant
from models.animal import Animal
from models.employee import Agronomist, Veterinarian
from models.task import Task
from models.sensor import TemperatureSensor, HumiditySensor


def main():
    farm = Farm("SmartFarm")

    greenhouse = Greenhouse(1, "Теплица №1")
    animal_zone = AnimalZone(2, "Загон №1")

    temp_sensor = TemperatureSensor(1, "Датчик температуры", 24, "°C")
    humidity_sensor = HumiditySensor(2, "Датчик влажности", 62, "%")

    greenhouse.add_sensor(temp_sensor)
    greenhouse.add_sensor(humidity_sensor)
    print(greenhouse.get_info())

    tomato = Plant(1, "овощ", "росток", 85, True)
    cucumber = Plant(2, "овощ", "растение", 76, True)

    greenhouse.add_plant(tomato)
    greenhouse.add_plant(cucumber)

    print(greenhouse.show_plants())
    print(greenhouse.get_average_plant_health())
    print(greenhouse.get_info())

    cow = Animal(1, "Белка", "корова", 4, 90, False)
    goat = Animal(2, "Стрелка", "коза", 2, 70, True)

    animal_zone.add_animal(cow)
    animal_zone.add_animal(goat)

    agronomist = Agronomist(1, "Иван Петров", "агроном")
    veterinarian = Veterinarian(2, "Мария Смирнова", "ветеринар")

    task1 = Task(
        "Полить томаты",
        "Проверить влажность и полить растения",
        "средний"
    )

    task2 = Task(
        "Проверить корову",
        "Осмотреть состояние здоровья животного",
        "высокий"
    )

    agronomist.assign_task(task1)
    veterinarian.assign_task(task2)

    print(agronomist.get_info())

    farm.add_zone(greenhouse)
    farm.add_zone(animal_zone)
    farm.add_employee(agronomist)
    farm.add_employee(veterinarian)
    farm.add_task(task1)
    farm.add_task(task2)

    print(farm.get_farm_info())

main()