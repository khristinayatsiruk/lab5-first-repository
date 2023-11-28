import time
from enum import Enum
from datetime import datetime


class CarBrand(Enum):
    TOYOTA = 1
    HONDA = 2
    FORD = 3
    BMW = 4
    AUDI = 5
    INFINITY = 6


class Car:
    def __init__(self, brand, age, max_speed, horsepower):
        self.brand = brand
        self.age = age
        self.max_speed = max_speed
        self.horsepower = horsepower


class Parking:
    def __init__(self, max_capacity, hour_rate):
        self.max_capacity = max_capacity
        self.hour_rate = hour_rate
        self.cars = []

    def park_car(self, car):
        if len(self.cars) < self.max_capacity:
            car.parked_time = datetime.now()
            self.cars.append(car)
            print(f"{car.brand} has been parked.")
        else:
            print(f"Parking is full. Cannot park your {car.brand.name}.")

    def leave_parking(self, car):
        if car in self.cars:
            if car.parked_time:
                parked_duration = (datetime.now() - car.parked_time).total_seconds() / 3600
                price = parked_duration * self.hour_rate
                print(
                    f"{car.brand} has left the parking. Parking duration: {parked_duration:.2f}"
                    f" hours. Price: ${price:.2f}")
                self.cars.remove(car)
            else:
                print(f"{car.brand} has no parked time.")
        else:
            print(f"{car.brand} is not in the parking.")


if __name__ == "__main__":

    car_1 = Car(CarBrand.BMW, 4, 230, 180)
    car_2 = Car(CarBrand.AUDI, 6, 210, 165)
    car_3 = Car(CarBrand.FORD, 2, 190, 126)
    car_4 = Car(CarBrand.HONDA, 9, 160, 88)
    car_5 = Car(CarBrand.TOYOTA, 5, 200, 147)
    car_6 = Car(CarBrand.INFINITY, 7, 195, 164)

    parking = Parking(4, 6.0)

    parking.park_car(car_1)
    time.sleep(1)

    parking.park_car(car_3)
    time.sleep(1)

    parking.park_car(car_4)
    time.sleep(1)

    parking.park_car(car_5)
    time.sleep(2)

    parking.park_car(car_6)
    time.sleep(1)

    parking.leave_parking(car_1)
    parking.park_car(car_6)
    time.sleep(1)
    parking.leave_parking(car_2)
    parking.leave_parking(car_3)
    parking.leave_parking(car_4)
    




