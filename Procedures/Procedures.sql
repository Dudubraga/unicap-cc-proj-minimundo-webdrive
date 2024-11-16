
-- Procedure para contar quantos usuarios tem um mesmo arquivo
DELIMITER $$
CREATE PROCEDURE Conta_usuarios (IN id_arq INT)
BEGIN
	DECLARE cont INT;
    
    SELECT COUNT(DISTINCT id_usuario) INTO cont FROM drive.historico WHERE id_arquivo = id_arq;
    
    SELECT cont AS qtd_usuarios;
END $$
DELIMITER ;

CALL Conta_usuarios(1);