import mysql.connector
from CRUD.DataBase import DataBase

class Main:
    print("Usuários disponíveis:\nadministrador | usuario | empresa")
    user = input("Digite seu usuário: ")
    passwd = input("Digite sua senha: ")
        
    
    try:
        db = mysql.connector.connect(
            host="localhost",
            user= user,
            passwd= passwd,
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

            # for dropProcedure in ConstructProcedures.dropProcedures():
                # cu.execute(f"{dropProcedure}")

            # for procedure in ConstructProcedures.createProcedures():
                # cu.execute(f"{procedure}")

            for view in DataBase.createViews():
                cu.execute(f"{view}")

            for trigger in DataBase.createTriggers():
                cu.execute(f"{trigger}")

            # for insert in Inserts.insertDefault():
                # cu.execute(f"{insert}")

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
                            cu.execute("SELECT * FROM usuarioArquivo")
                            for linha in cu: print(linha)

                        case 2:
                            cu.execute("SELECT * FROM usuarioHistorico")
                            for linha in cu: print(linha)
                        case 3:
                            args = (
                                input("Insira nome: "),
                                input("Insira tipo: "),
                                input("Insira URL: "),
                                input("Insira permissões de acesso: "),
                                input("Insira localização: "),
                                input("Insira tamanho: "),
                                # data modificacao
                            )    
                            # cu.execute(Inserts.newInsertArquivo(*args))
                        case 4:
                            args = (
                                input("Insira o novo nome: "),
                                input("Insira o novo tipo: "),
                                input("Insira p novo URL: "),
                                input("Insira as novas permissões de acesso: "),
                                input("Insira a nova localização: "),
                                input("Insira o novo tamanho: "),
                                # data modificacao
                            ) 
                            # cu.execute(Updates.updateArquivo(*args))
                
                case "empresa":
                    print("\nMenu da Empresa:")
                    print("[1] Visualizar usuários")
                    print("[2] Visualizar arquivos")
                    
                    escolha = int(input("\nEscolha uma opção: "))
                    match escolha:
                        case 1:
                            cu.execute("SELECT * FROM empresaUsuarios")
                            for linha in cu: print(linha)
                        case 2:
                            cu.execute("SELECT * FROM empresaArquivos")
                            for linha in cu: print(linha)
                
                case "administrador":
                    print("\nMenu do Administrador:")
                    print("[1] Gerenciar usuários")
                    print("[2] Gerenciar arquivos")
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
                            ans = int(input())

                            match ans:
                                case 1: 
                                    cu.execute("SELECT * FROM usuario")
                                    for linha in cu: print(linha)
                                case 2:
                                    args = (
                                        input("Insira login: "),
                                        input("Insira e-mail: "),
                                        input("Insira senha: "),
                                        # data ingresso
                                        input("Insira o ID da instituição: ")
                                    )    
                                    # cu.execute(Inserts.newInsertUsuario(*args))
                                case 3:
                                    id = input("Informe o ID do usuário que deseja atualizar: ")
                                    #verifica se usuário existe e pede infos
                                    args = (
                                        id,
                                        input("Insira o novo login: "),
                                        input("Insira o novo e-mail: "),
                                        input("Insira a nova senha: "),
                                        # data ingresso
                                        input("Insira o novo ID da instituição: ")
                                    )    
                                    # cu.execute(Update.updateUsuario(*args))
                                    pass
                                case 4:
                                    id = input("Informe o ID do usuário que deseja deletar: ")
                                    # conferir existencia do usuário
                                    cu.execute("DELETE usuario WHERE id = usuario.id")

                        #ARQUIVO
                        case 2:
                            print("[1] Visualizar arquivos")
                            print("[2] Inserir novo arquivo")
                            print("[3] Atualizar arquivo")
                            print("[4] Deletar arquivo")
                            ans = int(input())

                            match ans:
                                case 1:
                                    cu.execute("SELECT * FROM arquivo")
                                    for linha in cu: print(linha)
                                case 2:
                                    args = (
                                        input("Insira nome: "),
                                        input("Insira tipo: "),
                                        input("Insira URL: "),
                                        input("Insira permissões de acesso: "),
                                        input("Insira localização: "),
                                        input("Insira tamanho: "),
                                        # data modificacao
                                    ) 
                                    # cu.execute(Inserts.newInsertArquivo(*args))
                                case 3:
                                    id = input("Informe o ID do arquivo que deseja atualizar: ")
                                    #verifica se arquivo existe e pede infos
                                    args = (
                                        input("Insira o novo nome: "),
                                        input("Insira o novo tipo: "),
                                        input("Insira o novo URL: "),
                                        input("Insira as novas permissões de acesso: "),
                                        input("Insira a nova localização: "),
                                        input("Insira o novo tamanho: "),
                                        # data modificacao
                                    ) 
                                    # cu.execute(Updates.updateArquivo(*args))
                                case 4:
                                    id = input("Informe o ID do arquivo que deseja deletar: ")
                                    # conferir existencia do arquivo
                                    # cu.execute("DELETE arquivo WHERE id = arquivo.id")
                        
                        #HISTÓRICO
                        case 3:
                            print("[1] Visualizar histórico")
                            print("[2] Inserir novo histórico")
                            print("[3] Atualizar histórico")
                            print("[4] Deletar histórico")
                            ans = int(input())

                            match ans:
                                case 1:
                                    cu.execute("SELECT * FROM historico")
                                    for linha in cu: print(linha)
                                case 2:
                                    args = (
                                        input("Insira operação: "),
                                        # data
                                        # hora
                                        input("Insira o conteúdo alterado: "),
                                        input("Insira o ID do usuário: "),
                                        input("Insira o ID do arquivo: "),
                                    ) 
                                    # cu.execute(Inserts.newInsertHistorico(*args))
                                case 3:
                                    id = input("Informe o ID do histórico que deseja atualizar: ")
                                    #verifica se histórico existe e pede infos
                                    args = (
                                        input("Insira a nova operação: "),
                                        input("Insira o novo conteúdo alterado: "),
                                        input("Insira o novo ID do usuário: "),
                                        input("Insira o novo ID do arquivo: "),
                                    ) 
                                    # cu.execute(Updates.updateHistorico(*args))
                                case 4:
                                    id = input("Informe o ID do histórico que deseja deletar: ")
                                    # conferir existencia do histórico
                                    # cu.execute("DELETE historico WHERE id = historico.id")

                        #PLANO         
                        case 4:
                            
                            pass
                        
                        #INSTITUIÇÃO
                        case 5:
                            pass
                        
                        #ADMINISTRADOR
                        case 6:
                            pass
                        
                        #SUPORTE
                        case 7:
                            pass

                        #OPERAÇÕES
                        case 8: 
                            pass

                        #COMENTÁRIOS
                        case 9:
                            pass

                        #COMPARTILHAMENTO
                        case 10:
                            pass

                        #ATIVIDADE RECENTE
                        case 11:
                            pass
                        
                            
            
            db.commit()
            opcao = int(input("\nDeseja continuar?\n[0] Não\n[1] Sim\n"))