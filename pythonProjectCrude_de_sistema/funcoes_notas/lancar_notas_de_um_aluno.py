import json
import os
def lancar_notas_de_um_aluno(alunos,notas):
    id = input('Qual ID: ')
    os.system('cls')
    for aluno in alunos:
        if aluno['id'] == id:
            print(f'\n{aluno}')
            print('Preenche as notas a seguir.')
            nota1 = input('\nnota1: ')
            os.system('cls')
            try:
                nota1 = float(nota1)
            except ValueError:
                nota1 = 0.0
                os.system('cls')
                print('Erro. digita um numero decimal separado com ponto, como exemplo:', nota1)

            nota2 = input('\nnota2: ')
            os.system('cls')
            try:
                nota2 = float(nota2)
            except ValueError:
                nota2 = 0.0
                os.system('cls')
                print('Erro. digita um numero decimal separado com ponto, como exemplo:', nota2)

            nota3 = input('\nnota3: ')
            os.system('cls')
            try:
                nota3 = float(nota3)
            except ValueError:
                nota3 = 0.0
                os.system('cls')
                print('Erro. digita um numero decimal separado com ponto, como exemplo:', nota3)
            media = (nota1 + nota2 + nota3) / 3

            estado = ''
            if media >= 14:
                estado = 'Dispensou'
            elif media >= 10:
                estado = 'Passou'
            else:
                estado = 'Reprovou'
            print(f'Nota 1: {nota1}, Nota 2: {nota2}, Nota 3: {nota3}, Media: {media}, Estado: {estado}')

            nota_de_aluno = {
                'id_de_aluno': id,
                'nota1': nota1,
                'nota2': nota2,
                'nota3': nota3,
                'media': media,
                'estado': estado
                }
            notas.append(nota_de_aluno)
            break
    else:
        print('\nPor favor! Introduza o seu ID.')



def lancar_notas_base_de_dados():
    dict_db = {}
    with open ('./base_de_dados.json', 'r') as db:
        dict_db = json.load(db)
    with open('./base_de_dados.json', 'w') as db:
        try:
            lancar_notas_de_um_aluno(dict_db['alunos'], dict_db['notas'])
            json.dump(dict_db, db)
        except Exception as _:
            json.dump(dict_db, db)
