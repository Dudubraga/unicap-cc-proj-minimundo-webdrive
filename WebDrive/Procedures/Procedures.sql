-- Procedure para atualizar a ultima_versao para a data atual
DELIMITER $$

CREATE PROCEDURE Verificar_atividades()
BEGIN
	UPDATE atividades_recentes SET ultima_versao = CURDATE();
END $$

DELIMITER ;

SET SQL_SAFE_UPDATES = 0; -- tive que desligar a segurança para conseguir atualizar a coluna da table toda
CALL Verificar_atividades();
SET SQL_SAFE_UPDATES = 1;
DROP PROCEDURE Verificar_atividades;

-- Procedure para contar quantos usuarios tem um mesmo arquivo
DELIMITER $$

CREATE PROCEDURE Conta_usuarios (IN id_arq INT)
BEGIN
	DECLARE cont INT;
    
    SELECT COUNT(DISTINCT id_usercompartilhado) INTO cont FROM drive.compartilhamento WHERE id_arquivo = id_arq;
    SET cont := cont+1;
    SELECT cont AS qtd_usuarios;
END $$

DELIMITER ;

CALL Conta_usuarios(1);
DROP PROCEDURE Conta_usuarios;

-- Procedure para Atualizar o arquivo de prioritario para não prioritario e vice versa;
DELIMITER $$

CREATE PROCEDURE Chavear(IN id_arq INT)
BEGIN
		IF (SELECT atividades_recentes.acesso FROM atividades_recentes WHERE id_arquivo = id_arq) = 'prioritário' THEN
			UPDATE atividades_recentes SET acesso = 'não prioritário' WHERE id_arquivo = id_arq;
		ELSE
			UPDATE atividades_recentes SET acesso = 'prioritário' WHERE id_arquivo = id_arq;
		END IF;
END $$

DELIMITER ;

CALL Chavear(3);
DROP PROCEDURE Chavear;

-- Procedure para Remover_acesso
DELIMITER $$

CREATE PROCEDURE Remover_acessos(IN id_arq INT)
BEGIN
	DELETE FROM compartilhamento WHERE id_arquivo = id_arq;
END $$

DELIMITER ;

CALL Remover_acessos(10);
