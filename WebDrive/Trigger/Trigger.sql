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

-- Trigger para atualizar a data de ultima versao em atividades_recentes
DELIMITER $$

CREATE TRIGGER Registrar_operacao
AFTER INSERT ON opera
FOR EACH ROW
BEGIN
    -- Atualiza a data da última versão na tabela atividades_recentes
    UPDATE atividades_recentes
    SET ultima_versao = CURDATE()
    WHERE id_arquivo = NEW.id_arquivo;
    -- Atualiza a data da última versão na tabela arquivo
    UPDATE arquivo
    SET data_modificacao = CURDATE()
    WHERE id = NEW.id_arquivo;
END $$

DELIMITER ;

-- Trigger para atualizar os registros de um novo acesso
DELIMITER $$

CREATE TRIGGER Atualizar_acesso
AFTER INSERT ON compartilhamento
FOR EACH ROW
BEGIN
    -- Atualiza a data da última versão na tabela atividades_recentes
    UPDATE atividades_recentes
    SET ultima_versao = CURDATE()
    WHERE id_arquivo = NEW.id_arquivo;
    -- Atualiza a data da última versão na tabela arquivo
    UPDATE arquivo
    SET data_modificacao = CURDATE()
    WHERE id = NEW.id_arquivo;    
END $$

DELIMITER;

INSERT INTO opera (hora, tipo_operacao, data_operacao, id_usuario, id_arquivo) VALUES
('17:30:00', 'modificação', '2024-11-17', 5, 5);
DROP TRIGGER Registrar_operacao;


