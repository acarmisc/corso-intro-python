from flask import Flask
from oggetti import Automobile


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/saluta/<nome>')
def saluta(nome):
	return 'Ciao %s' % nome

@app.route('/somma/<int:a>/<int:b>')
def somma(a, b):
	somma = a + b
	return "%s" % somma

@app.route('/auto/<nome>/<anno>/<marca>/<consumo>')
def crea_automobile(nome, anno, marca, consumo):
	auto = Automobile(nome, anno, marca, consumo) 
	return auto.nome

app.run()
