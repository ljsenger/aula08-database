from flask import Flask, render_template, request, json, url_for, redirect, make_response, flash, session
from config import Config
from app.forms import LoginForm
from app import app

modelos = { "0":  {"nome": "pegasus", "preco": 500, "promocao": False},
            "1":  {"nome": "vintage", "preco": 1500, "promocao": False},
            "2":  {"nome": "sport",   "preco": 1500, "promocao": True},
            "3":  {"nome": "eco",     "preco": 759, "promocao": True}
}
u = None
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    return render_template("index.html", name=name, u=u)

@app.route("/modelos")
def produtos():
    return render_template("produtos.html", m=modelos)

@app.route("/promocoes")
def promocoes():
    return render_template("promocoes.html", m=modelos)    

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Requisição de login para  {}, lembre-me={}'.format(form.usuario.data, form.lembre_me.data))
        session['user'] = form.usuario.data
        return redirect(url_for('index'))

    return render_template('login.html', title='Entrar', form=form)

def setUser(user):
    global u 
    u = user

def getUser():
    return u

@app.context_processor
def contextProc():
    return dict(getUser=getUser)