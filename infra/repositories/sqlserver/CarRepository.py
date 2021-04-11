from core.domain.interfaces.repositories.sqlserver.CarRepositoryInterface import CarRepositoryInterface  # noqa
from core.domain.models.Car import Car
from typing import List
import pyodbc


class CarRepository(CarRepositoryInterface):
    
    def __init__(self):
        self.tableName = "dbo.Car"
        self.connection = pyodbc.connect("""
                        Driver={SQL Server};
                        Server=DESKTOP-J565JP9\\SQLEXPRESS;
                        Database=MAIN_DB;
                        Trusted_Connection=yes;""")  # noqa

    def createNewCar(self, car: Car) -> int:

        isNew = int()

        if car.isNew == True:
            isNew = 1
        else:
            isNew = 0

        query = f"""
                INSERT INTO {self.tableName} 
                (name, carType, yearModel, isNew) VALUES 
                ('{car.name}', '{car.carType}', {car.yearModel}, {isNew})"""  # noqa

        cursor = self.connection.cursor()
        cursor.execute(query)
        cursor.commit()

        query = f"""
                SELECT TOP 1 id FROM {self.tableName} WITH (NOLOCK)
                WHERE name = '{car.name}'
                AND carType = '{car.carType}'
                AND yearModel = '{car.yearModel}'
                AND isNew = '{isNew}'
                ORDER BY id DESC
                """
        cursor.execute(query)

        row = cursor.fetchone()

        cursor.close()

        return row[0]

    def readAllCars(self) -> list[Car]:
        query = f"SELECT * FROM {self.tableName} WITH (NOLOCK)"
        cursor = self.connection.cursor()
        cursor.execute(query)

        carList = list[Car]()

        for row in cursor.fetchall():
            car = Car()
            car.id = row[0]
            car.name = row[1]
            car.carType = row[2]
            car.yearModel = row[3]
            car.isNew = row[4]
            carList.append(car)
        return carList

    def readCar(self, carId: int) -> Car:
        query = f"SELECT * FROM {self.tableName} WITH (NOLOCK) WHERE id = {carId}"
        cursor = self.connection.cursor()
        cursor.execute(query)

        car = Car()

        row = cursor.fetchone()

        car.id = row[0]
        car.name = row[1]
        car.carType = row[2]
        car.yearModel = row[3]
        car.isNew = row[4]
            
        return car

    def updateCar(self, car: Car):
        isNew = int()

        if car.isNew == True:
            isNew = 1
        else:
            isNew = 0

        query = f"""
            UPDATE {self.tableName} 
            SET name = '{car.name}', 
            carType = '{car.carType}', 
            yearModel = {car.yearModel}, 
            isNew = {isNew} 
            WHERE id = {car.id}"""  # noqa

        cursor = self.connection.cursor()
        cursor.execute(query)
        cursor.commit()
        cursor.close()

    def deleteCar(self, carId: int):
        query = f"""
            DELETE FROM {self.tableName} 
            WHERE id = {carId}"""  # noqa
            
        cursor = self.connection.cursor()
        cursor.execute(query)
        cursor.commit()
        cursor.close()
