SELECT * FROM drive.arquivo;

INSERT INTO arquivo(nome,tipo,URL,Permissoes_acesso,localizacao,tamanho,data_modificacao,id_usuario)VALUES('ÁrvoresB+', 'exe','httpl...','escrita', 'pasta/B',245,'2024-11-17', 7);
DELETE FROM arquivo WHERE id = 13;

-- Trigger para não deixar arquivos executaveis serem inseridos na tabela de arquivos
DELIMITER $$

CREATE TRIGGER Safe_security
BEFORE INSERT ON arquivo
FOR EACH ROW
BEGIN
    IF NEW.tipo = 'exe' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Arquivos executáveis não são permitidos no drive.';
    END IF;
END $$

DELIMITER ;
