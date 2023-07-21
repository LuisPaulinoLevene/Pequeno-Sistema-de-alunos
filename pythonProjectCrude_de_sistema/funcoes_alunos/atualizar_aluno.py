import json
import os

def atualizar_aluno(alunos):
    id = input("\nQual ID: ")
    os.system('cls')
    for aluno in alunos:
        if aluno['id'] == id:
            print('\nPreenche os espacos que pretende actualizar')
            nome = input('\nnome: ')
            apelido = input('\napelido: ')
            idade = input('\nidade: ')
            os.system('cls')

            aluno['nome'] = nome if nome !='' else aluno['nome']
            aluno['apelido'] = apelido if apelido !='' else aluno['apelido']
            aluno['idade'] = idade if idade !='' else aluno['idade']
            print(f'\nO aluno foi atualizado com sucesso! Caso os dados estiverem incorrecto reatualiza-os. Confira-os a seguir:')
            print(f'Nome: {nome} {apelido}, Idade: {idade}, ID: {id}.')
            break
    else:
        print('\nPor favor! Introduza o seu ID.')

def atualizar_aluno_na_base_de_dados():
    dict_db = {}
    with open('./base_de_dados.json','r') as db:
        dict_db = json.load(db)

    with open('./base_de_dados.json', 'w') as db:
        try:
            atualizar_aluno(dict_db['alunos'])
            json.dump(dict_db,db)
        except Exception:
            json.dump(dict_db,db)