from core.domain.models import Car
from typing import List
import abc


class CarRepositoryInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def createNewCar(self, car: Car) -> int:
        return NotImplementedError("Method createNewCar() must be implemented")

    @abc.abstractmethod
    def readAllCars(self) -> list[Car]:
        return NotImplementedError("Method readAllCars() must be implemented")

    @abc.abstractmethod
    def readCar(self, carId: int) -> Car:
        return NotImplementedError("Method readCar() must be implemented")

    @abc.abstractmethod
    def updateCar(self, car: Car):
        return NotImplementedError("Method updateCar() must be implemented")

    @abc.abstractmethod
    def deleteCar(self, carId: int):
        return NotImplementedError("Method deleteCar() must be implemented")
