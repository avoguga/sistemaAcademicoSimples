
import psycopg2 # Modulo para o Pgadmin
def linhas():
    print('-' * 60)
def consultarAlunos():
    try:
        connection = psycopg2.connect(database='SistemaAcademico',
                                      user='postgres',
                                      password='adm',
                                      host='localhost',
                                      port="5432")
        cursor = connection.cursor()
    except (Exception, psycopg2.Error) as error:
        print("Falha na conexao", error)
    postgreSQL_select_Query = "select * from aluno"
    try:
        cursor.execute(postgreSQL_select_Query)
        alunoData = cursor.fetchall()
        for row in alunoData:
            print("Matricula: ", row[0], )
            print("Nome: ", row[1], '\n')
            print("CPF: ", row[2], '\n')
            print("Email: ", row[3], '\n')
            print("Data de Nascimento: ", row[4], '\n')
            linhas()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
        if cursor is not None:
            cursor.close()
def consultarProfessores():
    try:
        connection = psycopg2.connect(database='SistemaAcademico',
                                      user='postgres',
                                      password='adm',
                                      host='localhost',
                                      port="5432")
        cursor = connection.cursor()
    except (Exception, psycopg2.Error) as error:
        print("Falha na conexao", error)
    postgreSQL_select_Query = "select * from professor"
    try:
        cursor.execute(postgreSQL_select_Query)
        alunoData = cursor.fetchall()
        for row in alunoData:
            print("Matricula Professor: ", row[0], )
            print("Nome do Professor: ", row[1], '\n')
            print("Email: ", row[2], '\n')
            print("Data de Nascimento: ", row[3], '\n')

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
        if cursor is not None:
            cursor.close()
#def consultarDisciplinas():
#def consultarTurmas():
def cadastrarAlunos():
    try:
        connection = psycopg2.connect(database='SistemaAcademico',
                                      user='postgres',
                                      password='adm',
                                      host='localhost',
                                      port="5432")
        cursor = connection.cursor()
    except (Exception, psycopg2.Error) as error:
        print("Falha na conexao", error)

    nomeAluno = input('Informe o nome do aluno: ')
    cpfAluno = input('Informe o CPF: ')
    emailAluno = input('Informe o email: ')
    dataNascAluno = input('Informe a data de nascimento: ')

    postgreSQL_select_Query = f"""INSERT INTO aluno( nome, cpf, email, data_nascimento)
    VALUES('{nomeAluno}', '{cpfAluno}', '{emailAluno}', '{dataNascAluno}')
    RETURNING matricula;
    """
    try:
        cursor.execute(postgreSQL_select_Query)
        alunoData = cursor.fetchall()
        connection.commit()
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
        if cursor is not None:
            cursor.close()
def alterarNomeAlunos():
    postgreSQL_select_Query = "select * from aluno"
    try:
        cursor.execute(postgreSQL_select_Query)
        alunoData = cursor.fetchall()
        for row in alunoData:
            print("Matricula: ", row[0], )
            print("Nome: ", row[1], '\n')
            print("CPF: ", row[2], '\n')
            print("Email: ", row[3], '\n')
            print("Data de Nascimento: ", row[4], '\n')
            linhas()
        matriculaAluno = input("Digite a matricula do aluno para poder alterar seus dados: ")
        query = "SELECT * FROM aluno WHERE matricula = %s"
        cursor.execute(query, (matriculaAluno))
        record = cursor.fetchone()
        nomeAluno = input("Informe o nome do Aluno ")
        sql = """UPDATE aluno SET nome = '{}' WHERE matricula = {};"""
        try:
            cursor.execute(sql.format(nomeAluno, matriculaAluno))
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if connection is not None:
                connection.close()
            if cursor is not None:
                cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
        if cursor is not None:
            cursor.close()
def alterarCPFAlunos():
    postgreSQL_select_Query = "select * from aluno"
    try:
        cursor.execute(postgreSQL_select_Query)
        alunoData = cursor.fetchall()
        for row in alunoData:
            print("Matricula: ", row[0], )
            print("Nome: ", row[1], '\n')
            print("CPF: ", row[2], '\n')
            print("Email: ", row[3], '\n')
            print("Data de Nascimento: ", row[4], '\n')
            linhas()
        matriculaAluno = input("Digite a matricula do aluno para poder alterar seus dados: ")
        query = "SELECT * FROM aluno WHERE matricula = %s"
        cursor.execute(query, (matriculaAluno))
        record = cursor.fetchone()
        cpf = input("Informe o CPF do Aluno ")
        sql = """UPDATE aluno SET cpf = '{}' WHERE matricula = {};"""
        try:
            cursor.execute(sql.format(cpf, matriculaAluno))
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if connection is not None:
                connection.close()
            if cursor is not None:
                cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
        if cursor is not None:
            cursor.close()
def alterarEmailAlunos():
    postgreSQL_select_Query = "select * from aluno"
    try:
        cursor.execute(postgreSQL_select_Query)
        alunoData = cursor.fetchall()
        for row in alunoData:
            print("Matricula: ", row[0], )
            print("Nome: ", row[1], '\n')
            print("CPF: ", row[2], '\n')
            print("Email: ", row[3], '\n')
            print("Data de Nascimento: ", row[4], '\n')
            linhas()
        matriculaAluno = input("Digite a matricula do aluno para poder alterar seus dados: ")
        query = "SELECT * FROM aluno WHERE matricula = %s"
        cursor.execute(query, (matriculaAluno))
        record = cursor.fetchone()
        email = input("Informe o email do Aluno ")
        sql = """UPDATE aluno SET email = '{}' WHERE matricula = {};"""
        try:
            cursor.execute(sql.format(email, matriculaAluno))
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if connection is not None:
                connection.close()
            if cursor is not None:
                cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
        if cursor is not None:
            cursor.close()
def alterarDataAlunos():
    postgreSQL_select_Query = "select * from aluno"
    try:
        cursor.execute(postgreSQL_select_Query)
        alunoData = cursor.fetchall()
        for row in alunoData:
            print("Matricula: ", row[0], )
            print("Nome: ", row[1], '\n')
            print("CPF: ", row[2], '\n')
            print("Email: ", row[3], '\n')
            print("Data de Nascimento: ", row[4], '\n')
            linhas()
        matriculaAluno = input("Digite a matricula do aluno para poder alterar seus dados: ")
        query = "SELECT * FROM aluno WHERE matricula = %s"
        cursor.execute(query, (matriculaAluno))
        record = cursor.fetchone()
        cpf = input("Informe a data de nascimento do Aluno ")
        sql = """UPDATE aluno SET data_nascimento = '{}' WHERE matricula = {};"""
        try:
            cursor.execute(sql.format(cpf, matriculaAluno))
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if connection is not None:
                connection.close()
            if cursor is not None:
                cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
        if cursor is not None:
            cursor.close()
print('Bem vindo! O que você gostaria de fazer?')

while(True):
    # Menu inicial
    print("1 - Consultar dados")
    print("2 - Alterar dados")
    print("3 - Sair")
    primeiroMenu = int(input('Escolha a opção: '))
    linhas()
    if (primeiroMenu == 3):
        break
    elif (primeiroMenu == 1):
        print("1 - Alunos")
        print("2 - Professores ")
        menuConsulta = int(input('Você gostaria de consultar quais dados? '))
        linhas()
        if (menuConsulta == 1):
            consultarAlunos()
        elif (menuConsulta == 2):
            consultarProfessores()
    elif (primeiroMenu == 2):

        print("1 - Cadastrar aluno ")
        print("2 - Alterar dados de aluno ")
        print("3 - Cadastrar professor ")
        menuAlterar = int(input('Você gostaria de alterar quais dados? '))
        linhas()
        if (menuAlterar == 1):
            cadastrarAlunos()
        elif (menuAlterar == 2):
            try:
                connection = psycopg2.connect(database='SistemaAcademico',
                                              user='postgres',
                                              password='adm',
                                              host='localhost',
                                              port="5432")
                cursor = connection.cursor()
            except (Exception, psycopg2.Error) as error:
                print("Falha na conexao", error)

            print("1 - Nome do aluno ")
            print("2 - CPF do aluno ")
            print("3 - Email do aluno ")
            print("4 - Data de nascimento do aluno ")
            opcaoAlterar = int(input('O que você gostaria de alterar? '))
            if(opcaoAlterar == 1):
                alterarNomeAlunos()
            elif(opcaoAlterar == 2):
                alterarCPFAlunos()
            elif(opcaoAlterar == 3):
                alterarEmailAlunos()
            elif(opcaoAlterar == 4):
                alterarDataAlunos()


#print("4 - Encerrar")