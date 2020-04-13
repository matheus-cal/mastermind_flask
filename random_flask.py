from flask import Flask
# from func import num_ran, inicia, tentativa
from func import num_ran
from func import inicia
from func import tentativa

app = Flask(__name__)


@app.route("/gera_numero", methods=['GET'])
def foo1():
    return f'{num_ran()}'


@app.route("/inicia", methods=['GET'])
def foo2():

    return f'{inicia()}'


@app.route("/tentativa", methods=['GET'])
def foo3():
    return f'{tentativa()}'


if __name__ == "__main__":
    app.run(debug=True, port=8090)
