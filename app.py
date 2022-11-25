import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

app=Flask("__name__")



basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Reporter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String(100), unique=True, nullable=False)
    assunto=db.Column(db.String(300), nullable=False)
    descricao=db.Column(db.String(500), nullable=False)
    def __repr__(self):
        return f'<Reporter {self.email}>'
    


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
        p=Reporter(email=email, assunto=assunto, descricao=descricao)
        db.session.add(Reporter(email=email, assunto=assunto, descricao=descricao))
        db.session.commit()
        # return redirect(url_for('base.html'))


    return render_template('contato.html')



if __name__ == "__main__":
    app.run(debug= True)




