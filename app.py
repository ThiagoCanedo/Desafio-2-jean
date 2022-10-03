

from flask import Flask
from flask import render_template
app=Flask("__name__")






@app.route("/")
def index():
    return render_template ('index.html')
    
@app.route("/quemsomos")
@app.route("/templates/quemsomos.html")
def quemsomos():
    return render_template('quemsomos.html')

@app.route("/contato")
def contato():
    return render_template('contato.html')

if __name__ == "__main__":
    app.run(debug= True)

