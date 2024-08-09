from flask import Flask, render_template, redirect

app = Flask(__name__)

# TELA HOME
@app.route('/')
def home():
    return render_template("home.html")

# DADOS BANCÁRIOS DO USUÁRIO
@app.route('/banco')
def banco():
    return render_template("banco.html")

# CONTA DO USUÁRIO(LOGIN/CADASTRO)
@app.route('/cadastro')
def cadastro():
    return render_template("criar_conta.html")

@app.route('/login')
def login():
    return render_template("acessar_conta.html")

# CRIAÇÃO DO PROJETO 
@app.route('/cria_projeto')
def criacao_projeto():
    return render_template("criação_do_projeto_1.html")

@app.route('/cria_projeto2')
def criacao_projeto2():
    return render_template("criação_do_projeto_2.html")

@app.route('/perfil')
def perfil():
    return render_template("perfil.html")

#APP RUN (RODA A APLICAÇÃO )
app.run(host='0.0.0.0',port=5000, debug=True)