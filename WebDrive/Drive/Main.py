import mysql.connector
from CRUD.DataBase import DataBase
from Select.Select import Select
from Inserts.Inserts import Inserts
from CRUD.Procedures import Procedures
from Update.Update import Update

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
                            id = input("Informe o ID do arquivo que deseja atualizar: ")

                            cu.execute(Select.selectUsuarioArquivos())
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
                
                case "empresa":
                    print("\nMenu da Empresa:")
                    print("[1] Visualizar usuários")
                    print("[2] Visualizar arquivos")
                    
                    escolha = int(input("\nEscolha uma opção: "))
                    match escolha:
                        case 1:
                            cu.execute(Select.selectEmpresaUsuarios())
                            # cu.execute("SELECT * FROM empresaUsuarios")
                            for linha in cu: print(linha)
                        case 2:
                            cu.execute(Select.selectEmpresaArquivos())
                            # cu.execute("SELECT * FROM empresaArquivos")
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
                                    cu.execute(Select.selectUsuario())
                                    # cu.execute("SELECT * FROM usuario")
                                    for linha in cu: print(linha)
                                case 2:
                                    args = (
                                        input("Insira login: "),
                                        input("Insira e-mail: "),
                                        input("Insira senha: "),
                                        # data ingresso
                                        input("Insira o ID da instituição: ")
                                    )    
                                    cu.execute(Inserts.newInsertUsuario(*args))
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
                                    cu.execute(Select.selectArquivo())
                                    # cu.execute("SELECT * FROM arquivo")
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
                                    cu.execute(Inserts.newInsertArquivo(*args))
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
                                    # cu.execute(Updates.updateArquivo(*args) WHERE id = arquivo.id)
                                case 4:
                                    id = input("Informe o ID do arquivo que deseja deletar: ")
                                    # conferir existencia do arquivo
                                    cu.execute("DELETE arquivo WHERE id = arquivo.id")
                        
                        #HISTÓRICO
                        case 3:
                            print("[1] Visualizar histórico")
                            print("[2] Inserir novo histórico")
                            print("[3] Atualizar histórico")
                            print("[4] Deletar histórico")
                            ans = int(input())

                            match ans:
                                case 1:
                                    cu.execute(Select.selectHistorico())
                                    # cu.execute("SELECT * FROM historico")
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
                                    cu.execute(Inserts.newInsertHistorico(*args))
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
                                    # cu.execute("DELETE historico WHERE id = historico.id").

                        #PLANO         
                        case 4:
                            print("[1] Visualizar planos")
                            print("[2] Inserir novo plano")
                            print("[3] Atualizar plano")
                            print("[4] Deletar plano")
                            ans = int(input())

                            match ans:
                                case 1:
                                    cu.execute(Select.selectPlano())
                                    # cu.execute("SELECT * FROM plano")
                                    for linha in cu: print(linha)
                                case 2:
                                    args = (
                                        input("Insira nome: "),
                                        input("Insira descrição: "),
                                        input("Insira preço: "),
                                        input("Insira capacidade: ")
                                    )    
                                    cu.execute(Inserts.newInsertPlano(*args))
                                case 3:
                                    id = input("Informe o ID do plano que deseja atualizar: ")
                                    args = (
                                        id,
                                        input("Insira novo nome: "),
                                        input("Insira nova descrição: "),
                                        input("Insira novo preço: "),
                                        input("Insira nova capacidade: ")
                                    )    
                                    # cu.execute(Updates.updatePlano(*args))
                                case 4:
                                    id = input("Informe o ID do plano que deseja deletar: ")
                                    # cu.execute("DELETE plano WHERE id = plano.id")

                        #INSTITUIÇÃO
                        case 5:
                            print("[1] Visualizar instituições")
                            print("[2] Inserir nova instituição")
                            print("[3] Atualizar instituição")
                            print("[4] Deletar instituição")
                            ans = int(input())

                            match ans:
                                case 1:
                                    cu.execute(Select.selectInstituicao())
                                    # cu.execute("SELECT * FROM instituicao")
                                    for linha in cu: print(linha)
                                case 2:
                                    args = (
                                        input("Insira nome: "),
                                        input("Insira CNPJ: "),
                                        input("Insira endereço: "),
                                        input("Insira telefone: "),
                                        input("Insira ID do plano: ")
                                    )    
                                    cu.execute(Inserts.newInsertInstituicao(*args))
                                case 3:
                                    id = input("Informe o ID da instituição que deseja atualizar: ")
                                    args = (
                                        id,
                                        input("Insira novo nome: "),
                                        input("Insira novo CNPJ: "),
                                        input("Insira novo endereço: "),
                                        input("Insira novo telefone: "),
                                        input("Insira novo ID do plano: ")
                                    )    
                                    # cu.execute(Updates.updateInstituicao(*args))
                                case 4:
                                    id = input("Informe o ID da instituição que deseja deletar: ")
                                    # cu.execute("DELETE instituicao WHERE id = instituicao.id")

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
                                    # cu.execute("SELECT * FROM administrador")
                                    for linha in cu: print(linha)
                                case 2:
                                    args = (
                                        input("Insira login: "),
                                        input("Insira senha: "),
                                        input("Insira nível de acesso: "),
                                        input("Insira ID da instituição: ")
                                    )    
                                    cu.execute(Inserts.newInsertAdministrador(*args))
                                case 3:
                                    id = input("Informe o ID do administrador que deseja atualizar: ")
                                    args = (
                                        id,
                                        input("Insira novo login: "),
                                        input("Insira nova senha: "),
                                        input("Insira novo nível de acesso: "),
                                        input("Insira novo ID da instituição: ")
                                    )    
                                    # cu.execute(Updates.updateAdministrador(*args))
                                case 4:
                                    id = input("Informe o ID do administrador que deseja deletar: ")
                                    # cu.execute("DELETE administrador WHERE id = administrador.id")

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
                                    cu.execute("SELECT * FROM suporte")
                                    for linha in cu: print(linha)
                                case 2:
                                    args = (
                                        input("Insira título: "),
                                        input("Insira descrição: "),
                                        input("Insira status: "),
                                        input("Insira prioridade: "),
                                        input("Insira ID do usuário: ")
                                    )    
                                    # cu.execute(Inserts.newInsertSuporte(*args))
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
                                    # cu.execute(Updates.updateSuporte(*args))
                                case 4:
                                    id = input("Informe o ID do suporte que deseja deletar: ")
                                    # cu.execute("DELETE suporte WHERE id = suporte.id")

                        #ALTERAÇÕES
                        case 8:
                            print("[1] Visualizar alterações")
                            print("[2] Inserir nova alteração")
                            print("[3] Atualizar alteração")
                            print("[4] Deletar alteração")
                            ans = int(input())

                            match ans:
                                case 1:
                                    cu.execute(Select.selectOpera())
                                    # cu.execute("SELECT * FROM opera")
                                    for linha in cu: print(linha)
                                case 2:
                                    args = (
                                        input("Insira tipo: "),
                                        input("Insira descrição: "),
                                        # data_alteracao
                                        input("Insira ID do arquivo: ")
                                    )    
                                    cu.execute(Inserts.newInsertOpera(*args))
                                case 3:
                                    id = input("Informe o ID da alteração que deseja atualizar: ")
                                    args = (
                                        id,
                                        input("Insira novo tipo: "),
                                        input("Insira nova descrição: "),
                                        input("Insira novo ID do arquivo: ")
                                    )    
                                    # cu.execute(Updates.updateOpera(*args))
                                case 4:
                                    id = input("Informe o ID da alteração que deseja deletar: ")
                                    # cu.execute("DELETE opera WHERE id = opera.id")

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
                                    # cu.execute("SELECT * FROM comentario")
                                    for linha in cu: print(linha)
                                case 2:
                                    args = (
                                        input("Insira conteúdo: "),
                                        # data_comentario
                                        input("Insira ID do usuário: "),
                                        input("Insira ID do arquivo: ")
                                    )    
                                    cu.execute(Inserts.newInsertComentario(*args))
                                case 3:
                                    id = input("Informe o ID do comentário que deseja atualizar: ")
                                    args = (
                                        id,
                                        input("Insira novo conteúdo: "),
                                        input("Insira novo ID do usuário: "),
                                        input("Insira novo ID do arquivo: ")
                                    )    
                                    # cu.execute(Updates.updateComentario(*args))
                                case 4:
                                    id = input("Informe o ID do comentário que deseja deletar: ")
                                    # cu.execute("DELETE comentario WHERE id = comentario.id")

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
                                        input("Insira tipo de permissão: "),
                                        # data_compartilhamento
                                        input("Insira ID do usuário origem: "),
                                        input("Insira ID do usuário destino: "),
                                        input("Insira ID do arquivo: ")
                                    )    
                                    # cu.execute(Inserts.newInsertCompartilhamento(*args))
                                case 3:
                                    id = input("Informe o ID do compartilhamento que deseja atualizar: ")
                                    args = (
                                        id,
                                        input("Insira novo tipo de permissão: "),
                                        input("Insira novo ID do usuário origem: "),
                                        input("Insira novo ID do usuário destino: "),
                                        input("Insira novo ID do arquivo: ")
                                    )    
                                    # cu.execute(Updates.updateCompartilhamento(*args))
                                case 4:
                                    id = input("Informe o ID do compartilhamento que deseja deletar: ")
                                    # cu.execute("DELETE compartilhamento WHERE id = compartilhamento.id")


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
                                    #cu.execute("SELECT * FROM atividade_recente")
                                    for linha in cu: print(linha)
                                case 2:
                                    args = (
                                        input("Insira tipo de atividade: "),
                                        input("Insira descrição: "),
                                        # data_atividade
                                        input("Insira ID do usuário: "),
                                        input("Insira ID do arquivo: ")
                                    )    
                                    # cu.execute(Inserts.newInsertAtividade(*args))
                                case 3:
                                    id = input("Informe o ID da atividade que deseja atualizar: ")
                                    args = (
                                        id,
                                        input("Insira novo tipo de atividade: "),
                                        input("Insira nova descrição: "),
                                        # data_atividade
                                        input("Insira novo ID do usuário: "),
                                        input("Insira novo ID do arquivo: ")
                                    )    
                                    # cu.execute(Updates.updateAtividade(*args))
                                case 4:
                                    id = input("Informe o ID da atividade que deseja deletar: ")
                                    # cu.execute("DELETE atividade_recente WHERE id = atividade_recente.id")

                            db.commit()
                            opcao = int(input("\nDeseja continuar?\n[0] Não\n[1] Sim\n"))