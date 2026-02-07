from estudo import app
from flask import render_template, url_for
@app.route('/') #@ significa quue vai ser um decorator, so a / é pq ele vai pegar desde a raiz do app.
def homepage():#renderizar a pag.
    return render_template('index.html')

@app.route('contato') #outra pag'/nova/'
def nova():#renderizar a pag.
    return 'outra view'

