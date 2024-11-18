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
                    print("[5] Visualizar histórico")
                    
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
                            )    
                            # cu.execute(Inserts.newInsertArquivo(*args))
                        case 4:
                            
                            pass
                        case 5:
                            
                            pass
                
                case "empresa":
                    print("\nMenu da Empresa:")
                    print("[1] Visualizar usuários")
                    print("[2] Visualizar arquivos")
                    
                    escolha = int(input("\nEscolha uma opção: "))
                    match escolha:
                        case 1:
                            cu.execute("SELECT * FROM empresaUsuarios")
                            for row in cu: print(row)
                        case 2:
                            cu.execute("SELECT * FROM empresaArquivos")
                            for row in cu: print(row)
                
                case "administrador":
                    print("\nMenu do Administrador:")
                    print("[1] Gerenciar usuários")
                    print("[2] Gerenciar arquivos")
                    print("[3] Visualizar histórico")
                    print("[4] Gerenciar permissões")
                    
                    escolha = int(input("\nEscolha uma opção: "))
                    match escolha:
                        case 1:
                            
                            pass
                        case 2:
                            
                            pass
                        case 3:
                            cu.execute("SELECT * FROM historico")
                            for linha in cu: print(linha)
                        case 4:
                            
                            pass
            
            db.commit()
            opcao = int(input("\nDeseja continuar?\n[0] - Não\n[1] - Sim\n"))