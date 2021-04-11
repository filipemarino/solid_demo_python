# sobre as bibliotecas utilizadas:
# Flask: Biblioteca que é responsavel por disponibilizar o WSGI (Web Server Gateway Interface) - Em outras palavras, a disponibilização do framework do python em acesso pela rede por chamadas
# Blueprint: Registro de aplicações num prefixo de URL ('cardealer') ou subdominio
# Flask RestX: Adiciona suporte à APIs RESTful
# ProxyFix: Biblioteca que faz configuração de aplicações que precisam ser executadas atras de um proxy (opcional)

# uma vez executado, a aplicação Python está no ar e pode ser chamada via webservice REST

from flask import Flask, Blueprint
from flask_restx import Api
# from werkzeug.middleware.proxy_fix import ProxyFix
from presentation.webapi.controllers.CarDealerController import api as cardealer  # noqa

# instancio nova aplicacao Flask
app = Flask(__name__)
# app.wsgi_app = ProxyFix(app.wsgi_app)

# configuro o blueprint
blueprint = Blueprint('api', __name__)

# registramos o dominio do blueprint
app.register_blueprint(blueprint)

# configuramos a API do RestX
api = Api(app, title='Car Dealer API', version='1.0', description='API with endpoints for car dealer services', prefix='/api')  # noqa

# adicionado endpoint cardealer para rotas
api.add_namespace(cardealer, path='/cardealer')
