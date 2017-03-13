from flask import Flask, render_template, request
from oggetti import Automobile


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

"""
@app.route('/saluta/<nome>')
def saluta(nome):
	return 'Ciao %s' % nome
"""

@app.route('/somma/<int:a>/<int:b>')
def somma(a, b):
	somma = a + b
	return "%s" % somma

@app.route('/auto/<nome>/<anno>/<marca>/<consumo>')
def crea_automobile(nome, anno, marca, consumo):
	auto = Automobile(nome, anno, marca, consumo) 
	return auto.nome

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')

@app.route('/saluta', methods=['POST', 'GET'])
def saluta():
	name = request.form['name']
	return render_template('saluta.html', name=name)

@app.route('/nuovaauto')
def nuovaauto():
	return render_template('nuovaauto.html')

@app.route('/salvaauto', methods=['POST'])
def salvaauto():
	nome = request.form['name']
	anno = request.form['year']
	marca = request.form['brand']
	consumo = request.form['consumption']

	auto = Automobile(nome, anno, marca, consumo) 
	
	return render_template('salvaauto.html', name=auto.nome)	

app.run()

