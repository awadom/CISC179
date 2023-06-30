class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed


new_car = Car(2022, "BMW")

# print("Accelerating:")
for gas_pedal in range(5):
    new_car.accelerate()
    print(new_car.get_speed())

# print("Braking:")
for brake_pedal in range(5):
    new_car.brake()
    print(new_car.get_speed())
