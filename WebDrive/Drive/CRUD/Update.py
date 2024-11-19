class Update:
    def updatePlano(nome, duracao, data_aquisicao, espaco_usuario, id):
        command = f"""
            UPDATE plano
            SET 
                nome = '{nome}', 
                duracao = '{duracao}', 
                data_aquisicao = '{data_aquisicao}', 
                espaco_usuario = '{espaco_usuario}'
            WHERE id = '{id}';
        """
        return command
    
    def updateInstituicao(nome, causa_social, endereco, id_plano, id):
        command = f"""
            UPDATE instituicao 
            SET 
                nome = '{nome}', 
                causa_social = '{causa_social}', 
                endereco = '{endereco}', 
                id_plano = '{id_plano}' 
            WHERE id = '{id}';
        """
        return command
    
    def updateUsuario(login, email, senha, data_ingresso, id_instituicao, id):
        command = f"""
            UPDATE usuario
            SET 
                login = '{login}', 
                email = '{email}', 
                senha = '{senha}', 
                data_ingresso = '{data_ingresso}', 
                id_instituicao = '{id_instituicao}'
            WHERE 
                id = '{id}';
        """
        return command

    def updateAdministrador(login, email, senha, data_ingresso, id):
        command = f"""
            UPDATE administrador
            SET 
                login = '{login}', 
                email = '{email}', 
                senha = '{senha}', 
                data_ingresso = '{data_ingresso}'
            WHERE 
                id = '{id}';
        """
        return command

    def updateSuporta(dia, hora, descricao, id_usuario, id_administrador, id):
        command = f"""
            UPDATE suporta
            SET 
                dia = '{dia}', 
                hora = '{hora}', 
                descricao = '{descricao}', 
                id_usuario = '{id_usuario}', 
                id_administrador = '{id_administrador}'
            WHERE 
                id = '{id}';
        """
        return command
    
    def updateArquivo(nome,tipo,URL,acesso,localizacao,tamanho,data,id_arq):
        command = f"""
            UPDATE arquivo 
            SET 
                nome='{nome}',
                tipo='{tipo}',
                URL='{URL}',
                Permissoes_acesso='{acesso}',
                localizacao='{localizacao}', 
                tamanho='{tamanho}',
                data_modificacao='{data}' 
            WHERE id = '{id_arq}';
        """
        return command
    
    def updateOpera(hora, tipo_operacao, data_operacao, id_usuario, id_arquivo, id):
        command = f"""
            UPDATE opera
            SET 
                hora = '{hora}', 
                tipo_operacao = '{tipo_operacao}', 
                data_operacao = '{data_operacao}', 
                id_usuario = '{id_usuario}', 
                id_arquivo = '{id_arquivo}'
            WHERE 
                id = '{id}';
        """
        return command

    def updateHistorico(operacao, data_operacao, hora, conteudo_alterado, id_usuario, id_arquivo, id):
        command = f"""
            UPDATE historico
            SET 
                operacao = '{operacao}', 
                data_operacao = '{data_operacao}', 
                hora = '{hora}', 
                conteudo_alterado = '{conteudo_alterado}', 
                id_usuario = '{id_usuario}', 
                id_arquivo = '{id_arquivo}'
            WHERE 
                id = '{id}';
        """
        return command

    def updateComentario(conteudo, data_comentario, hora, id_usuario, id_arquivo, id):
        command = f"""
            UPDATE comentario
            SET 
                conteudo = '{conteudo}', 
                data_comentario = '{data_comentario}', 
                hora = '{hora}', 
                id_usuario = '{id_usuario}', 
                id_arquivo = '{id_arquivo}'
            WHERE 
                id = '{id}';
        """
        return command

    def updateCompartilhamento(id_dono, id_arquivo, id_usercompartilhado, data_compartilhamento, id):
        command = f"""
            UPDATE compartilhamento
            SET 
                id_dono = '{id_dono}', 
                id_arquivo = '{id_arquivo}', 
                id_usercompartilhado = '{id_usercompartilhado}', 
                data_compartilhamento = '{data_compartilhamento}'
            WHERE 
                id = '{id}';
        """
        return command

    def updateAtividadesRecentes(ultima_versao, acesso, id_arquivo):
        command = f"""
            UPDATE Atividades_recentes
            SET 
                ultima_versao = '{ultima_versao}', 
                acesso = '{acesso}'
            WHERE 
                id_arquivo = '{id_arquivo}';
        """
        return command
