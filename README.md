Aqui estou tentado fazer um integração de front-end e back-end para testar uma API.
A API já foi validada pelo Postman, mas estou tentado tornar em algo realmente funcinal para estudo.
# API-TAI

O que está acontecendo neste código:

• Flask(__name__) cria a aplicação web;
• A lista alunos simula um banco de dados em memória;
• Criamos dois objetos da classe Aluno;
• O decorador @app.route("/alunos", methods=["GET"]) define uma rota HTTP;
• Quando alguém acessa /alunos, a função listar_alunos() é executada;
• A list comprehension converte cada objeto em dicionário;
• jsonify() transforma os dicionários em JSON válido;
• debug=True ativa recarregamento automático e mensagens de erro detalhadas.

Importante: Objetos Python não podem ser enviados diretamente pela web. Por isso utilizamos o
método to_dict() para convertê-los antes de aplicar jsonify().

O fluxo da requisição GET será:

    Cliente → Flask → Função da rota → Objeto → Dicionário → JSON → Resposta HTTP

Execute a aplicação:

```bash
python app.py
