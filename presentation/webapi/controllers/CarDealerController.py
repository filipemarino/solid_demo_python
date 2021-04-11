from flask_restx import Resource, Namespace, fields
from flask import request
import json
from application.service.CarService import CarService  # noqa
from core.domain.dto.CarInsertRequestDTO import CarInsertRequestDTO
from core.domain.dto.CarUpdateRequestDTO import CarUpdateRequestDTO
from core.domain.dto.CarInsertResponseDTO import CarInsertResponseDTO
from os import environ

api = Namespace('Car Dealer', description='Car Dealer Services')

# definição de modelo que será validado ao receber post
modelInsert = api.model('CarModelInsert', {
    'name': fields.String,
    'type': fields.String,
    'year': fields.Integer,
    'isNew': fields.Boolean
})

# definição de modelo que será validado ao receber put
modelUpdate = api.model('CarModelUpdate', {
    'name': fields.String,
    'type': fields.String,
    'year': fields.Integer,
    'isNew': fields.Boolean
})

hostName = environ.get('SERVER_HOST', 'localhost')

idCreate = int()

# rota padrao desse controller


@api.route('/')
class CarDealerController(Resource):
    # anotando o método get para realizar a busca de veiculos
    @api.response(200, "Busca realizada com sucesso")  # noqa documentação para tipo de respostas
    def get(self):
        # instancio o objeto CarService() que contem as implementacoes do servico de carros
        carService = CarService()

        # retorno o resultado da procura de itens para uma variavel result
        result = carService.getAllItens()

        # transformo em um json o resultado da lista fazendo um foreach em cada 
        # item da lista e concatenando os itens na variavel jsonResult
        jsonResult = json.dumps([ob.__dict__ for ob in result])

        # retorno o jsonResult com um código 200
        return jsonResult, 200

    @api.expect(modelInsert)  # espera modelo ao criar novo veiculo
    @api.response(201, description="Objeto criado com sucesso")
    def post(self):
        # instancio o objeto CarService() que contem as implementacoes do servico de carros
        carService = CarService()

        # retorno o resultado da procura de itens para uma variavel result

        carInsert = CarInsertRequestDTO()

        carInsert.carName = request.json.get("name")
        carInsert.carType = request.json.get("type")
        carInsert.yearModel = request.json.get("year")
        carInsert.isNew = request.json.get("isNew")

        idCreate = carService.addNewItem(carInsert)

        response = CarInsertResponseDTO()
        response.carName = carInsert.carName
        response.carType = carInsert.carType
        response.yearModel = carInsert.yearModel
        response.isNew = carInsert.isNew
        response.id = idCreate

        jsonResult = json.dumps(response.__dict__)

        return jsonResult, 201

@api.route('/<id>')
class CarsDealerController(Resource):
    # anotando o método get para realizar a busca de veiculos
    @api.response(200, "Busca realizada com sucesso")  # noqa documentação para tipo de respostas
    def get(self, id: int):
        # instancio o objeto CarService() que contem as implementacoes do servico de carros
        carService = CarService()

        # retorno o resultado da procura de itens para uma variavel result
        result = carService.getCarById(id)

        # transformo em um json o resultado da lista fazendo um foreach em cada 
        # item da lista e concatenando os itens na variavel jsonResult
        jsonResult = json.dumps(result.__dict__)

        # retorno o jsonResult com um código 200
        return jsonResult, 200

    @api.expect(modelUpdate)  # espera modelo ao atualizar veiculo
    @api.response(200, "Atualizado com sucesso")
    def put(self, id: int):
        # instancio o objeto CarService() que contem as implementacoes do servico de carros
        carService = CarService()

        # retorno o resultado da procura de itens para uma variavel result

        carUpdate = CarUpdateRequestDTO()

        carUpdate.carName = request.json.get("name")
        carUpdate.carType = request.json.get("type")
        carUpdate.yearModel = request.json.get("year")
        carUpdate.isNew = request.json.get("isNew")
        carUpdate.id = id

        idCreate = carService.updateCar(carUpdate)

        return "Atualizado com sucesso", 200

    @api.response(200, "Apagado com sucesso")
    def delete(self, id: int):
        # instancio o objeto CarService() que contem as implementacoes do servico de carros
        carService = CarService()

        idCreate = carService.deleteCar(id)

        return "Apagado com sucesso", 200
