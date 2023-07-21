import json
import os

def ver_notas_de_um_aluno(alunos,notas):
    id = input("\nQual ID: ")
    os.system('cls')
    for aluno in alunos:
        if aluno['id'] == id:
            print(f'\n{aluno}')

    for nota in notas:
        if nota['id_de_aluno'] == id:
            print(nota)
            break
    else:
        print('\nPor favor! Introduza o seu ID.')




def ver_notas_de_um_aluno_da_base_de_dados():
    with open('./base_de_dados.json', 'r') as db:
        dict_db = json.load(db)
        ver_notas_de_um_aluno(dict_db['alunos'],dict_db['notas'])