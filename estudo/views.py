from estudo import app
from flask import render_template, url_for #quando for referenciar um link da sua view tem q usar url_for, pq aí vc n precisa se preocupar com a rota em si, so passar a rota da sua view(o nome dela 'nova'), a rota('o nome dela /contato')pode ser q mude, mas o nome da funçao dificilmente ela vai mudar.
@app.route('/') #@ significa quue vai ser um decorator, so a / é pq ele vai pegar desde a raiz do app.
def homepage():#renderizar a pag.
    usuario = 'Moises'
    idade = 16
    altura = 1.87

    dicionario= { #com um dicionario eu n preciso passar diversoas variaveis,consigo utilçizar apenas 1 'dicionario'.fazendo essa metodologia, 1 recupero(usuario, idade e altura),passo tudo pro dicionario, dicionario passa tudo como 1 variavel(dicionario=dicionario)e dps no index eu recupero esse dicionario e passo qual o parãmetro que eu quero: dicionario.usuario; dicionario.idade; e dicionario.altura.
        'usuario' : usuario,
        'idade' : idade,
        'altura': altura
    }


    return render_template('index.html', dicionario=dicionario ) #toda variavel que estivermos recuperando{{usuario}} sempre dentro de chave dupla. olha essa variavel que tem dentro desse template aqui, ent ela vai ta buscando essa variavel chamada usuario.

@app.route('/contato') #outra pag'/nova/'
def nova():#renderizar a pag.
    return 'outra view'

