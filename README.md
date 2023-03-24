<h3 align='center'>Sistema de Controle de Coleta Seletiva e Resíduos Tóxicos</h3>

Para rodar o projeto no Windows:
<br>
Abra o arquivo settings.py na pasta core, procure por <strong> databases</strong> e altere 'PASSWORD': 'digitesuasenhadomysql' conforme sua senha de usuário do mysql.

Crie a database no mysql: create database residuo; 
PowerShell Permissão: Set-ExecutionPolicy Unrestricted -Scope Process

Criando Ambiente Virtual: python -m venv venv

Ativando Ambiente: ./venv/scripts/activate

Instalando Dependências: python -r install requirements.txt

Rodando Django:

python manage.py runserver

-----------------------------

Para rodar o projeto no Linux Ubuntu:
<br>
Abra o arquivo settings.py na pasta core, procure por <strong> databases</strong> e altere 'PASSWORD': 'digitesuasenhadomysql' conforme sua senha de usuário do mysql.

Crie a database no mysql: create database residuo; 
Instalando as dependências: sudo apt-get install python3-dev default-libmysqlclient-dev build-essential

Criando Ambiente Virtual: python3 -m venv venv

Ativando Ambiente: source venv/bin/activate

Instalando Dependências: python3 -r install requirements.txt

Rodando Django:

python3 manage.py runserver

P.S .; Instale o Python 3,MySQL e clone o projeto com o <strong> git clone </strong>, antes de executar os comandos.
