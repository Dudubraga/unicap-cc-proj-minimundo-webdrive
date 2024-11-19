class Delete:
    def deleteUsuario(id):
        command = f"""
            DELETE FROM usuario
            WHERE id = '{id}';
        """
        return command

    def deleteAdministrador(id):
        command = f"""
            DELETE FROM administrador
            WHERE id = '{id}';
        """
        return command

    def deleteSuporta(id):
        command = f"""
            DELETE FROM suporta
            WHERE id = '{id}';
        """
        return command

    def deleteArquivo(id):
        command = f"""
            DELETE FROM arquivo
            WHERE id = '{id}';
        """
        return command

    def deleteOpera(id):
        command = f"""
            DELETE FROM opera
            WHERE id = '{id}';
        """
        return command

    def deleteHistorico(id):
        command = f"""
            DELETE FROM historico
            WHERE id = '{id}';
        """
        return command

    def deleteComentario(id):
        command = f"""
            DELETE FROM comentario
            WHERE id = '{id}';
        """
        return command

    def deleteCompartilhamento(id):
        command = f"""
            DELETE FROM compartilhamento
            WHERE id = '{id}';
        """
        return command

    def deleteAtividadesRecentes(id_arquivo):
        command = f"""
            DELETE FROM Atividades_recentes
            WHERE id_arquivo = '{id_arquivo}';
        """
        return command

    def deletePlano(id):
        command = f"""
            DELETE FROM plano
            WHERE id = '{id}';
        """
        return command
    
    def deleteInstituicao(id):
        command = f"""
            DELETE FROM instituicao
            WHERE id = '{id}';
        """
        return command
    