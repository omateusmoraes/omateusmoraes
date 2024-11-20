from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agendamentos.db'  # Configuração do banco de dados SQLite
db = SQLAlchemy(app)

# Modelo para a tabela de agendamentos
class Agendamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10), nullable=False)
    hora = db.Column(db.String(5), nullable=False)
    servico = db.Column(db.String(50), nullable=False)
    profissional = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
    # Exemplo simples de consulta aos agendamentos já salvos
    agendamentos = Agendamento.query.all()
    return render_template('index.html', agendamentos=agendamentos)

@app.route('/novo_agendamento', methods=['POST'])
def novo_agendamento():
    # Obtém os dados do formulário
    data = request.form['data']
    hora = request.form['hora']
    servico = request.form['servico']
    profissional = request.form['profissional']

    # Cria um novo objeto de agendamento
    novo_agendamento = Agendamento(data=data, hora=hora, servico=servico, profissional=profissional)

    # Adiciona e commita no banco de dados
    db.session.add(novo_agendamento)
    db.session.commit()

    # Redireciona de volta para a página inicial após adicionar
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Cria as tabelas no banco de dados se ainda não existirem
    db.create_all()
    # Inicia o servidor Flask
    app.run(debug=True)
