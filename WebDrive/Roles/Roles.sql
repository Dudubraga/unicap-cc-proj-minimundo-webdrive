-- criando o papel usuario
CREATE ROLE 'papelusuario';
GRANT SELECT ON usuarioArquivo TO 'papelusuario';
GRANT SELECT ON usuarioHistorico TO 'papelusuario';
GRANT SELECT (id) ,INSERT, UPDATE ON drive.arquivo TO 'papelusuario';
GRANT 'papelusuario' TO 'usuario'@'localhost';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'papelusuario';
DROP ROLE 'papelusuario';

-- criando o papel empresa
CREATE ROLE 'papelempresa';
GRANT SELECT ON empresaUsuarios TO 'papelempresa';
GRANT SELECT ON empresaArquivos TO 'papelempresa';
GRANT 'papelempresa' TO 'empresa'@'localhost';
FLUSH PRIVILEGES;

-- criando o papel administrador
CREATE ROLE 'papeladministrador';
GRANT SELECT, INSERT, UPDATE, DELETE ON drive.* TO 'papeladministrador';
GRANT 'papeladministrador' TO 'administrador'@'localhost';
FLUSH PRIVILEGES;



SHOW GRANTS FOR 'papelempresa';
SHOW GRANTS FOR 'empresa'@'localhost';
DROP ROLE 'papelempresa';
DROP USER 'administrador'@'localhost';