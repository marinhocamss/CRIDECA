from doctest import debug
from flask import Flask, render_template, request, redirect, url_for, flash
from model import enviar, salvar, dt, mostrar, cadastrar
app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def ola():
    if request.method == "POST":
        nome = request.form.get("nome")
        senha = request.form.get("senha")
        dados = mostrar()
        for i in dados:
            if nome == i[0] and senha == i[1]:
                return redirect("/nota")
            
        return f"<h1>O usuario {nome} nao existe no sistema</h1>"
        
    return render_template("longe2.html")

@app.route("/signup", methods = ["POST", "GET"])
def signup():
    if request.method == "POST":
        nome = request.form.get("usuario")
        senha = request.form.get("senha")
        cadastrar(nome, senha)
        return redirect('/')
    return render_template("singup.html")

@app.route("/nota", methods = ["POST", "GET"])
def nota():
    if request.method == "POST":
        data = request.form.get("data")
        data = dt(data)
        professor = request.form.get("professor")
        aluno = request.form.get("aluno")
        periodo = request.form.get("periodo")
        corpo = request.form.get("corpo")
        enviar(data, professor, aluno, periodo, corpo)
        salvar(aluno, periodo, data)
        flash("Nota enviada com sucesso!")
        #return redirect("/sucesso")
    return render_template("teste.html")

@app.route("/sucesso", methods = ["POST", "GET"])
def sucesso():
    return render_template("sucesso.html")

if __name__ == "__main__":
    app.secret_key = "super secret key"
    app.run(debug=True)