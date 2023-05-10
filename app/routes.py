from app import app
from flask import Flask, render_template, request, flash, redirect
import mysql.connector #pip install mysql-connector-python
import time

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='cadastro'
)

cursor = conexao.cursor()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastrado', methods=["POST"])
def cadastrar():

    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    
    if usuario != '':
        try:
            comandoInsert = f'INSERT INTO cliente (nome,senha) VALUES ("{usuario}","{senha}")'
            cursor.execute(comandoInsert)
            conexao.commit()
            flash('Cadastro realizado com sucesso!')
            time.sleep(1)
            return redirect('/cadastro')
        except mysql.connector.errors.IntegrityError as e:
            flash(
                f'Ocorreu um erro de integridade: {e}')
            time.sleep(1)
            return redirect('/cadastro')
    else:
        flash('Erro')
        time.sleep(1)
        return redirect('/cadastro')

@app.route('/exibir')
def exibir():
    ComandoListar = f'SELECT * FROM cliente'
    cursor.execute(ComandoListar)
    resultado = cursor.fetchall()
    return resultado

@app.route('/atualizar')
def renderAtualizar():
    return render_template('atualizar.html')

@app.route('/atualizardados', methods=["POST"])
def atualizarDados():
    usuario = request.form.get('usuario')
    flash('Atualização realizado com sucesso!')
    
    ComandoAtualizar = f'DELETE FROM cliente WHERE nome = "{usuario}"'
    cursor.execute(ComandoAtualizar)
    conexao.commit()
    return redirect('/cadastro')

@app.route('/deletar')
def deletar():
    return render_template('deletar.html')

@app.route('/deletando', methods=["POST"])
def deletando():
    usuario = request.form.get('usuario')
    flash('Usuario deletado com sucesso!')
    ComandoDeletar = f'DELETE FROM cliente WHERE nome = "{usuario}"'
    cursor.execute(ComandoDeletar)
    conexao.commit()
    return redirect('/deletar')