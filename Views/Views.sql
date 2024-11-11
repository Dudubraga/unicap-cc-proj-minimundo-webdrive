USE drive;

-- view para usuario ver seus arquivos
CREATE VIEW usuarioArquivo AS 
SELECT 
nome AS nome_arquivo,
tipo AS tipo_arquivo,
URL,
Permissoes_acesso,
localizacao,
tamanho,
data_modificacao
FROM drive.arquivo WHERE id_usuario = 4;

-- view para usuario ver o historico dele
CREATE VIEW usuarioHistorico AS
SELECT
operacao,
data_operacao,
hora,
conteudo_alterado,
id_usuario,
id_arquivo
FROM drive.historico WHERE id_usuario = 4;

DROP VIEW usuarioArquivo;
-- criando View para empresa visualizar seus usuarios
CREATE VIEW empresaUsuarios AS
SELECT
login,
email,
data_ingresso
FROM drive.usuario WHERE id_instituicao = 1;

/*


CREATE VIEW empresaArquivos AS
SELECT
nome,
tipo,
URL,
Permissoes_acesso,
localizacao,
tamanho,
data_modificacao,
id_usuario
FROM drive.arquivo WHERE id_usuario = (SELECT usuario.id FROM drive.usuario WHERE id_instituicao = 1);
*/
DROP VIEW empresaArquivos;