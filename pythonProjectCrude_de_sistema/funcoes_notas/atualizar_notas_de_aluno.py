import json
import os
def atualizar_notas_de_aluno(alunos, notas):
    id = input("Qual ID: ")
    os.system('cls')
    for aluno in alunos:
        if aluno['id'] == id:
            print(aluno)
        for nota in notas:
            if nota['id_de_aluno'] == id:

                nota1 = input('nota1: ')
                os.system('cls')
                try:
                    nota1 = float(nota1)
                except ValueError:
                    nota1 = 0.0
                    os.system('cls')
                    print('Erro. digita um numero decimal separado com ponto, como exemplo:', nota1)

                nota2 = input('nota2: ')
                os.system('cls')
                try:
                    nota2 = float(nota2)
                except ValueError:
                    nota2 = 0.0
                    os.system('cls')
                    print('Erro. digita um numero decimal separado com ponto, como exemplo:', nota2)

                nota3 = input('nota3: ')
                os.system('cls')
                try:
                    nota3 = float(nota3)
                except ValueError:
                    nota3 = 0.0
                    os.system('cls')
                    print('Erro. digita um numero decimal separado com ponto, como exe4wreszfdmplo:', nota3)
                media = (nota1 + nota2 + nota3) / 3
                estado = ''
                if media >= 14:
                    estado = 'Dispensou'
                elif media >= 10:
                    estado = 'Passou'
                else:
                    estado = 'Reprovou'
                print(f'Nota 1: {nota1}, Nota 2: {nota2}, Nota 3: {nota3}, Media: {media}, Estado: {estado}')

                nota['nota1'] = nota1 if nota1 != '' else nota['nota1']
                nota['nota2'] = nota2 if nota2 != '' else nota['nota2']
                nota['nota3'] = nota3 if nota3 != '' else nota['nota3']
                nota['media'] = media if media != '' else nota['media']
                nota['estado'] = estado if estado != '' else nota['estado']
                print(f'\nAs notas do aluno  foram removidas com sucesso.')
                break
        else:
            print('Por favor! Introduza o seu ID.')
            break
        break

def atualizar_notas_de_um_aluno_na_base_de_dados():
    dict_db = {}
    with open('./base_de_dados.json','r') as db:
        dict_db = json.load(db)

    with open('./base_de_dados.json', 'w') as db:
        try:
            atualizar_notas_de_aluno(dict_db['alunos'],dict_db['notas'])
            json.dump(dict_db,db)
        except Exception:
            json.dump(dict_db,db)