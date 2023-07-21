import os

from funcoes_alunos import cadastrar_aluno
from funcoes_alunos import ver_todos_alunos
from funcoes_alunos import ver_um_aluno
from funcoes_alunos import remover_aluno
from funcoes_alunos import atualizar_aluno
from funcoes_notas import lancar_notas_de_um_aluno
from funcoes_notas import ver_notas_de_todos_alunos
from funcoes_notas import ver_notas_de_um_aluno
from funcoes_notas import atualizar_notas_de_aluno
from funcoes_notas import remover_notas_de_aluno
from funcoes_alunos import apagar_todos_alunos
from funcoes_notas import apagar_notas_de_todos_alunos


def ciclo_aluno():
    while True:
        print("""\nO QUE DESEJA FAZER? \n
                    1 - Cadastrar aluno
                    2 - Ver todos alunos
                    3 - Ver um aluno
                    4 - Atualizar um aluno
                    5 - Remover um aluno
                    6 - Remover todos alunos
                    0 - Voltar
                    00 - Sair
              """)
        entrada = input("\nEscolha a sua opcao:  ")

        if entrada == "1":
            os.system('cls')
            cadastrar_aluno.criar_base_de_dados()
        elif entrada == "2":
            os.system('cls')
            ver_todos_alunos.ver_alunos_da_base_de_dados()
        elif entrada == '3':
            os.system('cls')
            ver_um_aluno.ver_alunos_da_base_de_dados()
        elif entrada == '4':
            os.system('cls')
            atualizar_aluno.atualizar_aluno_na_base_de_dados()
        elif entrada == '5':
            os.system('cls')
            remover_aluno.remover_aluno_da_base_de_dados()
        elif entrada == '6':
            os.system('cls')
            apagar_todos_alunos.apagar_alunos_da_base_de_dados()
        elif entrada == '0':
            os.system('cls')
            break
        elif entrada == '00':
            exit()

def ciclo_notas():
    while True:
        print("""\nO QUE DESEJA FAZER? \n
                    1 - lancar notas
                    2 - Ver notas de todos alunos
                    3 - Ver notas de um aluno
                    4 - Atualizar notas de um aluno
                    5 - Remover notas de um aluno
                    6 - Remover notas de todos alunos
                    0 - Voltar
                    00 - Sair
              """)
        entrada = input("\nEscolha a sua opcao: ")

        if entrada == "1":
            os.system('cls')
            lancar_notas_de_um_aluno.lancar_notas_base_de_dados()
        elif entrada == "2":
            os.system('cls')
            ver_notas_de_todos_alunos.ver_notas_de_todos_alunos_da_base_de_dados()
        elif entrada == '3':
            os.system('cls')
            ver_notas_de_um_aluno.ver_notas_de_um_aluno_da_base_de_dados()
        elif entrada == '4':
            os.system('cls')
            atualizar_notas_de_aluno.atualizar_notas_de_um_aluno_na_base_de_dados()
        elif entrada == "5":
            os.system('cls')
            remover_notas_de_aluno.remover_notas_de_aluno_da_base_de_dados()
        elif entrada == '6':
            os.system('cls')
            apagar_notas_de_todos_alunos.apagar_notas_de_alunos_da_base_de_dados()
        elif entrada == "0":
            os.system('cls')
            break
        elif entrada == '00':
            exit()

while True:
    print('\nBEM VINDO AO SISTEMA DE GESTAO DE ALUNOS')
    print("""\nO QUE DESEJA FAZER?
        1 - Gerir alunos
        2 - Gerir Notas
        00 - Sair
          """)
    entrada = input("\nEscolha a sua opcao: ")
    if entrada == "1":
        os.system('cls')
        ciclo_aluno()
    elif entrada == '2':
        os.system('cls')
        ciclo_notas()
    elif entrada == '0':
        exit()