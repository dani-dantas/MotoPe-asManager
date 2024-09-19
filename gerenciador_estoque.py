# src/inventory/gerenciador_estoque.py

import sqlite3

CAMINHO_BANCO_DADOS = 'data/inventory.db'

def criar_banco_dados():
    # Cria o banco de dados se ainda não existir
    conexao = sqlite3.connect(CAMINHO_BANCO_DADOS)
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            codigo_produto TEXT PRIMARY KEY,
            nome_produto TEXT,
            quantidade INTEGER
        )
    ''')
    conexao.commit()
    conexao.close()

def atualizar_estoque(codigo_produto, quantidade_vendida):
    # Atualiza o estoque, subtraindo a quantidade vendida
    conexao = sqlite3.connect(CAMINHO_BANCO_DADOS)
    cursor = conexao.cursor()
    cursor.execute('''
        UPDATE produtos 
        SET quantidade = quantidade - ?
        WHERE codigo_produto = ?
    ''', (quantidade_vendida, codigo_produto))
    conexao.commit()
    conexao.close()

def verificar_estoque(codigo_produto):
    # Verifica a quantidade atual do produto no estoque
    conexao = sqlite3.connect(CAMINHO_BANCO_DADOS)
    cursor = conexao.cursor()
    cursor.execute('''
        SELECT quantidade FROM produtos WHERE codigo_produto = ?
    ''', (codigo_produto,))
    resultado = cursor.fetchone()
    conexao.close()
    return resultado[0] if resultado else 0

# Inicializa o banco de dados (execute uma vez)
criar_banco_dados()
