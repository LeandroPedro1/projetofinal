from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/frete/')
def frete():
    return render_template('frete.html')


@app.route('/login/')
def login():
    return render_template('login.html')


@app.route('/pedidos/')
def pedidos():
    return render_template('pedidos.html')


@app.route('/about/')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
