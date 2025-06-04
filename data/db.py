import pymysql
from tkinter import messagebox

# Função utilitária para obter uma nova conexão
def get_conexao():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='sgea'
    )

def inserir_usuario():
    try:
        conn = get_conexao()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Usuario(nome_usuario, senha) VALUES ('admim', 'sgea2025')")
        conn.commit()
        print("INSERIDO COM SUCESSO")
    except Exception as e:
        print("Erro ao inserir usuário:", e)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def buscar_usuario(nome, senha):
    try:
        conn = get_conexao()
        cursor = conn.cursor()
        cursor.execute("SELECT nome_usuario, senha FROM Usuario WHERE nome_usuario = %s and senha = %s", (nome, senha))
        result = cursor.fetchone()
        return result
    except Exception as e:
        print("Erro ao buscar usuário:", e)
        return None
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def inserir_produtos(nome_produto, categoria, preco, validade, localidade):
    try:
        conn = get_conexao()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Produto(nome_produto, categoria, preco, data_validade, localidade) 
            VALUES (%s, %s, %s, %s, %s)
        """, (nome_produto, categoria, preco, validade, localidade))
        conn.commit()
        messagebox.showinfo("Sucesso!", "Produto inserido com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro!", "Produto não inserido", e)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def pesquisar_produto():
    try:
        conn = get_conexao()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT p.id_produto, nome_produto, qtd_produto, localidade
            FROM Produto AS P
            LEFT JOIN Estoque AS E ON P.id_produto = E.id_produto
        """)
        resultado = cursor.fetchall()
        return resultado
    except Exception as e:
        print("Erro na pesquisa de produto:", e)
        return []
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

def adicionar_produtos(produto, quantidade):
    try:
        conn = get_conexao()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Estoque (id_produto, qtd_produto) VALUES (%s, %s)", (produto, quantidade))
        conn.commit()
        messagebox.showinfo("Sucesso!", "Quantidade atualizada!")
    except Exception as e:
        messagebox.showerror("Erro!", "Produto não atualizado", e)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def remover_produtos(produto, quantidade):
    try:
        conn = get_conexao()
        cursor = conn.cursor()
        cursor.execute("UPDATE Estoque SET qtd_produto = qtd_produto - %s WHERE id_produto = %s", (quantidade, produto))
        conn.commit()
        messagebox.showinfo("Sucesso!", "Quantidade foi alterada!")
    except Exception as e:
        messagebox.showerror("Erro!", "Quantidade não atualizada!", e)

    finally:
        if cursor: cursor.close()
        if conn: conn.close()
