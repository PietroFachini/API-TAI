from flask import Flask, jsonify, request, render_template, redirect
from aluno import Aluno

app = Flask(__name__)

alunos = []

@app.route("/", methods=["GET"])
def pagina_inicial():
    return render_template("index.html", alunos=alunos)

@app.route("/alunos", methods=["GET"])
def listar_alunos():
    return jsonify([aluno.to_dict() for aluno in alunos])

@app.route("/alunos", methods=["POST"])
def adicionar_aluno():
    nome = request.form["nome"]
    idade = int(request.form["idade"])
    novo_aluno = Aluno(nome, idade)
    alunos.append(novo_aluno)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)