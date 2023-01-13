from flask import Flask, jsonify, request

app = Flask(__name__)

requisicao = [
    {
    "chave": 1,
    "assunto": "teste130123",
    "texto": "Corpo130123",
    "endereco": "joao.rcosta19@gmail.com"
    },
    {
    "chave": 2,
    "assunto": "teste130123",
    "texto": "Corpo130123",
    "endereco": "joao.r19@gmail.com"
    },
    {
    "chave": 3,
    "assunto": "teste130123",
    "texto": "Corpo130123",
    "endereco": "joao@gmail.com"
    }
]

#consultar todos 
@app.route("/listar", methods=['GET'])
def consultar():
    return jsonify(requisicao)

#consultar por chave
@app.route("/listar/<int:chave>", methods=['GET'])
def consultarChave(chave):
    for x in requisicao:
        if x.get('chave') == chave:
            return jsonify(x)
#editar 
@app.route("/alterar/<int:chave>", methods=['PUT'])
def editar(chave):
    alterar = request.get_json()
    for indice, req in enumerate(requisicao):
        if req.get('chave') == chave:
            requisicao[indice].update(alterar)
            return jsonify(requisicao[indice])

#criar
@app.route("/criar", methods=['POST'])
def criar():
    nova_req = request.get_json()
    requisicao.append(nova_req)
    return jsonify(requisicao)

#excluir
@app.route("/alterar/<int:chave>", methods=['DELETE'])
def excluir(chave):
    for indice, req in enumerate(requisicao):
        if req.get('chave') == chave:
            del requisicao[indice]
    return jsonify(requisicao)

app.run(port=5000,host='localhost',debug=True)