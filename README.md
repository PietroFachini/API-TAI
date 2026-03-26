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
python app.py
Você verá no terminal que o servidor foi iniciado.
Teste no navegador:
http://127.0.0.1:5000/alunos
Se tudo estiver correto, será exibido um JSON contendo os alunos criados.
Observe também o terminal: Cada requisição realizada aparecerá registrada no log do servidor.