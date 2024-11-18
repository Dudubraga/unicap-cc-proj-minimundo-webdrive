class Inserts:

    def insertDefault():
        insertDefaultPlano = """
            INSERT INTO plano (nome, duracao, data_aquisicao, espaco_usuario) VALUES
            ('Plano Básico', 12, '2024-01-01', 500),
            ('Plano Padrão', 24, '2024-02-15', 1000),
            ('Plano Premium', 36, '2024-03-10', 2000),
            ('Plano Empresarial', 48, '2024-04-20', 5000),
            ('Plano Familia', 12, '2024-05-05', 750),
            ('Plano Estudante', 6, '2024-06-01', 300),
            ('Plano Startup', 24, '2024-07-15', 1500),
            ('Plano Freelancer', 12, '2024-08-30', 800),
            ('Plano Executivo', 36, '2024-09-25', 2500),
            ('Plano Corporativo', 60, '2024-10-20', 10000);
        """
        
        insertDefaultInstituicao = """
            INSERT INTO instituicao (nome, causa_social, endereco, id_plano) VALUES
            ('empresa',)
            ('Instituto Educacional Brasil', 'Educação', 'Avenida Central, 1000, Cidade A', 1),
            ('Saúde para Todos', 'Saúde', 'Rua das Flores, 200, Cidade B', 2),
            ('Verde no Horizonte', 'Ambiente', 'Rua das Árvores, 300, Cidade C', 3),
            ('Lar Seguro', 'Habitação', 'Travessa da Paz, 400, Cidade D', 4),
            ('Direitos Humanos em Ação', 'Direitos Humanos', 'Avenida da Liberdade, 500, Cidade E', 5),
            ('Proteção Animal', 'Animais', 'Estrada dos Bichos, 600, Cidade F', 6),
            ('Tech Avançada', 'Tecnologia', 'Rua do Futuro, 700, Cidade G', 7),
            ('Arte e Cultura', 'Arte', 'Praça das Artes, 800, Cidade H', 8),
            ('Cultura Viva', 'Cultura', 'Rua da Cultura, 900, Cidade I', 9),
            ('Pesquisa e Desenvolvimento', 'Pesquisa', 'Avenida das Ciências, 1000, Cidade J', 10);
        """
        
        insertDefaultUsuario = """
            INSERT INTO usuario (login, email, senha, data_ingresso, id_instituicao) VALUES
            ('alex.rodriguez', 'alex.rodriguez@example.com', 'ar_password1', '2024-01-10', 1),
            ('usuario', 'usuario@gmail.com', 'user123', '2024-01-10',1),
            ('maria.garcia', 'maria.garcia@example.com', 'mg_password2', '2024-02-20', 2),
            ('daniel.evans', 'daniel.evans@example.com', 'de_password3', '2024-03-15', 3),
            ('sophia.hall', 'sophia.hall@example.com', 'sh_password4', '2024-04-18', 4),
            ('william.harris', 'william.harris@example.com', 'wh_password5', '2024-05-22', 5),
            ('olivia.martin', 'olivia.martin@example.com', 'om_password6', '2024-06-11', 6),
            ('lucas.king', 'lucas.king@example.com', 'lk_password7', '2024-07-27', 7),
            ('emma.scott', 'emma.scott@example.com', 'es_password8', '2024-08-14', 8),
            ('jackson.white', 'jackson.white@example.com', 'jw_password9', '2024-09-30', 9),
            ('ava.lee', 'ava.lee@example.com', 'al_password10', '2024-10-05', 10);
        """
        
        insertDefaultAdministrador = """
            INSERT INTO administrador (login, email, senha, data_ingresso) VALUES
            ('administrador', 'administrador@gmail.com','adm123','2023-01-02'),
            ('anasilva', 'ana.silva@example.com', 'ana123', '2024-01-01'),
            ('brunomartins', 'bruno.martins@example.com', 'bruno456', '2024-02-12'),
            ('carlospereira', 'carlos.pereira@example.com', 'carlos789', '2024-03-15'),
            ('danielaoliveira', 'daniela.oliveira@example.com', 'daniela1011', '2024-04-20'),
            ('eduardorocha', 'eduardo.rocha@example.com', 'eduardo1213', '2024-05-05'),
            ('fernandasouza', 'fernanda.souza@example.com', 'fernanda1415', '2024-06-18'),
            ('gustavoalmeida', 'gustavo.almeida@example.com', 'gustavo1617', '2024-07-22'),
            ('helenacosta', 'helena.costa@example.com', 'helena1819', '2024-08-30'),
            ('igorsantos', 'igor.santos@example.com', 'igor2021', '2024-09-10'),
            ('juliaramos', 'julia.ramos@example.com', 'julia2223', '2024-10-01');
        """

        insertDefaultSuporte = """
            INSERT INTO suporta (dia, hora, descricao, id_usuario, id_administrador) VALUES
            ('2024-11-01', '10:00:00', 'Suporte para configuração de conta', 2, 1),
            ('2024-11-02', '11:30:00', 'Ajuda com redefinição de senha', 3, 2),
            ('2024-11-03', '14:15:00', 'Orientação sobre uso de aplicativo', 3, 3),
            ('2024-11-04', '09:45:00', 'Assistência para backup de dados', 4, 4),
            ('2024-11-05', '13:00:00', 'Suporte para recuperação de arquivo', 5, 5),
            ('2024-11-06', '15:30:00', 'Ajuda com instalação de software', 6, 6),
            ('2024-11-07', '08:20:00', 'Orientação sobre política de segurança', 7, 7),
            ('2024-11-08', '12:10:00', 'Assistência para atualização de perfil', 8, 8),
            ('2024-11-09', '16:45:00', 'Suporte técnico geral', 9, 9),
            ('2024-11-10', '10:30:00', 'Ajuda com configuração de e-mail', 10, 10);
        """
        
        insertDefaultArquivo = """
            INSERT INTO arquivo (nome, tipo, URL, Permissoes_acesso, localizacao, tamanho, data_modificacao, id_usuario) VALUES
            ('Relatório Anual', 'Documento', 'http://example.com/relatorio2024.pdf', 'leitura', 'pasta/documentos', 2048, '2024-01-01', 2),
            ('Foto Evento', 'Imagem', 'http://example.com/fotoevento.jpg', 'leitura', 'pasta/imagens', 1024, '2024-02-15', 2),
            ('Planilha Financeira', 'Planilha', 'http://example.com/financeiro.xlsx', 'leitura-escrita', 'pasta/financeiro', 512, '2024-03-10', 3),
            ('Apresentação', 'Slide', 'http://example.com/apresentacao.pptx', 'leitura', 'pasta/apresentacoes', 3072, '2024-04-20', 4),
            ('Contrato', 'Documento', 'http://example.com/contrato.pdf', 'leitura', 'pasta/contratos', 256, '2024-05-05', 5),
            ('Vídeo Tutorial', 'Vídeo', 'http://example.com/tutorial.mp4', 'leitura', 'pasta/videos', 8192, '2024-06-01', 6),
            ('Relatório Mensal', 'Documento', 'http://example.com/relatorio_mensal.pdf', 'leitura-escrita', 'pasta/documentos', 2048, '2024-07-15', 7),
            ('Desenho Projeto', 'Imagem', 'http://example.com/projeto.jpg', 'leitura', 'pasta/projetos', 1024, '2024-08-30', 8),
            ('Documento Técnico', 'Documento', 'http://example.com/doc_tecnico.pdf', 'leitura', 'pasta/tecnico', 512, '2024-09-25', 9),
            ('Planilha Controle', 'Planilha', 'http://example.com/controle.xlsx', 'leitura-escrita', 'pasta/controle', 3072, '2024-10-20', 10);
        """

        insertDefaultOpera = """
            INSERT INTO opera (hora, tipo_operacao, data_operacao, id_usuario, id_arquivo) VALUES
            ('10:00:00', 'criação', '2024-11-01', 2, 1),
            ('11:15:00', 'modificação', '2024-11-02', 2, 3),
            ('14:30:00', 'exclusão', '2024-11-03', 3, 4),
            ('09:45:00', 'acesso', '2024-11-04', 4, 5),
            ('13:00:00', 'criação', '2024-11-05', 5, 6),
            ('15:20:00', 'modificação', '2024-11-06', 6, 7),
            ('08:10:00', 'exclusão', '2024-11-07', 7, 8),
            ('12:05:00', 'acesso', '2024-11-08', 8, 9),
            ('16:40:00', 'criação', '2024-11-09', 9, 10),
            ('10:25:00', 'modificação', '2024-11-10', 10, 11);
        """
        
        insertDefaultHistorico = """
            INSERT INTO historico (operacao, data_operacao, hora, conteudo_alterado, id_usuario, id_arquivo) VALUES
            ('criação', '2024-11-01', '10:00:00', 'Arquivo criado: Relatório Anual', 2, 1),
            ('modificação', '2024-11-02', '11:15:00', 'Arquivo modificado: Foto Evento', 2, 3),
            ('exclusão', '2024-11-03', '14:30:00', 'Arquivo excluído: Planilha Financeira', 2, 4),
            ('acesso', '2024-11-04', '09:45:00', 'Arquivo acessado: Apresentação', 4, 5),
            ('criação', '2024-11-05', '13:00:00', 'Arquivo criado: Contrato', 5, 5),
            ('modificação', '2024-11-06', '15:20:00', 'Arquivo modificado: Vídeo Tutorial', 6, 6),
            ('exclusão', '2024-11-07', '08:10:00', 'Arquivo excluído: Relatório Mensal', 7, 7),
            ('acesso', '2024-11-08', '12:05:00', 'Arquivo acessado: Desenho Projeto', 8, 8),
            ('criação', '2024-11-09', '16:40:00', 'Arquivo criado: Documento Técnico', 9, 9),
            ('modificação', '2024-11-10', '10:25:00', 'Arquivo modificado: Planilha Controle', 10, 10);
        """
        
        insertDefaultComentario = """
            INSERT INTO comentario (conteudo, data_comentario, hora, id_usuario, id_arquivo) VALUES
            ('Ótimo relatório!', '2024-11-01', '10:05:00', 2, 1),
            ('MUITO BOM!', '2024-11-02', '11:20:00', 2, 1),
            ('Planilha bem organizada.', '2024-11-03', '14:35:00', 2, 2),
            ('Apresentação clara e concisa.', '2024-11-04', '09:50:00', 4, 4),
            ('Contrato bem elaborado.', '2024-11-05', '13:10:00', 5, 5),
            ('Vídeo muito informativo.', '2024-11-06', '15:25:00', 6, 6),
            ('Relatório mensal detalhado.', '2024-11-07', '08:15:00', 7, 7),
            ('Desenho do projeto está ótimo.', '2024-11-08', '12:15:00', 8, 8),
            ('Documento técnico bem feito.', '2024-11-09', '16:50:00', 9, 9),
            ('Planilha de controle muito útil.', '2024-11-10', '10:35:00', 10, 10);
        """
        
        insertDefaultCompartilhamento = """
            INSERT INTO compartilhamento (id_dono, id_arquivo, id_usercompartilhado, data_compartilhamento) VALUES
            (2, 1, 3, '2024-11-01'),
            (2, 3, 3, '2024-11-02'),
            (2, 1, 4, '2024-11-03'),
            (2, 1, 5, '2024-11-04'),
            (2, 1, 6, '2024-11-05'),
            (6, 6, 7, '2024-11-06'),
            (7, 7, 8, '2024-11-07'),
            (8, 8, 9, '2024-11-08'),
            (9, 9, 10, '2024-11-09'),
            (10, 10, 9, '2024-11-10');
        """

        insertDefaulttAtividades_recentes = """
            INSERT INTO Atividades_recentes (id_arquivo, ultima_versao, acesso) VALUES
            (1, '2024-11-01', 'prioritário'),
            (2, '2024-11-02', 'não prioritário'),
            (3, '2024-11-03', 'prioritário'),
            (4, '2024-11-04', 'não prioritário'),
            (5, '2024-11-05', 'prioritário'),
            (6, '2024-11-06', 'não prioritário'),
            (7, '2024-11-07', 'prioritário'),
            (8, '2024-11-08', 'não prioritário'),
            (9, '2024-11-09', 'prioritário'),
            (10, '2024-11-10', 'não prioritário');
        """

        insertDefaultList = (insertDefaultArquivo, insertDefaultAdministrador, insertDefaultComentario,
                             insertDefaultCompartilhamento, insertDefaultHistorico, insertDefaultInstituicao,
                             insertDefaultOpera, insertDefaultPlano, insertDefaultSuporte, insertDefaultUsuario, 
                             insertDefaulttAtividades_recentes)
        return insertDefaultList

    def newInsertPlano(nome,duracao, data_aquisicao, espaco_usuario):
        command = f"""
            INSERT INTO plano(nome, duracao, data_aquisicao, espaco_usuario)
            VALUES('{nome}', '{duracao}', '{data_aquisicao}', '{espaco_usuario}')
        """
        return command
    
    def newInsertInstituicao(nome, causa_social, endereco, id_plano):
        command = f"""
            INSERT INTO instituicao(nome, causa_social, endereco, id_plano)
            VALUES('{nome}', '{causa_social}', '{endereco}', '{id_plano}')
        """
        return command

    def newInsertUsuario(login,email,senha,data_ingresso,id_instituicao):
        command = f"""
            INSERT INTO usuario(login, email, senha, data_ingresso, id_instituicao)
            VALUES('{login}','{email}','{senha}','{data_ingresso}', '{id_instituicao}')
        """    
        return command

    def newInsertAdministrador(login,email,senha,data_ingresso):
        command = f"""
            INSERT INTO administrador(login,email,senha,data_ingresso)
            VALUES('{login}','{email}','{senha}','{data_ingresso}')
        """
        return command
    
    def newInsertSuporta(dia,hora,descricao,id_usuario,id_administrador):
        command = f"""
            INSERT INTO suporta(dia,hora,descricao,id_usuario,id_administrador)
            VALUES('{dia}','{hora}','{descricao}','{id_usuario}','{id_administrador}')
        """
        return command
    
    def newInsertArquivo(nome, tipo, URL, Permissoes_acesso, localizacao, tamanho, data_modificacao):
        command = f"""
            INSERT INTO arquivo(nome, tipo, URL, Permissoes_acesso, localizacao, tamanho, data_modificacao, id_usuario)
            VALUES('{nome}','{tipo}','{URL}','{Permissoes_acesso}','{localizacao}','{tamanho}', '{data_modificacao}', 2)
        """
        return command
    
    def newInsertOpera(hora, tipo_operacao, data_operacao, id_usuario, id_arquivo):
        command = f"""
            INSERT INTO opera (hora, tipo_operacao, data_operacao, id_usuario, id_arquivo)
            VALUES('{hora}', '{tipo_operacao}', '{data_operacao}', '{id_usuario}', '{id_arquivo}')
        """
        return command
    
    def newInsertHistorico(operacao, data_operacao, hora, conteudo_alterado, id_usuario, id_arquivo):
        command = f"""
            INSERT INTO historico(operacao, data_operacao, hora, conteudo_alterado, id_usuario, id_arquivo)
            VALUES('{operacao}','{data_operacao}','{hora}','{conteudo_alterado}','{id_usuario}')
        """
        return command


    def newInsertComentario(conteudo, data_comentario, hora, id_usuario, id_arquivo):
        command = f"""
            INSERT INTO comentario (conteudo, data_comentario, hora, id_usuario, id_arquivo)
            VALUES('{conteudo}', '{data_comentario}', '{hora}', '{id_usuario}', '{id_arquivo}')
        """
        return command
    
    def newInsertCompartilhamento(id_dono, id_arquivo, id_usercompartilhado, data_compartilhamento):
        command = f"""
            INSERT INTO compartilhamento(id_dono, id_arquivo, id_usercompartilhado, data_compartilhamento)
            VALUES('{id_dono}','{id_arquivo}','{id_usercompartilhado}','{data_compartilhamento}')
        """
        return command

    def newInsertAtividades_recente(id_arquivo, ultima_versao, acesso):
        command = f"""
            INSERT INTO Atividades_recentes (id_arquivo, ultima_versao, acesso)
            VALUES('{id_arquivo}', '{ultima_versao}', '{acesso}')
        """
        return command
    
    