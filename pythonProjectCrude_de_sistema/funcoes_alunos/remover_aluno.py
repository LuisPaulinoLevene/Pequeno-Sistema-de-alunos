import json
import os
def remover_aluno(alunos: list):

    id = input("\nQual ID: ")
    os.system('cls')
    for aluno in alunos:
        if aluno['id'] == id:
            alunos.remove(aluno)
            print(f'\nAluno de {aluno} foi removido com sucesso!')
            break
    else:
        print('\nPor favor! Introduza o seu ID.')


def remover_aluno_da_base_de_dados():
    dict_db = {}
    with open('./base_de_dados.json','r') as db:
        dict_db = json.load(db)

    with open('./base_de_dados.json', 'w') as db:
        try:
            remover_aluno(dict_db['alunos'])
            json.dump(dict_db,db)
        except Exception:
            json.dump(dict_db,db)