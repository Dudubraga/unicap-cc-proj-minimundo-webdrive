USE drive;

CREATE VIEW usuarioArquivo AS 
SELECT nome AS nome_arquivo,
tipo AS tipo_arquivo,
URL,
Permissoes_acesso,
localizacao,
tamanho,
data_modificacao
FROM drive.arquivo WHERE id_usuario = 4;




