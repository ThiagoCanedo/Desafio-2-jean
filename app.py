
from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL
# from flask_bootstrap import Bootstrap
from routes import end
from db import mysql


app=Flask("__name__")


# def creat_app():
#     from app import route
#     route.init_app(app)
#     return app

# Bootstrap(app)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSOWORD']=''
app.config['MYSQL_DB']='contatos'

mysql.init_app(app)

app.register_blueprint(end)

if __name__=='__main__':
    app.run()