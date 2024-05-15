# Singleton: Менеджер кав'ярні, який єдиний керує закладом
class CafeManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CafeManager, cls).__new__(cls)
        return cls._instance

if __name__ == "__main__":
    # Singleton: Один менеджер кав'ярні
    manager1 = CafeManager()
    manager2 = CafeManager()
    print(f"Екземпляри менеджера однакові: {manager1 is manager2}")
