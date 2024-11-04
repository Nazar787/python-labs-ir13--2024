class Car:
    color = ""                      
    year = 0   
    
    def __init__(self, engine_power=0, brand="", max_speed=0):
        self.__engine_power = engine_power    
        self.__brand = brand                  
        self.__max_speed = max_speed          
        self.__distance = 0                   
    def get_engine_power(self):
        return self.__engine_power

    def set_engine_power(self, engine_power):
        self.__engine_power = engine_power

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_max_speed(self):
        return self.__max_speed

    def set_max_speed(self, max_speed):
        self.__max_speed = max_speed

    def get_distance(self):
        return self.__distance

    def set_distance(self, distance):
        self.__distance = distance

    def drive(self, distance):
        if distance > 0:
            self.__distance += distance
            print(f"{self.__brand} проїхав {distance} км. Загальна відстань: {self.__distance} км.")
        else:
            print("Відстань повинна бути позитивною!")

    def __str__(self):
        return (f"Car: {self.__brand}, Power: {self.__engine_power} HP, Max Speed: {self.__max_speed} km/h, "
                f"Distance traveled: {self.__distance} km")

    def __repr__(self):
        return (f"Car(brand='{self.__brand}', engine_power={self.__engine_power}, "
                f"max_speed={self.__max_speed}, distance={self.__distance})")

    def __del__(self):
        print(f"Car '{self.__brand}' знищено")

if __name__ == "__main__":
    car1 = Car(150, "Toyota", 180)
    car2 = Car(200, "BMW", 220)
    car3 = Car(120, "Honda", 160)

    car1.drive(100)
    car2.drive(150)
    car3.drive(200)

    print(car1)
    print(car2)
    print(car3)
