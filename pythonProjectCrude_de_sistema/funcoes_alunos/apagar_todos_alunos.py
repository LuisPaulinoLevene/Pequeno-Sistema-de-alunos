import json
def apagar_todos_alunos(alunos):
    for aluno in alunos:
        alunos.clear()
        print(f'\nOs alunos foram removidos com sucesso.')

def apagar_alunos_da_base_de_dados():
    dict_db = {}
    with open('./base_de_dados.json', 'r') as db:
        dict_db = json.load(db)

    with open('./base_de_dados.json', 'w') as db:
        try:
            apagar_todos_alunos(dict_db['alunos'])
            json.dump(dict_db, db)
        except Exception:
            json.dump(dict_db, db)
