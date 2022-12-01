
from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL
# from flask_bootstrap import Bootstrap
from db import mysql, app





def creat_app():
    from app import routes
    routes.init_app(app)
    return app

# Bootstrap(app)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSOWORD']=''
app.config['MYSQL_DB']='contatos'



app.run()