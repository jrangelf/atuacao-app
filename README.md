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
---
![image](https://github.com/user-attachments/assets/920d9431-7105-4266-9f03-308954c67e6e)
---
![image](https://github.com/user-attachments/assets/57acc003-ca60-482f-b87b-5409fc9054d4)
---
![image](https://github.com/user-attachments/assets/b8d14a74-1a83-444f-95a9-77fd5f11a16b)
---
![image](https://github.com/user-attachments/assets/915104ef-2827-4756-b872-1edb5afb9090)
---
![image](https://github.com/user-attachments/assets/61dc08bb-f1a9-4401-8fbc-875d403d191f)
---
![image](https://github.com/user-attachments/assets/5a3b215a-bf34-43d0-8e2a-83a4cae7ca93)
---
![image](https://github.com/user-attachments/assets/5f14be91-433d-4dc0-8fed-26ead894fade)
---
![image](https://github.com/user-attachments/assets/a9697ade-10c3-43e1-9032-0801a83e2dcc)
---
![image](https://github.com/user-attachments/assets/c0f01c61-f9c6-4ff9-a495-2362a3028eb0)
---
![image](https://github.com/user-attachments/assets/621c01b1-cdef-4fa3-8a13-c1394d6b9245)
---










