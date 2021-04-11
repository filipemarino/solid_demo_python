from core.domain.dto import CarInsertRequestDTO, CarResponseDTO, CarUpdateRequestDTO  # noqa
from typing import List
import abc


class CarServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addNewItem(self, carData: CarInsertRequestDTO) -> int:
        return NotImplementedError("Method addNewItem() must be implemented")

    @abc.abstractmethod
    def getAllItens(self) -> list[CarResponseDTO]:
        return NotImplementedError("Method getAllItens() must be implemented")

    @abc.abstractmethod
    def getCarById(self, id: int) -> CarResponseDTO:
        return NotImplementedError("Method getCarById() must be implemented")

    @abc.abstractmethod
    def updateCar(self, carData: CarUpdateRequestDTO):
        return NotImplementedError("Method updateCar() must be implemented")

    @abc.abstractmethod
    def deleteCar(self, id: int):
        return NotImplementedError("Method deleteCar() must be implemented")
