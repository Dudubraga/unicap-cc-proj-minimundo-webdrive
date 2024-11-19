import mysql.connector
from CRUD.DataBase import DataBase
from Select.Select import Select
from Inserts.Inserts import Inserts
from CRUD.Procedures import Procedures
from CRUD.Update import Update
from CRUD.Delete import Delete

class Main:
    print("Usuários disponíveis:\nadministrador | usuario | empresa")
    user = input("Digite seu usuário: ")
    passwd = input("Digite sua senha: ")

    try:
        db = mysql.connector.connect(
            host="localhost",
            user= 'root',
            database="drive"
        )
    except Exception as e:
        print(f"Erro na conexão: {e}")
    
    else:
        cursor = db.cursor()

        def bootstrap(cursor):
            cursor.execute(DataBase.CreateDataBase)
            cursor.execute(DataBase.UseDataBase)

            for user in DataBase.createUser():
                cursor.execute(f"{user}", multi = True)

            for table in DataBase.createTables():
                cursor.execute(f"{table}")

            for dropProcedure in Procedures.dropProcedures():
                cursor.execute(f"{dropProcedure}")

            for procedure in Procedures.createProcedures():
                cursor.execute(f"{procedure}")

            for view in DataBase.createViews():
                cursor.execute(f"{view}")

            for trigger in DataBase.createTriggers():
                cursor.execute(f"{trigger}")

            for insert in Inserts.insertDefault():
                cursor.execute(f"{insert}")

        db.commit()

        def validate(cursor, login, senha):
            if login == 'usuario':
                cursor.execute(f"SELECT id, senha FROM usuario WHERE login = '{login}'")
            elif login == 'administrador':
                cursor.execute(f"SELECT id, senha FROM administrador WHERE login = '{login}'")
            elif login == 'empresa':
                cursor.execute(f"SELECT id, senha FROM instituicao WHERE login = '{login}'")
            info = cursor.fetchone()
            if info is not None and info[1] == senha:
                return True
            else:
                cursor.close()
                return False

        if not validate(cursor, user, passwd):
            print(f"Senha ou usuario invalidos")
        else:
            opcao = 1
            while(opcao == 1):
                match user:
                    case "usuario":
                        print("\nMenu do Usuário:")
                        print("[1] Visualizar meus arquivos")
                        print("[2] Visualizar meu histórico")
                        print("[3] Inserir novo arquivo")
                        print("[4] Atualizar arquivo")

                        escolha = int(input("\nEscolha uma opção: "))
                        match escolha:
                            case 1:
                                cursor.execute(Select.selectUsuarioArquivos())
                                for linha in cursor: print(linha)

                            case 2:
                                cursor.execute(Select.selectUsuarioHistorico())
                                for linha in cursor: print(linha)
                            case 3:
                                args = (
                                    input("Insira nome: "),
                                    input("Insira tipo: "),
                                    input("Insira URL: "),
                                    input("Insira permissões de acesso: "),
                                    input("Insira localização: "),
                                    input("Insira tamanho: "),
                                    input("Insira a data: "),
                                )    
                                cursor.execute(Inserts.newInsertArquivo(*args))
                                db.commit()
                            case 4:
                                cursor.execute(Select.selectUsuarioArquivo())
                                for linha in cursor: print(linha)
                                args = (
                                    input("Insira o novo nome: "),
                                    input("Insira o novo tipo: "),
                                    input("Insira p novo URL: "),
                                    input("Insira as novas permissões de acesso: "),
                                    input("Insira a nova localização: "),
                                    input("Insira o novo tamanho: "),
                                    input("Insira a data: "),
                                    input("Insira o id do arquivo: ")
                                ) 
                                cursor.execute(Update.updateArquivo(*args))
                                db.commit()
                        db.commit()
                        opcao = int(input("\nDeseja continuar?\n[0] Não\n[1] Sim\n"))

                    case "empresa":
                        print("\nMenu da Empresa:")
                        print("[1] Visualizar usuários")
                        print("[2] Visualizar arquivos")

                        escolha = int(input("\nEscolha uma opção: "))
                        match escolha:
                            case 1:
                                cursor.execute(Select.selectEmpresaUsuarios())
                                for linha in cursor: print(linha)
                            case 2:
                                cursor.execute(Select.selectEmpresaArquivos())
                                for linha in cursor: print(linha)
                        db.commit()
                        opcao = int(input("\nDeseja continuar?\n[0] Não\n[1] Sim\n"))

                    case "administrador":
                        print("\nMenu do Administrador:")
                        print("[1] Gerenciar usuários") #feito
                        print("[2] Gerenciar arquivos")#feito
                        print("[3] Gerenciar histórico")
                        print("[4] Gerenciar plano")
                        print("[5] Gerenciar instituição")
                        print("[6] Gerenciar administrador")
                        print("[7] Gerenciar suportes")
                        print("[8] Gerenciar alterações")
                        print("[9] Gerenciar comentários")
                        print("[10] Gerenciar compartilhamentos")
                        print("[11] Gerenciar atividades recentes")

                        escolha = int(input("\nEscolha uma opção: "))
                        match escolha:
                            #USUARIO
                            case 1:
                                print("[1] Visualizar usuários")
                                print("[2] Inserir novo usuário")
                                print("[3] Atualizar usuário")
                                print("[4] Deletar usuário")
                                ans = int(input("\nEscolha uma opção: "))

                                match ans:
                                    case 1: 
                                        cursor.execute(Select.selectUsuario())
                                        for linha in cursor: print(linha)
                                    case 2:
                                        args = (
                                            input("Insira login: "),
                                            input("Insira e-mail: "),
                                            input("Insira senha: "),
                                            input("Insira a data: "),
                                            input("Insira o ID da instituição: ")
                                        )    
                                        cursor.execute(Inserts.newInsertUsuario(*args))
                                        db.commit()
                                    case 3:
                                        id = input("Informe o ID do usuário que deseja atualizar: ")
                                        args = (
                                            input("Insira o novo login: "),
                                            input("Insira o novo e-mail: "),
                                            input("Insira a nova senha: "),
                                            input("Insira a data: "),
                                            input("Insira o novo ID da instituição: "),
                                            id
                                        )    
                                        cursor.execute(Update.updateUsuario(*args))
                                        db.commit()
                                        pass
                                    case 4:
                                        id = input("Informe o ID do usuário que deseja deletar: ")
                                        confirmacao = input("Tem certeza que quer deletar o usuário " + id + "? [S/N]: ")
                                        if(confirmacao == 'S'):
                                            cursor.execute(Delete.deleteUsuario())
                                            db.commit()
                                        else:
                                            print("Operação cancelada! ")

                            #ARQUIVO
                            case 2:
                                print("[1] Visualizar arquivos")
                                print("[2] Inserir novo arquivo")
                                print("[3] Atualizar arquivo")
                                print("[4] Deletar arquivo")
                                ans = int(input("\nEscolha uma opção: "))

                                match ans:
                                    case 1:
                                        cursor.execute(Select.selectArquivo())
                                        for linha in cursor: print(linha)
                                    case 2:
                                        cursor.execute(Select.selectArquivo())
                                        for linha in cursor: print(linha)
                                        args = (
                                            input("Insira nome: "),
                                            input("Insira tipo: "),
                                            input("Insira URL: "),
                                            input("Insira permissões de acesso: "),
                                            input("Insira localização: "),
                                            input("Insira tamanho: "),
                                            input("Insira a data: "),
                                        )    
                                        cursor.execute(Inserts.newInsertArquivo(*args))
                                        db.commit()
                                    case 3:
                                        cursor.execute(Select.selectArquivo())
                                        for linha in cursor: print(linha)
                                        args = (
                                            input("Insira o novo nome: "),
                                            input("Insira o novo tipo: "),
                                            input("Insira p novo URL: "),
                                            input("Insira as novas permissões de acesso: "),
                                            input("Insira a nova localização: "),
                                            input("Insira o novo tamanho: "),
                                            input("Insira a data: "),
                                            input("Insira o id do arquivo: ")
                                        ) 
                                        cursor.execute(Update.updateArquivo(*args))
                                        db.commit()
                                    case 4:
                                        id = input("Informe o ID do arquivo que deseja deletar: ")
                                        confirmacao = input("Tem certeza que quer deletar o arquivo " + id + "? [S/N]: ")
                                        if(confirmacao == 'S'):
                                            cursor.execute(Delete.deleteArquivo())
                                            db.commit()
                                        else:
                                            print("Operação cancelada! ")

                            #HISTÓRICO
                            case 3:
                                print("[1] Visualizar histórico")
                                print("[2] Inserir novo histórico")
                                print("[3] Atualizar histórico")
                                print("[4] Deletar histórico")
                                ans = int(input("\nEscolha uma opção: "))

                                match ans:
                                    case 1:
                                        cursor.execute(Select.selectHistorico())
                                        for linha in cursor: print(linha)
                                    case 2:
                                        args = (
                                            input("Insira operação: "),
                                            input("Insira a data: "),
                                            input("Insira a hora: "),
                                            input("Insira o conteúdo alterado: "),
                                            input("Insira o ID do usuário: "),
                                            input("Insira o ID do arquivo: "),
                                        ) 
                                        cursor.execute(Inserts.newInsertHistorico(*args))
                                        db.commit()
                                    case 3:
                                        id = input("Informe o ID do histórico que deseja atualizar: ")
                                        args = (
                                            input("Insira a nova operação: "),
                                            input("Insira a nova data: "),
                                            input("Insira a nova hora: "),
                                            input("Insira o novo conteúdo alterado: "),
                                            input("Insira o novo ID do usuário: "),
                                            input("Insira o novo ID do arquivo: "),
                                            id
                                        ) 
                                        cursor.execute(Update.updateHistorico(*args))
                                        db.commit()
                                    case 4:
                                        id = input("Informe o ID do histórico que deseja deletar: ")
                                        confirmacao = input("Tem certeza que quer deletar o histórico " + id + "? [S/N]: ")
                                        if(confirmacao == 'S'):
                                            cursor.execute(Delete.deleteHistorico())
                                            db.commit()
                                        else:
                                            print("Operação cancelada! ")

                            #PLANO         
                            case 4:
                                print("[1] Visualizar planos")
                                print("[2] Inserir novo plano")
                                print("[3] Atualizar plano")
                                print("[4] Deletar plano")
                                ans = int(input("\nEscolha uma opção: "))

                                match ans:
                                    case 1:
                                        cursor.execute(Select.selectPlano())
                                        for linha in cursor: print(linha)
                                    case 2:
                                        args = (
                                            input("Insira nome: "),
                                            input("Insira duração: "),
                                            input("Insira data de aquisição: "),
                                            input("Insira capacidade: ")
                                        )    
                                        cursor.execute(Inserts.newInsertPlano(*args))
                                        db.commit()
                                    case 3:
                                        id = input("Informe o ID do plano que deseja atualizar: ")
                                        args = (
                                        
                                            input("Insira novo nome: "),
                                            input("Insira nova duração: "),
                                            input("Insira nova data aquisição"),
                                            input("Insira nova capacidade: ")
                                        )    
                                        cursor.execute(Update.updatePlano(*args))
                                        db.commit()
                                    case 4:
                                        id = input("Informe o ID do plano que deseja deletar: ")
                                        confirmacao = input("Tem certeza que quer deletar o plano " + id + "? [S/N]: ")
                                        if(confirmacao == 'S'):
                                            cursor.execute(Delete.deletePlano())
                                            db.commit()
                                        else:
                                            print("Operação cancelada! ")

                            #INSTITUIÇÃO
                            case 5:
                                print("[1] Visualizar instituições")
                                print("[2] Inserir nova instituição")
                                print("[3] Atualizar instituição")
                                print("[4] Deletar instituição")
                                ans = int(input("\nEscolha uma opção: "))

                                match ans:
                                    case 1:
                                        cursor.execute(Select.selectInstituicao())
                                        for linha in cursor: print(linha)
                                    case 2:
                                        args = (
                                            input("Insira nome: "),
                                            input("Insira causa social: "),
                                            input("Insira endereço: "),
                                            input("Insira ID do plano: ")
                                        )    
                                        cursor.execute(Inserts.newInsertInstituicao(*args))
                                        db.commit()
                                    case 3:
                                        id = input("Informe o ID da instituição que deseja atualizar: ")
                                        args = (
                                            input("Insira novo nome: "),
                                            input("Insira nova causa social: "),
                                            input("Insira novo endereço: "),
                                            input("Insira novo ID do plano: "),
                                            id
                                        )    
                                        cursor.execute(Update.updateInstituicao(*args))
                                        db.commit()
                                    case 4:
                                        id = input("Informe o ID da instituição que deseja deletar: ")
                                        confirmacao = input("Tem certeza que quer deletar a instituição " + id + "? [S/N]: ")
                                        if(confirmacao == 'S'):
                                            cursor.execute(Delete.deleteInstituicao(id))
                                            db.commit()
                                        else:
                                            print("Operação cancelada! ")

                            #ADMINISTRADOR
                            case 6:
                                print("[1] Visualizar administradores")
                                print("[2] Inserir novo administrador")
                                print("[3] Atualizar administrador")
                                print("[4] Deletar administrador")
                                ans = int(input())

                                match ans:
                                    case 1:
                                        cursor.execute(Select.selectAdministrador())
                                        for linha in cursor: print(linha)
                                    case 2:
                                        args = (
                                            input("Insira login: "),
                                            input("Insira e-mail: "),
                                            input("Insira senha: "),
                                            input("Insira a data de ingresso: ")
                                        )    
                                        cursor.execute(Inserts.newInsertAdministrador(*args))
                                        db.commit()
                                    case 3:
                                        id = input("Informe o ID do administrador que deseja atualizar: ")
                                        args = (
                                            input("Insira novo login: "),
                                            input("Insira novo e-mail: "),
                                            input("Insira nova senha: "),
                                            input("Insira a nova data de ingresso: "),
                                            id
                                        )    
                                        cursor.execute(Update.updateAdministrador(*args))
                                        db.commit()
                                    case 4:
                                        id = input("Informe o ID do administrador que deseja deletar: ")
                                        confirmacao = input("Tem certeza que quer deletar o administrador " + id + "? [S/N]: ")
                                        if(confirmacao == 'S'):
                                            cursor.execute(Delete.deleteAdministrador())
                                            db.commit()
                                        else:
                                            print("Operação cancelada! ")

                            #SUPORTE
                            case 7:
                                print("[1] Visualizar suportes")
                                print("[2] Inserir novo suporte")
                                print("[3] Atualizar suporte")
                                print("[4] Deletar suporte")
                                ans = int(input())

                                match ans:
                                    case 1:
                                        cursor.execute(Select.selectSuporta())
                                        for linha in cursor: print(linha)
                                    case 2:
                                        args = (
                                            input("Insira dia: "),
                                            input("Insira hora: "),
                                            input("Insira descrição: "),
                                            input("Insira ID do usuário: "),
                                            input("Insira ID do arquivo: ")
                                        )    
                                        cursor.execute(Inserts.newInsertSuporte(*args))
                                        db.commit()
                                    case 3:
                                        id = input("Informe o ID do suporte que deseja atualizar: ")
                                        args = (
                                            id,
                                            input("Insira novo título: "),
                                            input("Insira nova descrição: "),
                                            input("Insira novo status: "),
                                            input("Insira nova prioridade: "),
                                            input("Insira novo ID do usuário: ")
                                        )    
                                        cursor.execute(Update.updateSuporte(*args))
                                        db.commit()
                                    case 4:
                                        id = input("Informe o ID do suporte que deseja deletar: ")
                                        confirmacao = input("Tem certeza que quer deletar o suporte " + id + "? [S/N]: ")
                                        if(confirmacao == 'S'):
                                            cursor.execute(Delete.deleteSuporta())
                                            db.commit()
                                        else:
                                            print("Operação cancelada! ")

                            #OPERA
                            case 8:
                                print("[1] Visualizar alterações")
                                print("[2] Inserir nova alteração")
                                print("[3] Atualizar alteração")
                                print("[4] Deletar alteração")
                                ans = int(input())

                                match ans:
                                    case 1:
                                        cursor.execute(Select.selectOpera())
                                        for linha in cursor: print(linha)
                                    case 2:
                                        args = (
                                            input("Insira a hora: "),
                                            input("Insira o tipo da operação: "),
                                            input("Insira a data: "),
                                            input("Insira ID do usuário: "),
                                            input("Insira ID do arquivo: ")
                                        )    
                                        cursor.execute(Inserts.newInsertOpera(*args))
                                        db.commit()
                                    case 3:
                                        id = input("Informe o ID da alteração que deseja atualizar: ")
                                        args = (
                                            input("Insira a nova hora: "),
                                            input("Insira o novo tipo da operação: "),
                                            input("Insira a nova data: "),
                                            input("Insira o novo ID do usuário: "),
                                            input("Insira o novo ID do arquivo: "),
                                            id
                                        )    
                                        cursor.execute(Update.updateOpera(*args))
                                        db.commit()
                                    case 4:
                                        id = input("Informe o ID da operação que deseja deletar: ")
                                        confirmacao = input("Tem certeza que quer deletar a operação " + id + "? [S/N]: ")
                                        if(confirmacao == 'S'):
                                            cursor.execute(Delete.deleteOpera())
                                            db.commit()
                                        else:
                                            print("Operação cancelada! ")

                            #COMENTÁRIOS
                            case 9:
                                print("[1] Visualizar comentários")
                                print("[2] Inserir novo comentário")
                                print("[3] Atualizar comentário")
                                print("[4] Deletar comentário")
                                ans = int(input())

                                match ans:
                                    case 1:
                                        cursor.execute(Select.selectComentario())
                                        for linha in cursor: print(linha)
                                    case 2:
                                        args = (
                                            input("Insira o conteúdo: "),
                                            input("Insira a data: "),
                                            input("Insira a hora: "),
                                            input("Insira ID do usuário: "),
                                            input("Insira ID do arquivo: ")
                                        )    
                                        cursor.execute(Inserts.newInsertComentario(*args))
                                        db.commit()
                                    case 3:
                                        id = input("Informe o ID do comentário que deseja atualizar: ")
                                        args = (
                                            input("Insira novo conteúdo: "),
                                            input("Insira a nova data: "),
                                            input("Insira a nova hora: "),
                                            input("Insira novo ID do usuário: "),
                                            input("Insira novo ID do arquivo: "),
                                            id
                                        )    
                                        cursor.execute(Update.updateComentario(*args))
                                        db.commit()
                                    case 4:
                                        id = input("Informe o ID do usuário que deseja deletar: ")
                                        confirmacao = input("Tem certeza que quer deletar o arquivo " + id + "? [S/N]: ")
                                        if(confirmacao == 'S'):
                                            cursor.execute(Delete.deleteComentario())
                                            db.commit()
                                        else:
                                            print("Operação cancelada! ")

                            #COMPARTILHAMENTO
                            case 10:
                                print("[1] Visualizar compartilhamentos")
                                print("[2] Inserir novo compartilhamento")
                                print("[3] Atualizar compartilhamento")
                                print("[4] Deletar compartilhamento")
                                ans = int(input())

                                match ans:
                                    case 1:
                                        cursor.execute(Select.selectCompartilhamento())
                                        for linha in cursor: print(linha)
                                    case 2:
                                        args = (
                                            input("Insira ID do usuário origem: "),
                                            input("Insira ID do arquivo: "),
                                            input("Insira ID do usuário destino: "),
                                            input("Insira a data do compartilhamento: "),
                                        )    
                                        cursor.execute(Inserts.newInsertCompartilhamento(*args))
                                        db.commit()
                                    case 3:
                                        id = input("Informe o ID do compartilhamento que deseja atualizar: ")
                                        args = (
                                            input("Insira novo tipo de permissão: "),
                                            input("Insira a nova data do compartilhamento: "),
                                            input("Insira novo ID do usuário origem: "),
                                            input("Insira novo ID do usuário destino: "),
                                            input("Insira novo ID do arquivo: "),
                                            id
                                        )    
                                        cursor.execute(Update.updateCompartilhamento(*args))
                                        db.commit()
                                    case 4:
                                        id = input("Informe o ID do compartilhamento que deseja deletar: ")
                                        confirmacao = input("Tem certeza que quer deletar o compartilhame " + id + "? [S/N]: ")
                                        if(confirmacao == 'S'):
                                            cursor.execute(Delete.deleteAdministrador())
                                            db.commit()
                                        else:
                                            print("Operação cancelada! ")

                            #ATIVIDADE RECENTE
                            case 11:
                                print("[1] Visualizar atividades recentes")
                                print("[2] Inserir nova atividade")
                                print("[3] Atualizar atividade")
                                print("[4] Deletar atividade")
                                ans = int(input())

                                match ans:
                                    case 1:
                                        cursor.execute(Select.selectAtividades_recentes())
                                        for linha in cursor: print(linha)
                                    case 2:
                                        args = (
                                            input("Insira ID do arquivo: "),
                                            input("Insira a última versão: "),
                                            input("Insira o tipo de acesso: ")
                                        )    
                                        cursor.execute(Inserts.newInsertAtividade(*args))
                                        db.commit()
                                    case 3:
                                        id = input("Informe o ID do arquivo que deseja atualizar: ")
                                        args = (
                                            input("Insira a nova última versão: "),
                                            input("Insira o novo tipo de acesso: "),
                                            input("Insira o novo ID do arquivo: ")
                                        )    
                                        cursor.execute(Update.updateAtividade(*args))
                                        db.commit()
                                    case 4:
                                        id = input("Informe o ID da atividade que deseja deletar: ")
                                        confirmacao = input("Tem certeza que quer deletar a atividade " + id + "? [S/N]: ")
                                        if(confirmacao == 'S'):
                                            cursor.execute(Delete.deleteAtividadesRecentes())
                                            db.commit()
                                        else:
                                            print("Operação cancelada! ")
                        db.commit()
                        opcao = int(input("\nDeseja continuar?\n[0] Não\n[1] Sim\n"))
                cursor.close()
