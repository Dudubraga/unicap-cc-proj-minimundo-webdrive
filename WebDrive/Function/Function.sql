-- Function para verificar se tem mais de 100 dias que o arquivo foi alterado
DELIMITER $$
CREATE FUNCTION Verificar_data(id_arq INT)
RETURNS BOOLEAN
BEGIN
	DECLARE data_tab DATE;
    SET data_tab := (SELECT arquivo.data_modificacao FROM arquivo WHERE id = id_arq);
	IF DATEDIFF(CURDATE(),data_tab) > 100 THEN
		RETURN TRUE;
    ELSE
		RETURN FALSE;
	END IF;
END $$
    
DELIMITER ;
DROP FUNCTION Verificar_data;
SELECT Verificar_data(12) AS resp;
