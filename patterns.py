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

# Observer: Оповіщення баристи про нові замовлення
class OrderSubject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Barista:
    def update(self, message):
        raise NotImplementedError

class ConcreteBarista(Barista):
    def update(self, message):
        print(f"Бариста отримав замовлення: {message}")

# Strategy: Різні стратегії приготування напоїв
class PreparationStrategy:
    def prepare(self, ingredients):
        raise NotImplementedError

class EspressoStrategy(PreparationStrategy):
    def prepare(self, ingredients):
        return f"Приготування еспресо з {', '.join(ingredients)}"

class LatteStrategy(PreparationStrategy):
    def prepare(self, ingredients):
        return f"Приготування латте з {', '.join(ingredients)}"

class PreparationContext:
    def __init__(self, strategy: PreparationStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PreparationStrategy):
        self._strategy = strategy

    def prepare_beverage(self, ingredients):
        return self._strategy.prepare(ingredients)


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

    # Observer: Оповіщення баристи про замовлення
    order_subject = OrderSubject()
    barista = ConcreteBarista()
    order_subject.attach(barista)
    order_subject.notify("Нове замовлення: Капучино")


    # Strategy: Різні стратегії приготування напоїв
    context = PreparationContext(EspressoStrategy())
    print(context.prepare_beverage(["водою", "зернами кави"]))

    context.set_strategy(LatteStrategy())
    print(context.prepare_beverage(["молоком", "зернами кави"]))

