from core.domain.interfaces.services.CarServiceInterface import CarServiceInterface  # noqa
from infra.repositories.sqlserver.CarRepository import CarRepository  # noqa
from core.domain.dto.CarInsertRequestDTO import CarInsertRequestDTO
from core.domain.dto.CarResponseDTO import CarResponseDTO
from core.domain.dto.CarUpdateRequestDTO import CarUpdateRequestDTO
from core.domain.models.Car import Car
from typing import List


class CarService(CarServiceInterface):
    def addNewItem(self, carData: CarInsertRequestDTO) -> int:
        car = Car()
        car.name = carData.carName
        car.carType = carData.carType
        car.yearModel = carData.yearModel
        car.isNew = carData.isNew
        carRepository = CarRepository()
        carId = carRepository.createNewCar(car)

        return carId

    def getAllItens(self) -> list[CarResponseDTO]:
        carRepository = CarRepository()
        carListDB = carRepository.readAllCars()

        print(carListDB)

        carList = list[CarResponseDTO]()

        if len(carListDB) > 0:
            for car in carListDB:
                carData = CarResponseDTO()
                carData.id = car.id
                carData.name = car.name
                carData.carType = car.carType
                carData.isNew = car.isNew
                carList.append(carData)

        return carList

    def getCarById(self, id: int) -> CarResponseDTO:
        carRepository = CarRepository()
        carDB = carRepository.readCar(id)

        carData = CarResponseDTO()
        carData.id = carDB.id
        carData.name = carDB.name
        carData.carType = carDB.carType
        carData.isNew = carDB.isNew
        return carDB

    def updateCar(self, carData: CarUpdateRequestDTO):
        car = Car()
        car.name = carData.carName
        car.carType = carData.carType
        car.yearModel = carData.yearModel
        car.isNew = carData.isNew
        car.id = carData.id
        carRepository = CarRepository()
        carRepository.updateCar(car)

    def deleteCar(self, id: int):
        carRepository = CarRepository()
        carRepository.deleteCar(id)
