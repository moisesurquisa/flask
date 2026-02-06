from estudo import app
from flask import render_template
@app.route('/') #@ significa quue vai ser um decorator, so a / é pq ele vai pegar desde a raiz do app.
def homepage():#renderizar a pag.
    return render_template('index.html')

@app.route('/nova/') #outra pag'/nova/'
def novapag():#renderizar a pag.
    return 'outra view'
