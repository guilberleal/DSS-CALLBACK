import sqlite3
import os


def iniciarbc(pessoa):
    # Conectando ao banco de dados (ou criando-o se não existir)
    conexao = sqlite3.connect('banco_de_dados.db')

    # Criando um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Criando a tabela de nomes femininos
    cursor.execute('''CREATE TABLE IF NOT EXISTS nomes_femininos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT)''')


    # Função para incluir um nome feminino na tabela
    def incluir_nome_feminino(nome):
        cursor.execute("SELECT nome FROM nomes_femininos WHERE nome = ?", (nome,))
        resultado = cursor.fetchone()
        if resultado:
            print("Nome já existe na tabela de nomes femininos.")
        else:
            cursor.execute("INSERT INTO nomes_femininos (nome) VALUES (?)", (nome,))
            conexao.commit()
            print("Nome feminino incluído com sucesso.")

    # Função para consultar os nomes femininos na tabela
    def consultar_nomes_femininos(nome):
        cursor.execute("SELECT nome FROM nomes_femininos WHERE nome = ?", (nome,))
        resultado = cursor.fetchone()
        if resultado:
            return 'f'
        else:
            return 'nd'

    # Criando a tabela de nomes masculinos
    cursor.execute('''CREATE TABLE IF NOT EXISTS nomes_masculinos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT)''')

    # Função para incluir um nome masculino na tabela
    def incluir_nome_masculino(nome):
        cursor.execute("SELECT nome FROM nomes_masculinos WHERE nome = ?", (nome,))
        resultado = cursor.fetchone()
        if resultado:
            print("Nome já existe na tabela de nomes masculinos.")
        else:
            cursor.execute("INSERT INTO nomes_masculinos (nome) VALUES (?)", (nome,))
            conexao.commit()
            print("Nome masculino incluído com sucesso.")


    # Função para consultar os nomes masculinos na tabela
    def consultar_nomes_masculinos(nome):
        cursor.execute("SELECT nome FROM nomes_masculinos WHERE nome = ?", (nome,))
        resultado = cursor.fetchone()
        if resultado:
            return 'm'
        else:
            return 'nd'
        


    def painel(pessoa):
        consulta_feminino = consultar_nomes_femininos(pessoa)
        consulta_masculino = consultar_nomes_masculinos(pessoa)

        if consulta_feminino == 'nd' and consulta_masculino == 'nd':
            print('O nome fornecido ainda não existe em nossa base de dados, informe se o nome é feminino ou masculino.')
            genero = int(input('Digite 1 para feminino e 2 para masculino.\n'))
            if genero == 1:
                incluir_nome_feminino(pessoa)
                return 'f'
            elif genero == 2:
                incluir_nome_masculino(pessoa)
                return 'm'
            else:
                print('Essa não é uma opção válida.')
                input('')
                os.system('cls') or None
                return pergunta_genero(pessoa)
        return consulta_feminino

    
    def pergunta_genero(pessoa):
        print('O nome fornecido ainda não existe em nossa base de dados, informe se o nome é feminino ou masculino.')
        genero = int(input('Digite 1 para feminino e 2 para masculino.\n'))
        if genero == 1:
            incluir_nome_feminino(pessoa)
            return 'f'
        elif genero == 2:
            incluir_nome_masculino(pessoa)
            return 'm'
        else:
            print('Essa não é uma opção válida.')
            input('')
            os.system('cls') or None
            return pergunta_genero(pessoa)
        

    return painel(pessoa)


def configb():
    conexao = sqlite3.connect('banco_de_dados.db')

    cursor = conexao.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS nomes_femininos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT)''')
    
    def incluir_nome_feminino(nome):
        cursor.execute("SELECT nome FROM nomes_femininos WHERE nome = ?", (nome,))
        resultado = cursor.fetchone()
        if resultado:
            print("Nome já existe na tabela de nomes femininos.")
        else:
            cursor.execute("INSERT INTO nomes_femininos (nome) VALUES (?)", (nome,))
            conexao.commit()
            print("Nome feminino incluído com sucesso.")
    
    def excluir_nome_feminino(nome):
        cursor.execute("SELECT nome FROM nomes_femininos WHERE nome = ?", (nome,))
        resultado = cursor.fetchone()
        if resultado:
            cursor.execute("DELETE FROM nomes_femininos WHERE nome = ?", (nome,))
            conexao.commit()
            print("Nome feminino excluído com sucesso.")
        else:
            print("Nome não encontrado na tabela de nomes femininos.")   

   
    
    
    
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS nomes_masculinos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT)''')
    

    def incluir_nome_masculino(nome):
        cursor.execute("SELECT nome FROM nomes_masculinos WHERE nome = ?", (nome,))
        resultado = cursor.fetchone()
        if resultado:
            print("Nome já existe na tabela de nomes masculinos.")
        else:
            cursor.execute("INSERT INTO nomes_masculinos (nome) VALUES (?)", (nome,))
            conexao.commit()
            print("Nome masculino incluído com sucesso.")

    

    def excluir_nome_masculino(nome):
        cursor.execute("SELECT nome FROM nomes_masculinos WHERE nome = ?", (nome,))
        resultado = cursor.fetchone()
        if resultado:
            cursor.execute("DELETE FROM nomes_masculinos WHERE nome = ?", (nome,))
            conexao.commit()
            print("Nome masculino excluído com sucesso.")
        else:
            print("Nome não encontrado na tabela de nomes masculinos.")
    
    os.system('cls') or None
    print(' 1 = Incluir nome ao banco')
    print(' 2 = Excluir nome do banco')
    print(' 3 = Voltar ao menu principal\n')
    resposta = str(input(''))
    if resposta == '3':
        return 0
    if resposta not in ['1', '2', '3']:
        os.system('cls') or None
        print('Essa não é uma resposta válida')
        input('')
        os.system('cls') or None
        configb()

    os.system('cls') or None
    gen = int(input('1 para nome feminino e 2 para nome masculino\n'))
    os.system('cls') or None
    pessoa = str(input('Digite o nome da pessoa: '))
    os.system('cls') or None
    if resposta == '1':
        if gen == 1:
            incluir_nome_feminino(pessoa)
            input('\nRetornar ao menu')
            configb()
        elif gen == 2:
            incluir_nome_masculino(pessoa)
            input('\nRetornar ao menu')
            configb()
        else:
            print('Essa não é uma resposta válida')
            input('')
            configb()

    elif resposta == '2':
        if gen == 1:
            excluir_nome_feminino(pessoa)
            input('\nRetornar ao menu')
            configb()
        elif gen == 2:
            excluir_nome_masculino(pessoa)
            input('\nRetornar ao menu')
            configb()
        else:
            print('Essa não é uma resposta válida')
            input('')
            configb()
