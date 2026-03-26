from flask import Flask, jsonify
from flask import request
from aluno import Aluno

app = Flask(__name__)
alunos = []

aluno1 = Aluno("João", 17)

aluno1.adicionar_nota(6)
aluno1.adicionar_nota(7)
aluno1.adicionar_nota(8)

aluno2 = Aluno("Maria", 16)

aluno2.adicionar_nota(5)
aluno2.adicionar_nota(6)
aluno2.adicionar_nota(7)

alunos.append(aluno1)
alunos.append(aluno2)

@app.route("/alunos", methods=["GET"])
def listar_alunos():
    return jsonify([aluno.to_dict() for aluno in alunos])

@app.route("/alunos", methods=["POST"])
def adicionar_aluno():
    dados = request.get_json()
    novo_aluno = Aluno(dados["nome"], dados["idade"])
    alunos.append(novo_aluno)
    return jsonify(novo_aluno.to_dict()), 201

if __name__ == "__main__":
    app.run(debug=True)