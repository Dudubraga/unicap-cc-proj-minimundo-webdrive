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
    def updateUsuario():
        command = f"""
        
        """
        return command
    def updateAdministrador():
        command = f"""
        
        """
        return command
    def updateSuporta():
        command = f"""
        
        """
        return command
    def updateArquivo(nome,tipo,URL,acesso,localizacao,tamanho,data,id_arq):
        command = f"""
            UPDATE arquivo SET nome='{nome}',tipo='{tipo}',URL='{URL}',
            Permissoes_acesso='{acesso}',localizacao='{localizacao}', tamanho='{tamanho}',
            data_modificacao='{data}' WHERE id = '{id_arq}';
        """
        return command
    def updateOpera():
        command = f"""
        
        """
        return command
    def updateHistorico():
        command = f"""
        
        """
        return command
    def updateComentario():
        command = f"""
        
        """
        return command
    def updateCompartilhamento():
        command = f"""
        
        """
        return command
    def updateAtividades_recentes():
        command = f"""
        
        """
        return command
    
    """
    UPDATE atividades_recentes
    SET ultima_versao = CURDATE()
    WHERE id_arquivo = NEW.id_arquivo;

    UPDATE arquivo
    SET data_modificacao = CURDATE()
    WHERE id = NEW.id_arquivo;

    """