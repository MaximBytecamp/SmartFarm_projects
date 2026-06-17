from exceptions.farm_exceptions import ResourceNotEnoughError


class Storage:
    def __init__(self) -> None:
        self.resources: dict[str, int] = {}

    def add_resource(self, name: str, amount: int) -> str:
        self.resources[name] = self.resources.get(name, 0) + amount
        return f"На склад добавлено: {name} - {amount}"


    def use_resource(self, name: str, amount: int) -> str:
        current_amount = self.get_resource_amount(name)

        if current_amount < amount:
            raise ResourceNotEnoughError(
                f"Недостаточно ресурса {name}: есть {current_amount}, нужно {amount}"
            )

        self.resources[name] = current_amount - amount

        return f"Использовано: {name} - {amount}"


    def get_resource_amount(self, name: str) -> int:
        return self.resources.get(name, 0)


    def show_resources(self) -> str:
        if not self.resources:
            return "Склад пуст"

        return "\n".join(f"{name}: {amount}" for name, amount in self.resources.items())


    def __str__(self) -> str:
        return self.show_resources()