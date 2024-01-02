# Alimentação BD - Python/SQL
Script criado com o intuito de enviar tabelas .csv para o banco de dados à fim de melhorar a análise dos dados.

## Indice
- <a href='#Funcionalidades'> Funcionalidades </a>
- <a href='#Rodar'> Como rodar este projeto? </a>
- <a href='#Tecnologias'> Tecnologias Utilizadas </a>

## Funcionalidades do Projeto
- Leitura de arquivo .csv.
- Conexão com o banco de dados SQL Server com instância AWS.
- Criação de tabelas no BD.
- Envio de dados.

## Como rodar este projeto?
- O script principal é o modelar.py
- Os arquivos CSV a serem enviados estão armazenados na pasta Engenheiro de Dados - CSV.
- Necessário o Python instalado no ambiente.
- Atualize as configurações da instância no arquivo Classes/alchmeyBRAZ.py, na linha onde engine.GenEngine é chamado.
- Execute o script principal.
- O script lerá os arquivos CSV na pasta Engenheiro de Dados - CSV e enviará para o banco de dados configurado.

## Tecnologias Utilizadas

1. Python
2. Pandas
3. SQL Alchemy
4. SQL Server
5. AWS RDS 


