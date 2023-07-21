import json
def apagar_notas_de_todos_alunos(alunos,notas):
        for aluno in alunos:
            print(f'\n{aluno}')
            for nota in notas:
                notas.clear()
            print('\nAs notas dos alunos foram removidas com sucesso.')

def apagar_notas_de_alunos_da_base_de_dados():
    dict_db = {}
    with open('./base_de_dados.json', 'r') as db:
        dict_db = json.load(db)

    with open('./base_de_dados.json', 'w') as db:
        try:
            apagar_notas_de_todos_alunos(dict_db['alunos'], dict_db['notas'])
            json.dump(dict_db, db)
        except Exception:
            json.dump(dict_db, db)