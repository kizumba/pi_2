from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///meu_bd.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Estudante(db.Model):    
    ra = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    senha = db.Column(db.String)
    
    nome = db.Column(db.String(150))
    telefone = db.Column(db.String(11))
    email_alternativo = db.Column(db.String(100))
    rede_social = db.Column(db.String(100))
    hobby = db.Column(db.String(100))

    #trabalha = db.Column(db.Integer)
    periodo = db.Column(db.String(10))
    semana = db.Column(db.String(10))
    
    curso = db.Column(db.String(100))
    polo = db.Column(db.String(100))
    pi = db.Column(db.Integer)
    interesse_academico = db.Column(db.String(100))
    idioma = db.Column(db.String(50))


@app.route('/')
def homepage():
	estudantes = Estudante.query.all()
	return render_template('homepage.html', estudantes=estudantes)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=False)