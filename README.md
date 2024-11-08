# Projeto Banco de Dados: Minimundo - WebDrive
Linguagem: Deve ser feito usando uma linguagem de apoio a escolha do grupo e SQL. 
## Atividades:
1. Fazer o modelo conceitual  
2. Fazer o modelo lógico  
3. Fazer o modelo físico com as seguintes funcionalidades:  
    - Criação da base de dados  
    - Inserir objeto  
    - Buscar  
    - Atualizar  
    - Remover  

#### Implemente as seguintes visões:  
- O usuário não deve ver informações de arquivos que ele não tenha acesso, ele só verá e irá operar arquivos que ele possua acesso;  
- Os administradores terão acesso a toda base de dados;  
- O usuário terá acesso ao histórico de operações, mas ele pode apenas visualizar ela;  

Em todas as visões implementadas os ids estão ocultos e o usuário não terá acesso a eles;
#### Implemente as seguintes roles:  
- PapelUsuario – Ele terá acesso apenas aos seus arquivos ele pode selecionar, inserir e atualizar os arquivos que ele tenha permissão de acesso;  
- PapelEmpresa – Ele terá acesso aos usuários que fazem parte da empresa e aos arquivos dos funcionários, ela poderá apenas visualizar os usuários e os arquivos;  
- PapelAdm – Ele terá acesso à toda base de dados podendo visualizar, inserir, atualizar ou deletar.  
#### Crie os seguintes procedures:  
- Verificar_atividades – o procedure deve atualizar toda a tabela de atividades_recentes com a data atual;  
- Conta_usuários - Crie um procedure que receba um id de um arquivo e conte quantos  usuários diferentes o mesmo possui;  
- Chavear – Atualiza o arquivo de prioritário para não prioritário e vice-versa.  
- Remover_acessos – Crie um procedure que recebe o id de um arquivo e remove o acesso de todos os usuários menos do proprietário.  
#### Crie as seguintes funções: 
- Crie uma função que verifica se tem mais de 100 dias que o arquivo recebeu uma última alteração, caso sim retorne verdadeiro, caso não, retorne falso;  
#### Crie os seguintes triggers: 
- Safe_security – impeça que arquivos executáveis sejam inseridos no drive;  
- Registrar_operacao – Sempre que um arquivo tiver uma nova operação atualize a data da operação na tabela atividades_recentes;  
- Atualizar_acesso – Sempre que um usuário conseguir acesso a um novo arquivo, atualize os registros de arquivo dele também; 

## O Drive possui as seguintes características: 
- Os usuários possuem arquivos, estes arquivos podem ser de mídias diversas;   
- Um usuário deve ter um id, login, senha, data de ingresso e email;   
- Arquivos possuem id, nome, tipo, permissões de acesso, tamanho, data de última modificação, localização e URL;   
- O usuário opera os arquivos, podendo ser as seguintes operações: Carregar, atualizar e remover, todas as operações registradas devem ter a data e a hora associadas a elas.   
- Os arquivos podem ser compartilhados com outros usuários, tendo as seguintes informações: id do arquivo, id do dono, id do compartilhado e data de compartilhamento;   
- Um usuário pode ter vários arquivos, mas um arquivo deve estar associado a um usuário;   
- Um usuário pode compartilhar um arquivo com vários usuários;   
- O usuário também pode fazer um comentário sobre o seu arquivo, o comentário possui um id, 
conteúdo, data e hora. Um usuário pode fazer vários arquivos e um arquivo pode ser comentado por vários usuários;   
- A plataforma também acomoda instituições, a instituição possui um id, nome, causa social e 
endereço;   
- A instituição pode ter vários usuários, mas cada usuário só pode estar ligado a uma instituição;   
- A instituição adere a um plano que possui um id, nome, duração, data de aquisição e espaço por usuário (constraint em modelo físico, será implementado na segunda parte);  
- Cada instituição pode ter um plano;  
- O sistema também possui um suporte com o administrador, o administrador possui todas as informações que o usuário possui mais um id_administrador;   
- Um usuário pode ter acesso a vários adms e um adm pode suportar vários usuários;   
- Um usuário pode pedir suporte sobre um arquivo específico ou não, este suporte possui id, dia, hora e descrição;  
- Os arquivos possuem um histórico de versionamento, o histórico possui um id, data, hora, operação, id do usuário que alterou o arquivo e conteúdo mudado (sempre em formato de texto).  
- Um arquivo pode possuir um ou vários registros de versionamento, mas o registro de versionamento só pode estar vinculado a um único arquivo.

Crie uma tabela extra para controle de arquivos. A proposta é que arquivos que não são editados ou operados com frequência tendem a ser cada vez menos usado, a plataforma quer destinar acesso de qualidade aos arquivos com maior atividade. Nenhum usuário pode ter acesso à esta tabela exceto o usuário Root. Segue a estrutura da tabela:
- Atividades_recentes:  
Id_arquivo(FK) - id do arquivo que está sendo avaliado;  
Ultima_versao – um atributo tipo date que registra a última data editada do arquivo;  
Acesso – pode ser prioritário ou não prioritário.

## **Integrantes**
- Eduardo Braga
- Henrique Franca
- Isabela Medeiros
- Júlia Vilela
- Rafael Angelim
