-- criando o papel usuario
CREATE ROLE 'papelusuario';
GRANT SELECT ON usuarioArquivo TO 'papelusuario';
GRANT SELECT ON usuarioHistorico TO 'papelusuario';
GRANT SELECT (id) ,INSERT, UPDATE ON drive.arquivo TO 'papelusuario';
GRANT 'papelusuario' TO 'usuario'@'localhost';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'papelusuario';
DROP ROLE 'papelusuario';

