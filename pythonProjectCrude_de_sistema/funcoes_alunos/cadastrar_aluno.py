import json
import os

def cadastrar_aluno(alunos: list):
    print('\nPreenche os espacos a seguir.\n')
    nome = input("\nNome: ")
    os.system('cls')
    apelido = input("\nApelido: ")
    os.system('cls')
    idade = input("\nIdade: ")
    os.system('cls')
    id = input("\nID: ")
    os.system('cls')
    print('\nO aluno foi cadastrado com com sucesso! Confira abaixo, caso os dados estiverem incorrectos, atualiza_os.')
    print(f'Nome: {nome} {apelido}, Idade: {idade}, ID: {id}.')

    aluno = {
        "nome": nome,
        "apelido": apelido,
        "idade": idade,
        'id': id
        }

    alunos.append(aluno)

def criar_base_de_dados():
    dict_db = {}
    with open('./base_de_dados.json','r') as db:
        dict_db = json.load(db)

    with open('./base_de_dados.json', 'w') as db:
        try:
            cadastrar_aluno(dict_db['alunos'])
            json.dump(dict_db,db)
        except Exception as _:
            json.dump(dict_db,db)

