from flask import render_template, url_for, request
from app import app
from db import mysql

@app.route("/")
def index():
    return render_template ('index.html')
    
@app.route("/quemsomos")
@app.route("/templates/quemsomos.html")
def quemsomos():
    return render_template('quemsomos.html')

@app.route("/contato", methods=('GET', 'POST'))
def contato():
    if request.method =='POST':
        email=request.form['email']
        assunto=request.form['assunto']
        descricao=request.form['descricao']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contatos(email, assunto, descricao) VALUES (%s, %s, %s)", (email, assunto, descricao))
        mysql.connection.commit()
        cur.close()
        return 'sucesso'
    return render_template('contato.html')

@app.route('/users')
def users():
    cur=mysql.connection.cursor()
    users=cur.execute('SELECT * FROM contatos')
    if users>0:
        userDetails=cur.fetchall()
        return render_template("users.html",userDetails=userDetails)




