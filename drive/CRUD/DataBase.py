class DataBase:
    CreateDataBase = "CREATE DATABASE IF NOT EXISTS drive;"
    UseDataBase = "USE drive;"
    DropDataBase = "DROP DATABASE drive;"

    createPlano = """
        CREATE TABLE IF NOT EXISTS plano(
            id INT AUTO_INCREMENT,
            nome VARCHAR(100),
            duracao INT,
            data_aquisicao DATE,
            espaco_usuario INT,
            PRIMARY KEY(id)
        );
    """
    
    createInstituicao = """
        CREATE TABLE instituicao(
	        id INT AUTO_INCREMENT,
            nome VARCHAR(100),
            causa_social VARCHAR(100),
            endereco VARCHAR(100),
            id_plano INT,
            PRIMARY KEY(id),
            FOREIGN KEY(id_plano) REFERENCES plano(id)
        );
    """
    
    createUsuario = """
        CREATE TABLE usuario(
	        id INT AUTO_INCREMENT,
            login VARCHAR(100),
            email VARCHAR(100),
            senha VARCHAR(100),
            data_ingresso DATE,
            id_instituicao INT,
            PRIMARY KEY(id),
            FOREIGN KEY(id_instituicao) REFERENCES instituicao(id)
        );
    """

    createAdministrador = """
        CREATE TABLE administrador(
            id INT AUTO_INCREMENT,
            login VARCHAR(100),
            email VARCHAR(100),
            senha VARCHAR(100),
            data_ingresso DATE,
            PRIMARY KEY(id)
        );
    """

    createSuporta = """
        CREATE TABLE suporta(
	        id INT AUTO_INCREMENT,
            dia DATE,
            hora TIME,
            descricao VARCHAR(255),
            id_usuario INT,
            id_administrador INT,
            PRIMARY KEY(id),
            FOREIGN KEY(id_usuario) REFERENCES usuario(id),
            FOREIGN KEY(id_administrador) REFERENCES administrador(id)
        );
    """

    createArquivo = """
        CREATE TABLE arquivo(
	        id INT AUTO_INCREMENT,
            nome VARCHAR(255),
            tipo VARCHAR(100),
            URL VARCHAR(100),
            Permissoes_acesso VARCHAR(100),
            localizacao VARCHAR(100),
            tamanho INT,
            data_modificacao DATE,
            id_usuario INT,
            PRIMARY KEY(id),
            FOREIGN KEY(id_usuario) REFERENCES usuario(id)
        );
    """

    createOpera = """
        CREATE TABLE opera(
            id INT AUTO_INCREMENT,
            hora TIME,
            tipo_operacao VARCHAR(100),
            data_operacao DATE,
            id_usuario INT,
            id_arquivo INT,
            PRIMARY KEY(id),
            FOREIGN KEY(id_usuario) REFERENCES usuario(id),
            FOREIGN KEY(id_arquivo) REFERENCES arquivo(id)
        );
    """
    
    createHistorico = """
        CREATE TABLE historico(
        	id INT AUTO_INCREMENT,
            operacao VARCHAR(100),
            data_operacao DATE,
            hora TIME,
            conteudo_alterado VARCHAR(100),
            id_usuario INT,
            id_arquivo INT,
            PRIMARY KEY(id),
            FOREIGN KEY(id_usuario) REFERENCES usuario(id),
            FOREIGN KEY(id_arquivo)  REFERENCES arquivo(id)
        );
    """
    
    createComentario = """
        CREATE TABLE comentario(
            id INT AUTO_INCREMENT,
            conteudo VARCHAR(150),
            data_comentario DATE,
            hora TIME,
            id_usuario INT,
            id_arquivo INT,
            PRIMARY KEY(id),
            FOREIGN KEY(id_usuario) REFERENCES usuario(id),
            FOREIGN KEY(id_arquivo) REFERENCES arquivo(id)
        );
    """
    
    createCompartilhamento = """
        CREATE TABLE compartilhamento(
        	id INT AUTO_INCREMENT,
            id_dono INT,
            id_arquivo INT,
            id_usercompartilhado INT,
            data_compartilhamento DATE,
            PRIMARY KEY(id),
            FOREIGN KEY(id_dono) REFERENCES usuario(id),
            FOREIGN KEY(id_arquivo) REFERENCES arquivo(id),
            FOREIGN KEY(id_usercompartilhado) REFERENCES usuario(id)
        );
    """

    createAtividadesRecentes = """
        CREATE TABLE atividades_recentes (
            id_arquivo INT,
            ultima_versao DATE,
            acesso ENUM('prioritário', 'não prioritário') DEFAULT 'não prioritário',
            PRIMARY KEY (id_arquivo),
            FOREIGN KEY (id_arquivo) REFERENCES arquivo(id)
        );
    """
