from ui.menu import Exibir_Menu
from ui.listagem import Listar_Clientes, Listar_Pets
from flask import Flask, render_template, request
from services.petshop_service import (
    Cadastrar_Clientes,
    Cadastrar_Pets,
    Cadastrar_Servicos,
    Relatorio,
    Buscar_Pet,
    Faturamento
)



app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/cadastrar_cliente", methods=["POST"])
def cadastrar_clientes():
    nome = request.form.get("nome")
    documento = request.form.get("documento")
    telefone = request.form.get("telefone")
    endereco = request.form.get("endereco")
    nomedopet = request.form.get("nome-pet")
    tipopet = request.form.get("tipo-pet")
    servico = request.form.get("servico")

    Cadastrar_Clientes(nome, documento, telefone, endereco)
    Cadastrar_Pets(documento, nomedopet, tipopet, servico)
    return "Cliente Cadastrado!"



if __name__ =="__main__":
    app.run()