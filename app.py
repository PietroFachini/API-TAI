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

@app.route("/remover/<int:id>")
def remover_aluno(id):
    global alunos
    alunos = [aluno for aluno in alunos if aluno.id != id]
    return redirect("/")

# Rota para carregar os dados de um aluno
@app.route("/editar/<int:id>")
def editar_aluno(id):
    aluno = next((aluno for aluno in alunos if aluno.id == id), None)
    if aluno:
        return render_template("editar.html", aluno=aluno)
    return redirect("/")

# Rota para atualizar um aluno
@app.route("/atualizar/<int:id>", methods=["POST"])
def atualizar_aluno(id):
    aluno = next((aluno for aluno in alunos if aluno.id == id), None)
    if aluno:
        aluno.nome = request.form["nome"]
        aluno.idade = int(request.form["idade"])
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)