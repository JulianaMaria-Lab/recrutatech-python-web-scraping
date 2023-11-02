from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import re

link = "http://localhost:8000"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
requisicao = requests.get(link, headers=headers)
site = BeautifulSoup(requisicao.text, "html.parser")
# profissao = site.findAll("h4")
sobre = site.findAll("pre")
# pessoa = site.findAll("h2")
profissao = site.findAll("h4", {"class": "profissao"})
pessoa = site.findAll("h2", {"class": "nome"})
codigo = site.findAll("h3", {"class": "codigo"})

def profissoes():
    for x in profissao:
        print(x.text, x.next_sibling)

def qtd_pessoa_profissao(a):
    cont = 0
    for x in profissao:
        if(a == x.text):
            cont = cont + 1
    print(cont)


def mostrarCodigoProfissao(a):
    z = []
    r = []
    o = []
    t = 0
    for x in profissao:
        z.append(x.text)

    for d in z:
        if (a["cargo"].lower() == d.lower()):
            for e in codigo:
                r.append(e.text)
            o.append(r[t])

        t = t + 1
    return jsonify(o)

def matchProfissao(a):
    lista_profissao = []
    lista_codigo = []
    lista_sobre = []
    codigos = []
    sobres = []
    verificacao = []
    matchs = []
    contador = 0
    v_conhecimento = 0
    v_habilidade = 0
    v_atitude = 0

    for p in profissao:
        lista_profissao.append(p.text)

    for p in lista_profissao:
        if (a["cargo"].lower() == p.lower()):
            for s in sobre:
                so = s.text
                sob = re.sub(r'[.,"\'-?:!;]', '', so)
                lista_sobre.append(sob)
            sobres.append(lista_sobre[contador])

            for c in codigo:
                lista_codigo.append(c.text)
            codigos.append(lista_codigo[contador])

        contador = contador + 1
    
    contador = 0
    
    for s in sobres:
        for palavra in s.split():
            for conhecimento in a["conhecimentos"]:
                if(palavra.lower() == conhecimento.lower()):
                    v_conhecimento = v_conhecimento + 1

            for habilidade in a["habilidades"]:
                if(palavra.lower() == habilidade.lower()):
                    v_habilidade = v_habilidade + 1

            for atitude in a["atitudes"]:
                if(palavra.lower() == atitude.lower()):
                    v_atitude = v_atitude + 1

        v = [v_conhecimento, v_habilidade, v_atitude]
        verificacao.append(v)
        total = v_conhecimento + v_habilidade + v_atitude 
        if(total > 2):
            matchs.append(codigos[contador])
        contador = contador + 1
        v_conhecimento = 0
        v_habilidade = 0
        v_atitude = 0
                
    return jsonify(verificacao)
                 

app = Flask(__name__)
CORS(app)

@app.route('/scraping', methods=['POST'])
def ask_question():
    try:
        # data = request.data.decode('utf-8')
        data = request.json
        return matchProfissao(data)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)