class Car:
    def __init__(self, engine_power, brand, max_speed):
        self.engine_power = engine_power  # Потужність двигуна
        self.brand = brand  # Марка автомобіля
        self.max_speed = max_speed  # Максимальна швидкість

# Створення екземпляра класу
my_car = Car(625, "BMW", 305)

# Виведення значень полів
print(f"Марка: {my_car.brand}")
print(f"Потужність двигуна: {my_car.engine_power} к.с.")
print(f"Максимальна швидкість: {my_car.max_speed} км/год")