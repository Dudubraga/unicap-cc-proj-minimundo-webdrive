import mysql.connector
#from CRUD.DataBase import DataBase

class DriveSystem:
    def __init__(self):
        print("Usuários disponíveis:\nadministrador | usuario | empresa")
        self.user = input("Digite seu usuário: ")
        self.passwd = input("Digite sua senha: ")
        self.db = None
        self.cur = None

    def conectar(self):
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user=self.user,
                passwd=self.passwd,
                database="drive"
            )
            self.cur = self.db.cursor()
            return True
        except Exception as e:
            print(f"Erro na conexão: {e}")
            return False

    def executar(self):
        sair = "nao"
        while sair == "nao":
            print("\nOperações disponíveis:")
            match self.user:
                case "usuario":
                    print("[1] Visualizar meus arquivos")
                    print("[2] Visualizar meu histórico")
                    print("[3] Inserir novo arquivo")
                    print("[4] Atualizar arquivo")
                    
                    opcao = int(input("\nEscolha uma operação: "))
                    match opcao:
                        case 1:
                            # self.cur.execute("SELECT * FROM usuarioArquivo")
                            # for row in self.cur: print(row)
                            pass
                        case 2:
                            # self.cur.execute("SELECT * FROM usuarioHistorico")
                            # for row in self.cur: print(row)
                            pass
                        case 3:
                            # args = (
                            #     input("Nome do arquivo: "),
                            #     input("Tipo: "),
                            #     input("URL: "),
                            #     # ... outros campos
                            # )
                            # self.cur.execute("INSERT INTO arquivo ...")
                            pass
                        case 4:
                            # Implementar atualização de arquivo
                            pass

                case "empresa":
                    print("[1] Visualizar usuários da empresa")
                    print("[2] Visualizar arquivos da empresa")
                    
                    opcao = int(input("\nEscolha uma operação: "))
                    match opcao:
                        case 1:
                            # self.cur.execute("SELECT * FROM empresaUsuarios")
                            # for row in self.cur: print(row)
                            pass
                        case 2:
                            # self.cur.execute("SELECT * FROM empresaArquivos")
                            # for row in self.cur: print(row)
                            pass

                case "administrador":
                    print("[1] Gerenciar usuários")
                    print("[2] Gerenciar arquivos")
                    print("[3] Visualizar histórico")
                    print("[4] Gerenciar permissões")
                    
                    opcao = int(input("\nEscolha uma operação: "))
                    match opcao:
                        case 1:
                            # Implementar CRUD de usuários
                            pass
                        case 2:
                            # Implementar CRUD de arquivos
                            pass
                        case 3:
                            # self.cur.execute("SELECT * FROM historico")
                            # for row in self.cur: print(row)
                            pass
                        case 4:
                            # Implementar gerenciamento de permissões
                            pass

            self.db.commit()
            sair = input("\nDeseja sair? (sim/nao): ")

    def encerrar(self):
        if self.cur:
            self.cur.close()
        if self.db:
            self.db.close()

def main():
    sistema = DriveSystem()
    if sistema.conectar():
        try:
            sistema.executar()
        finally:
            sistema.encerrar()

if __name__ == "__main__":
    main()