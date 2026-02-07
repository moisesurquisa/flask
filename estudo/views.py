from estudo import app
from flask import render_template, url_for #quando for referenciar um link da sua view tem q usar url_for, pq aí vc n precisa se preocupar com a rota em si, so passar a rota da sua view(o nome dela 'nova'), a rota('o nome dela /contato')pode ser q mude, mas o nome da funçao dificilmente ela vai mudar.
@app.route('/') #@ significa quue vai ser um decorator, so a / é pq ele vai pegar desde a raiz do app.
def homepage():#renderizar a pag.
    return render_template('index.html')

@app.route('/contato') #outra pag'/nova/'
def nova():#renderizar a pag.
    return 'outra view'

