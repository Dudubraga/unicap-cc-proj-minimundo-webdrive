class Procedures:
    dropProcedureVerificar_atividades = "DROP PROCEDURE IF EXISTS Verificar_atividades"    
    dropProcedureConta_usuarios = "DROP PROCEDURE IF EXISTS Conta_usuarios"
    dropProcedureChavear = "DROP PROCEDURE IF EXISTS Chavear"    
    dropProcedureRemover_acessos = "DROP PROCEDURE IF EXISTS Remover_acesso" 


    createProcedureVerificar_atividades = """
        CREATE PROCEDURE Verificar_atividades()
        BEGIN
        	UPDATE atividades_recentes SET ultima_versao = CURDATE();
        END;
    """   
    
    createProcedureConta_usuarios = """
        CREATE PROCEDURE Conta_usuarios (IN id_arq INT)
        BEGIN
        	DECLARE cont INT;    
            SELECT COUNT(DISTINCT id_usercompartilhado) INTO cont FROM drive.compartilhamento WHERE id_arquivo = id_arq;
            SET cont := cont+1;
            SELECT cont AS qtd_usuarios;
        END;
    """   
    
    createProcedureChavear = """
        CREATE PROCEDURE Chavear(IN id_arq INT)
        BEGIN
        		IF (SELECT atividades_recentes.acesso FROM atividades_recentes WHERE id_arquivo = id_arq) = 'prioritário' THEN
        			UPDATE atividades_recentes SET acesso = 'não prioritário' WHERE id_arquivo = id_arq;
        		ELSE
        			UPDATE atividades_recentes SET acesso = 'prioritário' WHERE id_arquivo = id_arq;
        		END IF;
        END;
    """   
    
    createProcedureRemover_acessos = """
        DELIMITER $$
        
        CREATE PROCEDURE Remover_acessos(IN id_arq INT)
        BEGIN
        	DELETE FROM compartilhamento WHERE id_arquivo = id_arq;
        END;
    """

    def ContaUsuarios(id_arq):
        command = f"CALL Conta_usuarios({id_arq});"
        return command
    
    def VerificarAtividades():
        command = f"CALL Verificar_atividades();"
        return command
    
    def Chavear(id_arq):
        command = f"CALL Chavear({id_arq});"
        return command
    
    def RemoverAcessos(id_arq):
        command = f"CALL Remover_acessos({id_arq});"
        return command

    def dropProcedures():
        proceduresList = (Procedures.dropProcedureVerificar_atividades, Procedures.dropProcedureConta_usuarios,
                          Procedures.dropProcedureChavear, Procedures.dropProcedureRemover_acessos)
        return proceduresList

    def createProcedures():
        proceduresList = (Procedures.createProcedureVerificar_atividades, Procedures.createProcedureConta_usuarios,
                          Procedures.createProcedureChavear, Procedures.createProcedureVerificar_atividades)
        return proceduresList