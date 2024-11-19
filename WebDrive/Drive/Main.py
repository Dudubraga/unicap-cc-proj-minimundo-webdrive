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
        cu = db.cursor()

        def bootstrap(cu):
            cu.execute(DataBase.CreateDataBase)
            cu.execute(DataBase.UseDataBase)

            for user in DataBase.createUser():
                cu.execute(f"{user}", multi = True)

            for table in DataBase.createTables():
                cu.execute(f"{table}")

            for dropProcedure in Procedures.dropProcedures():
                cu.execute(f"{dropProcedure}")

            for procedure in Procedures.createProcedures():
                cu.execute(f"{procedure}")

            for view in DataBase.createViews():
                cu.execute(f"{view}")

            for trigger in DataBase.createTriggers():
                cu.execute(f"{trigger}")

            for insert in Inserts.insertDefault():
                cu.execute(f"{insert}")

        db.commit()

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
                            cu.execute(Select.selectUsuarioArquivos())
                            for linha in cu: print(linha)

                        case 2:
                            cu.execute(Select.selectUsuarioHistorico())
                            for linha in cu: print(linha)
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
                            cu.execute(Inserts.newInsertArquivo(*args))
                            db.commit()
                        case 4:
                            cu.execute(Select.selectUsuarioArquivo())
                            for linha in cu: print(linha)
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
                            cu.execute(Update.updateArquivo(*args))
                            db.commit()
                    db.commit()
                
                case "empresa":
                    print("\nMenu da Empresa:")
                    print("[1] Visualizar usuários")
                    print("[2] Visualizar arquivos")
                    
                    escolha = int(input("\nEscolha uma opção: "))
                    match escolha:
                        case 1:
                            cu.execute(Select.selectEmpresaUsuarios())
                            for linha in cu: print(linha)
                        case 2:
                            cu.execute(Select.selectEmpresaArquivos())
                            for linha in cu: print(linha)
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
                                    cu.execute(Select.selectUsuario())
                                    for linha in cu: print(linha)
                                case 2:
                                    args = (
                                        input("Insira login: "),
                                        input("Insira e-mail: "),
                                        input("Insira senha: "),
                                        input("Insira a data: "),
                                        input("Insira o ID da instituição: ")
                                    )    
                                    cu.execute(Inserts.newInsertUsuario(*args))
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
                                    cu.execute(Update.updateUsuario(*args))
                                    db.commit()
                                    pass
                                case 4:
                                    id = input("Informe o ID do usuário que deseja deletar: ")
                                    confirmacao = input("Tem certeza que quer deletar o usuário " + id + "? [S/N]: ")
                                    if(confirmacao == 'S'):
                                        cu.execute(Delete.deleteUsuario())
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
                                    cu.execute(Select.selectArquivo())
                                    for linha in cu: print(linha)
                                case 2:
                                    cu.execute(Select.selectArquivo())
                                    for linha in cu: print(linha)
                                    args = (
                                        input("Insira nome: "),
                                        input("Insira tipo: "),
                                        input("Insira URL: "),
                                        input("Insira permissões de acesso: "),
                                        input("Insira localização: "),
                                        input("Insira tamanho: "),
                                        input("Insira a data: "),
                                    )    
                                    cu.execute(Inserts.newInsertArquivo(*args))
                                    db.commit()
                                case 3:
                                    cu.execute(Select.selectArquivo())
                                    for linha in cu: print(linha)
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
                                    cu.execute(Update.updateArquivo(*args))
                                    db.commit()
                                case 4:
                                    id = input("Informe o ID do arquivo que deseja deletar: ")
                                    confirmacao = input("Tem certeza que quer deletar o arquivo " + id + "? [S/N]: ")
                                    if(confirmacao == 'S'):
                                        cu.execute(Delete.deleteArquivo())
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
                                    cu.execute(Select.selectHistorico())
                                    for linha in cu: print(linha)
                                case 2:
                                    args = (
                                        input("Insira operação: "),
                                        input("Insira a data: "),
                                        input("Insira a hora: "),
                                        input("Insira o conteúdo alterado: "),
                                        input("Insira o ID do usuário: "),
                                        input("Insira o ID do arquivo: "),
                                    ) 
                                    cu.execute(Inserts.newInsertHistorico(*args))
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
                                    cu.execute(Update.updateHistorico(*args))
                                    db.commit()
                                case 4:
                                    id = input("Informe o ID do histórico que deseja deletar: ")
                                    confirmacao = input("Tem certeza que quer deletar o histórico " + id + "? [S/N]: ")
                                    if(confirmacao == 'S'):
                                        cu.execute(Delete.deleteHistorico())
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
                                    cu.execute(Select.selectPlano())
                                    for linha in cu: print(linha)
                                case 2:
                                    args = (
                                        input("Insira nome: "),
                                        input("Insira duração: "),
                                        input("Insira data de aquisição: "),
                                        input("Insira capacidade: ")
                                    )    
                                    cu.execute(Inserts.newInsertPlano(*args))
                                    db.commit()
                                case 3:
                                    id = input("Informe o ID do plano que deseja atualizar: ")
                                    args = (
                
                                        input("Insira novo nome: "),
                                        input("Insira nova duração: "),
                                        input("Insira nova data aquisição"),
                                        input("Insira nova capacidade: ")
                                    )    
                                    cu.execute(Update.updatePlano(*args))
                                    db.commit()
                                case 4:
                                    id = input("Informe o ID do plano que deseja deletar: ")
                                    confirmacao = input("Tem certeza que quer deletar o plano " + id + "? [S/N]: ")
                                    if(confirmacao == 'S'):
                                        cu.execute(Delete.deletePlano())
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
                                    cu.execute(Select.selectInstituicao())
                                    for linha in cu: print(linha)
                                case 2:
                                    args = (
                                        input("Insira nome: "),
                                        input("Insira causa social: "),
                                        input("Insira endereço: "),
                                        input("Insira ID do plano: ")
                                    )    
                                    cu.execute(Inserts.newInsertInstituicao(*args))
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
                                    cu.execute(Update.updateInstituicao(*args))
                                    db.commit()
                                case 4:
                                    id = input("Informe o ID da instituição que deseja deletar: ")
                                    confirmacao = input("Tem certeza que quer deletar a instituição " + id + "? [S/N]: ")
                                    if(confirmacao == 'S'):
                                        cu.execute(Delete.deleteInstituicao(id))
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
                                    cu.execute(Select.selectAdministrador())
                                    for linha in cu: print(linha)
                                case 2:
                                    args = (
                                        input("Insira login: "),
                                        input("Insira e-mail: "),
                                        input("Insira senha: "),
                                        input("Insira a data de ingresso: ")
                                    )    
                                    cu.execute(Inserts.newInsertAdministrador(*args))
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
                                    cu.execute(Update.updateAdministrador(*args))
                                    db.commit()
                                case 4:
                                    id = input("Informe o ID do administrador que deseja deletar: ")
                                    confirmacao = input("Tem certeza que quer deletar o administrador " + id + "? [S/N]: ")
                                    if(confirmacao == 'S'):
                                        cu.execute(Delete.deleteAdministrador())
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
                                    cu.execute(Select.selectSuporta())
                                    for linha in cu: print(linha)
                                case 2:
                                    args = (
                                        input("Insira dia: "),
                                        input("Insira hora: "),
                                        input("Insira descrição: "),
                                        input("Insira ID do usuário: "),
                                        input("Insira ID do arquivo: ")
                                    )    
                                    cu.execute(Inserts.newInsertSuporte(*args))
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
                                    cu.execute(Update.updateSuporte(*args))
                                    db.commit()
                                case 4:
                                    id = input("Informe o ID do suporte que deseja deletar: ")
                                    confirmacao = input("Tem certeza que quer deletar o suporte " + id + "? [S/N]: ")
                                    if(confirmacao == 'S'):
                                        cu.execute(Delete.deleteSuporta())
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
                                    cu.execute(Select.selectOpera())
                                    for linha in cu: print(linha)
                                case 2:
                                    args = (
                                        input("Insira a hora: "),
                                        input("Insira o tipo da operação: "),
                                        input("Insira a data: "),
                                        input("Insira ID do usuário: "),
                                        input("Insira ID do arquivo: ")
                                    )    
                                    cu.execute(Inserts.newInsertOpera(*args))
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
                                    cu.execute(Update.updateOpera(*args))
                                    db.commit()
                                case 4:
                                    id = input("Informe o ID da operação que deseja deletar: ")
                                    confirmacao = input("Tem certeza que quer deletar a operação " + id + "? [S/N]: ")
                                    if(confirmacao == 'S'):
                                        cu.execute(Delete.deleteOpera())
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
                                    cu.execute(Select.selectComentario())
                                    for linha in cu: print(linha)
                                case 2:
                                    args = (
                                        input("Insira o conteúdo: "),
                                        input("Insira a data: "),
                                        input("Insira a hora: "),
                                        input("Insira ID do usuário: "),
                                        input("Insira ID do arquivo: ")
                                    )    
                                    cu.execute(Inserts.newInsertComentario(*args))
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
                                    cu.execute(Update.updateComentario(*args))
                                    db.commit()
                                case 4:
                                    id = input("Informe o ID do usuário que deseja deletar: ")
                                    confirmacao = input("Tem certeza que quer deletar o arquivo " + id + "? [S/N]: ")
                                    if(confirmacao == 'S'):
                                        cu.execute(Delete.deleteComentario())
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
                                    cu.execute(Select.selectCompartilhamento())
                                    for linha in cu: print(linha)
                                case 2:
                                    args = (
                                        input("Insira ID do usuário origem: "),
                                        input("Insira ID do arquivo: "),
                                        input("Insira ID do usuário destino: "),
                                        input("Insira a data do compartilhamento: "),
                                    )    
                                    cu.execute(Inserts.newInsertCompartilhamento(*args))
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
                                    cu.execute(Update.updateCompartilhamento(*args))
                                    db.commit()
                                case 4:
                                    id = input("Informe o ID do compartilhamento que deseja deletar: ")
                                    confirmacao = input("Tem certeza que quer deletar o compartilhame " + id + "? [S/N]: ")
                                    if(confirmacao == 'S'):
                                        cu.execute(Delete.deleteAdministrador())
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
                                    cu.execute(Select.selectAtividades_recentes())
                                    for linha in cu: print(linha)
                                case 2:
                                    args = (
                                        input("Insira ID do arquivo: "),
                                        input("Insira a última versão: "),
                                        input("Insira o tipo de acesso: ")
                                    )    
                                    cu.execute(Inserts.newInsertAtividade(*args))
                                    db.commit()
                                case 3:
                                    id = input("Informe o ID do arquivo que deseja atualizar: ")
                                    args = (
                                        input("Insira a nova última versão: "),
                                        input("Insira o novo tipo de acesso: "),
                                        input("Insira o novo ID do arquivo: ")
                                    )    
                                    cu.execute(Update.updateAtividade(*args))
                                    db.commit()
                                case 4:
                                    id = input("Informe o ID da atividade que deseja deletar: ")
                                    confirmacao = input("Tem certeza que quer deletar a atividade " + id + "? [S/N]: ")
                                    if(confirmacao == 'S'):
                                        cu.execute(Delete.deleteAtividadesRecentes())
                                        db.commit()
                                    else:
                                        print("Operação cancelada! ")
                    db.commit()
                    opcao = int(input("\nDeseja continuar?\n[0] Não\n[1] Sim\n"))