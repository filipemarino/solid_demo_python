from app import app
from os import environ

# ponto inicial do programa
# aqui será configurado a aplicação para ficar rodando no formato "listner" para atender as requisições que forem enviadas
# foi configurada para receber requisições simultâneas com threaded = true

# o proximo ponto da aplicação é o __init__.py da pasta app

if __name__ == '__main__':
    SERVER_HOST = environ.get('SERVER_HOST', 'localhost')
    app.run(
        host=SERVER_HOST, 
        port=5500, 
        debug=(not environ.get('ENV') == 'PRODUCTION'), 
        threaded=True)  # noqa
