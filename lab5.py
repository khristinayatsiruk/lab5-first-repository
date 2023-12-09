"""
Importing all modules
"""
import time
from enum import Enum
from datetime import datetime


class CarBrand(Enum):
    """
    Enum representing different types of cars
    """
    TOYOTA = 1
    HONDA = 2
    FORD = 3
    BMW = 4
    AUDI = 5
    INFINITY = 6


class Car:
    """
    Represents a car with basic properties
    """
    def __init__(self, brand, age, max_speed, horsepower):
        self.brand = brand
        self.age = age
        self.max_speed = max_speed
        self.horsepower = horsepower


class Parking:
    """
    Represents a parking composed of cars
    """
    def __init__(self, max_capacity, hour_rate):
        self.max_capacity = max_capacity
        self.hour_rate = hour_rate
        self.cars = []

    def park_car(self, car):
        """
        Park a car in the parking.
        """
        if len(self.cars) < self.max_capacity:
            car.parked_time = datetime.now()
            self.cars.append(car)
            print(f"{car.brand} has been parked.")
        else:
            print(f"Parking is full. Cannot park your {car.brand.name}.")

    def leave_parking(self, car):
        """
        Leave the parking and calculate the price.
        """
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

    car_bmw = Car(CarBrand.BMW, 4, 230, 180)
    car_audi = Car(CarBrand.AUDI, 6, 210, 165)
    car_ford = Car(CarBrand.FORD, 2, 190, 126)
    car_honda = Car(CarBrand.HONDA, 9, 160, 88)
    car_toyota = Car(CarBrand.TOYOTA, 5, 200, 147)
    car_infinity = Car(CarBrand.INFINITY, 7, 195, 164)

    parking = Parking(4, 6.0)

    parking.park_car(car_bmw)
    time.sleep(1)

    parking.park_car(car_audi)
    time.sleep(1)

    parking.park_car(car_ford)
    time.sleep(1)

    parking.park_car(car_honda)
    time.sleep(2)

    parking.park_car(car_toyota)
    time.sleep(1)

    parking.leave_parking(car_bmw)
    parking.park_car(car_infinity)
    time.sleep(1)
    parking.leave_parking(car_audi)
    parking.leave_parking(car_ford)
    parking.leave_parking(car_honda)
    




