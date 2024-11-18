class Select:
    def selectPlano():
        command = f"""
            SELECT * FROM plano;
        """
        return command
    
    def selectInstituicao():
        command = f"""
            SELECT * FROM instituicao; 
        """
        return command
    
    def selectUsuario():
        command = f"""
            SELECT * FROM usuario; 
        """
        return command
    
    def selectAdministrador():
        command = f"""
            SELECT * FROM administrador;
        """
        return command
    
    def selectSuporta():
        command = f"""
            SELECT * FROM suporta; 
        """
        return command
    
    def selectArquivo():
        command = f"""
            SELECT * FROM arquivo; 
        """
        return command
    
    def selectOpera():
        command = f"""
            SELECT * FROM opera; 
        """
        return command
    
    def selectHistorico():
        command = f"""
            SELECT * FROM historico;
        """
        return command
    
    def selectComentario():
        command = f"""
            SELECT * FROM comentario;
        """
        return command
    
    def selectCompartilhamento():
        command = f"""
            SELECT * FROM compartilhamento
        """
        return command
    
    def selectAtividades_recentes():
        command = f"""
            SELECT * FROM Atividades_recentes 
        """
        return command
    
    #view usuario
    def selectUsuarioArquivos():
        command = f"""
            SELECT * FROM usuarioArquivo;
        """
        return command
    
    def selectUsuarioHistorico():
        command = f"""
            SELECT * FROM usuarioHistorico;
        """
        return command
    
    #view empresa
    def selectEmpresaUsuarios():
        command = f"""
            SELECT * FROM empresaUsuarios;
        """
        return command
    
    def selectEmpresaArquivos():
        command = f"""
            SELECT * FROM empresaArquivos;
        """
        return command    
    
    