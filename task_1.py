import logging
from abc import ABC, abstractmethod


logging.basicConfig(level=logging.INFO)


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self) -> str:
        pass


class VehicleFactory(ABC):
    @abstractmethod
    def create_car() -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle() -> Vehicle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model) -> Vehicle:
        return Car(make, model, "US")

    def create_motorcycle(self, make, model) -> Vehicle:
        return Motorcycle(make, model, "US")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model) -> Vehicle:
        return Car(make, model, "EU")

    def create_motorcycle(self, make, model) -> Vehicle:
        return Motorcycle(make, model, "EU")


class Car(Vehicle):
    def __init__(self, make, model, region_spec):
        self.make = make
        self.model = model
        self.region_spec = region_spec

    def start_engine(self):
        logging.info(f"{self.make} {self.model} ({self.region_spec} spec): Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make, model, region_spec):
        self.make = make
        self.model = model
        self.region_spec = region_spec

    def start_engine(self):
        logging.info(f"{self.make} {self.model} ({self.region_spec} spec): Мотор заведено")


# Використання
vehicle1 = USVehicleFactory().create_car("Toyota", "Corolla")
vehicle1.start_engine()

vehicle2 = EUVehicleFactory().create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()
