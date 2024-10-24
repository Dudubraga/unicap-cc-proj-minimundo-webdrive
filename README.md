# Projeto Banco de Dados: Minimundo - Drive
**Atividades:**
1. Fazer o modelo conceitual  
2. Fazer o modelo lógico  
3. Fazer o modelo físico com as seguintes funcionalidades:  
    - Criação da base de dados  
    - Inserir objeto  
    - Buscar  
    - Atualizar  
    - Remover  

**O Drive possui as seguintes características:**
- Os usuários possuem arquivos, estes arquivos podem ser de mídias diversas;  
- Um usuário deve ter um id, login, senha, data de ingresso e email;  
- Arquivos possuem id, nome, tipo, permissões de acesso, tamanho, data de 
última modificação, localização e URL;  
- O usuário opera os arquivos, podendo ser as seguintes operações: Carregar, 
atualizar e remover, todas as operações registradas devem ter a data e a hora 
associadas a elas.  
- Os arquivos podem ser compartilhados com outros usuários, tendo as seguintes 
informações: id do arquivo, id do dono, id do compartilhado e data de 
compartilhamento;  
- Um usuário pode ter vários arquivos, mas um arquivo deve estar associado a um 
usuário;  
- Um usuário pode compartilhar um arquivo com vários usuários;  
- O usuário também pode fazer um comentário sobre o seu arquivo, o comentário 
possui um id, conteúdo, data e hora. Um usuário pode fazer vários arquivos e 
um arquivo pode ser comentado por vários usuários;  
- A plataforma também acomoda instituições, a instituição possui um id, nome, 
causa social e endereço;  
- A instituição pode ter vários usuários, mas cada usuário só pode estar ligado à 
uma instituição;  
- A instituição adere a um plano que possui um id, nome, duração, data de 
aquisição e espaço por usuário (constraint em modelo físico, será implementado 
na segunda parte); 
- Cada instituição pode ter um plano; 
- O sistema também possui um suporte com o administrador, o administrador 
possui todas as informações que o usuário possui mais um id_administrador;  
- Um usuário pode ter acesso a vários adms e um adm pode suportar vários 
usuários;  
- Um usuário pode pedir suporte sobre um arquivo específico ou não, este suporte 
possui id, dia, hora e descrição; 
- Os arquivos possuem um histórico de versionamento, o histórico possui um id, 
data, hora, operação, id do usuário que alterou o arquivo e conteúdo mudado 
(sempre em formato de texto). 
- Um arquivo pode possuir um ou vários registros de versionamento, mas o 
registro de versionamento só pode estar vinculado a um único arquivo.