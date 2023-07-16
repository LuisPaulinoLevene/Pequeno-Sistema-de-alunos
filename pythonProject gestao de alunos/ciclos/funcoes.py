from alunos import funcoes

alunos =[]
notas = []

def ciclo_aluno(alunos):
    while True:
        print("""Escolha a sua opcao: 
                    1 - Cadastrar aluno
                    2 - Ver um aluno
                    3 - ver todos alunos
                    4 - Atualizar um aluno
                    5 - Remover um aluno
                    6 - Sair
              """)
        entrada = input("Escolha a sua opcao:  ")

        if entrada == "1":
            funcoes.cadastrar_aluno(alunos)
        elif entrada  == "2":
            funcoes.ver_um_aluno(alunos)
        elif entrada == '3':
            funcoes.ver_todos_alunos(alunos)
        elif entrada == '4':
            funcoes.atualizar_aluno(alunos)
        elif entrada == '5':
            funcoes.remover_aluno(alunos)
        elif entrada == '6':
            break

def ciclo_notas():
    while True:
        print("""Escolha a sua opcao: 
                    1 - lancar notas
                    2 - Ver notas de um aluno
                    3 - Ver notas de todos alunos
                    4 - Atualizar notas de um aluno
                    5 - Remover notas de um aluno
                    6 - Sair
              """)
        entrada = input("Escolha a sua opcao: ")

        if entrada == "1":
            funcoes.lancar_notas_de_um_aluno(alunos,notas)
        elif entrada == "2":
            funcoes.ver_notas_de_um_aluno(alunos,notas)
        elif entrada == '3':
            funcoes.ver_notas_de_todos_alunos(alunos, notas)
        elif entrada == '4':
            funcoes.atualizar_notas_de_aluno(alunos, notas)
        elif entrada == "5":
            funcoes.remover_notas_de_aluno(alunos, notas)
        elif entrada == "6":
            break

def ciclo():
    while True:
        print("""
            1 - Gerir alunos
            2 - Gerir Notas e Medias
              """)
        entrada = input("Escolha a sua opcao: ")
        if entrada == "1":
            ciclo_aluno(alunos)
        elif entrada == '2':
            ciclo_notas()
