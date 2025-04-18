# atuacao-app 📊  

**Aplicação web** para registro e gerenciamento de cálculos judiciais pelos servidores do **PNEP/AGU**, substituindo a solução legada em *Microsoft Access*.  

**Funcionalidade principal**: CRUD completo em banco de dados **SQL Server**, com interface acessível e escalável para múltiplos usuários.  

---

## Recursos  
- **Entrada de Dados**: Preenchimento dos dados do processo.  
- **Consulta Registro**: Busca pelo número do processo ou pela ID do processo.  
- **Alteração**: Alguns campos do registro podem ser modificados:
    - Número do processo
    - Nome do exequente
    - Quantidade de exequentes
    - Valor do autor
    - Valor da União  
- **Exclusão**: A exclusão do registro pode ser feita por meio da ID do processo.  

---

## Tecnologias  
- **Frontend**: Django (Bootstrap) + JavaScript.  
- **Backend**: Python.  
- **Banco de dados**: SQL Server (conexão via `mssql`).  
- **Deploy**: Docker + hospedagem em servidor interno (`VM`) da AGU.  

---

## Pré-requisitos  
- **Servidor**: SQL Server 2019+ (usuário `ATUACAO_WEB`).  
- **Usuários**: Credenciais válidas no Active Directory (ou outro sistema de autenticação da AGU).  
- **Navegador**: Chrome/Firefox atualizado.  

---

## Instalação (Desenvolvimento)  
Clone o repositório:  
````
git clone https://github.com/jrangelf/atuacao-app.git 
````
Obtenha o arquivo .env do Google Drive:   
`https://drive.google.com/file/d/1_Rh2NkjsGY7pce3rfs2Qhvd-g4iDH8uV/view?usp=drive_link` 

Extraia o ID do arquivo:  
````
ID = 1_Rh2NkjsGY7pce3rfs2Qhvd-g4iDH8uV
````
Comando `curl`:
```
curl -L "https://drive.google.com/uc?export=download&id=${ID}" -o .env
```

Se preferir:

```sh
curl -L "https://drive.google.com/uc?export=download&id=1_Rh2NkjsGY7pce3rfs2Qhvd-g4iDH8uV" -o .env
```

O arquivo .env conterá as variáveis de ambiente e de configuração para acesso ao banco de dados:
  
DB_SERVER=servidor  
DB_USER=usuario  
DB_PASSWORD=senha  
DB_NAME=nome_banco  

Rodar o build do docker compose:
```
docker compose build --no-cache
````
Subir os containers:
```
docker compose up -d
```
verificar se os containers estão funcionando:
```
docker ps
```


