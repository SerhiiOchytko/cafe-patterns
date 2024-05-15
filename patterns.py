# Singleton: Менеджер кав'ярні, який єдиний керує закладом
class CafeManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CafeManager, cls).__new__(cls)
        return cls._instance

# Factory Method: Виробництво різних типів напоїв
class Beverage:
    def prepare(self):
        raise NotImplementedError

class Coffee(Beverage):
    def prepare(self):
        return "Приготування кави"

class Tea(Beverage):
    def prepare(self):
        return "Приготування чаю"

class BeverageCreator:
    def create_beverage(self):
        raise NotImplementedError

class CoffeeCreator(BeverageCreator):
    def create_beverage(self):
        return Coffee()

class TeaCreator(BeverageCreator):
    def create_beverage(self):
        return Tea()

if __name__ == "__main__":
    # Singleton: Один менеджер кав'ярні
    manager1 = CafeManager()
    manager2 = CafeManager()
    print(f"Екземпляри менеджера однакові: {manager1 is manager2}")

    # Factory Method: Створення напоїв
    coffee_creator = CoffeeCreator()
    coffee = coffee_creator.create_beverage()
    print(coffee.prepare())

    tea_creator = TeaCreator()
    tea = tea_creator.create_beverage()
    print(tea.prepare())
