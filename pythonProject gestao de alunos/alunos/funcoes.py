
def cadastrar_aluno(alunos):
    nome = input("Nome: ")
    apelido = input("Apelido: ")
    idade = input("Idade: ")
    id = input("ID: ")
    print(f'Nome: ', nome,apelido, '\nidade:',idade, '\nid: ',id)

    aluno = {
        "nome": nome,
        "apelido": apelido,
        "idade": idade,
        "id ": id
        }

    alunos.append(aluno)

def lancar_notas_de_um_aluno(alunos,notas):
    id = input("Qual ID: ")
    for aluno in alunos:
        if aluno["id "] == id:
            print(aluno)

    nota1 = input('nota1: ')
    try:
        nota1 = float(nota1)
    except ValueError:
        nota1 = 0.0
        print('Erro. digita um numero decimal separado com ponto, como exemplo:', nota1)

    nota2 = input('nota2: ')
    try:
        nota2 = float(nota2)
    except ValueError:
        nota2 = 0.0
        print('Erro. digita um numero decimal separado com ponto, como exemplo:', nota2)

    nota3 = input('nota3: ')
    try:
        nota3 = float(nota3)
    except ValueError:
        nota3 = 0.0
        print('Erro. digita um numero decimal separado com ponto, como exemplo:', nota3)
    media = (nota1 + nota2 + nota3) / 3
    estado = ''
    if media >= 14:
        estado = 'Dispensou'
    elif media >= 10:
        estado = 'Passou'
    else:
        estado = 'Reprovou'
    print(['nota1: ', nota1, 'nota2: ', nota2, 'nota3: ', nota3], '\nMedia:', media, '\nEstado:', estado)
    nota_de_aluno = {
        'id_de_aluno': id,
        'nota1': nota1,
        'nota2': nota2,
        'nota3': nota3,
        'media': media,
        'estado': estado
        }
    notas.append(nota_de_aluno)


def ver_notas_de_um_aluno(alunos,notas):
    id = input("Qual ID: ")
    for aluno in alunos:
        if aluno["id "] == id:
            print(aluno)

    for nota in notas:
        if nota['id_de_aluno'] == id:

            print(nota)


def ver_um_aluno(alunos):

    id = input("Qual ID: ")
    for aluno in alunos:
        if aluno["id "] == id:
            print(aluno)





def ver_todos_alunos(alunos):
    for aluno in alunos:
        print('=='*60,'\n',aluno,'\n','=='*60)


def ver_notas_de_todos_alunos(alunos,notas):
    for aluno in alunos:
        print('=='*60,'\n',aluno)
        for nota in notas:
            if nota['id_de_aluno'] == aluno['id ']:
                print(nota,'\n', '=='*60)
                break
    pass

def atualizar_aluno(alunos):
    id = input("Qual ID: ")
    for aluno in alunos:
        if aluno['id '] == id:
            nome = input('nome: ')
            apelido = input('apelido: ')
            idade = input('idade: ')
            aluno['nome'] = nome if nome !='' else aluno['nome']
            aluno['apelido'] = apelido if apelido !='' else aluno['apelido']
            aluno['idade'] = idade if idade !='' else aluno['idade']
            print(aluno)
            break

def remover_aluno(alunos):
    id = input("Qual ID: ")
    for aluno in alunos:
        if aluno['id '] == id:
            alunos.remove(aluno)

def atualizar_notas_de_aluno(alunos, notas):
    id = input("Qual ID: ")
    for aluno in alunos:
        if aluno["id "] == id:
            print(aluno)

    for nota in notas:
        if nota['id_de_aluno'] == id:
            nota1 = input('nota1: ')
            try:
                nota1 = float(nota1)
            except ValueError:
                nota1 = 0.0
                print('Erro. digita um numero decimal separado com ponto, como exemplo:', nota1)

            nota2 = input('nota2: ')
            try:
                nota2 = float(nota2)
            except ValueError:
                nota2 = 0.0
                print('Erro. digita um numero decimal separado com ponto, como exemplo:', nota2)

            nota3 = input('nota3: ')
            try:
                nota3 = float(nota3)
            except ValueError:
                nota3 = 0.0
                print('Erro. digita um numero decimal separado com ponto, como exemplo:', nota3)
            media = (nota1 + nota2 + nota3) / 3
            estado = ''
            if media >= 14:
                estado = 'Dispensou'
            elif media >= 10:
                estado = 'Passou'
            else:
                estado = 'Reprovou'
            print(['nota1: ',nota1, 'nota2: ',nota2, 'nota3: ',nota3], '\nMedia:', media, '\nEstado:',estado)

            nota['nota1'] = nota1 if nota1 != '' else nota['nota1']
            nota['nota2'] = nota2 if nota2 != '' else nota['nota2']
            nota['nota3'] = nota3 if nota3 != '' else nota['nota3']
            nota['media'] = media if media != '' else nota['media']
            nota['estado'] = estado if estado != '' else nota[estado]
            print()

def remover_notas_de_aluno(alunos,notas):
    id = input("Qual ID: ")
    for aluno in alunos:
        if aluno["id "] == id:
            print(aluno)
    for nota in notas:
        if nota['id_de_aluno'] == id:
            notas.remove(nota)