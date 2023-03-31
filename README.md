<h3 align='center'>Sistema de Controle de Coleta Seletiva e Resíduos Tóxicos</h3>

Para rodar o projeto no Windows:
<br>
Abra o arquivo settings.py na pasta core, procure por <strong> databases</strong> e altere 'PASSWORD': 'digitesuasenhadomysql' conforme sua senha de usuário do mysql.

Crie a database no mysql: create database residuo;<br>
PowerShell Permissão: Set-ExecutionPolicy Unrestricted -Scope Process

Criando Ambiente Virtual: python -m venv venv

Ativando Ambiente: ./venv/scripts/activate

Instalando Dependências: python -r install requirements.txt

Rodando o projeto pela primeira vez:
python manage.py makemigrations <br>
python manage.py migrate <br>
python manage.py createsuperuser <br>

Rodando Django:
python manage.py runserver

Abrindo a página do Django Admin:
http://localhost:porta/admin/

-----------------------------

Para rodar o projeto no Linux Ubuntu:
<br>
Abra o arquivo settings.py na pasta core, procure por <strong> databases</strong> e altere 'PASSWORD': 'digitesuasenhadomysql' conforme sua senha de usuário do mysql.

Crie a database no mysql: create database residuo;<br>
Instalando as dependências: sudo apt-get install python3-dev default-libmysqlclient-dev build-essential

Criando Ambiente Virtual: python3 -m venv venv

Ativando Ambiente: source venv/bin/activate

Instalando Dependências: python3 -r install requirements.txt

Rodando o projeto pela primeira vez:
python3 manage.py makemigrations <br>
python3 manage.py migrate <br>
python3 manage.py createsuperuser <br>

Rodando Django:
python3 manage.py runserver

Abrindo a página do Django Admin:
http://localhost:porta/admin/

P.S .; Instale o Python 3,MySQL e clone o projeto com o <strong> git clone </strong>, antes de executar os comandos.

_____________________________________________________________

Alunos: José Carlos Romão Da Silva Junior - 202110818
        Alex Junior Mahia Amaral - 202111245
        Renan Magalhães Farias - 202011751
        Leonardo Avelar - 202110529
        Marcelo Goncalves Braga Costa - 202110474
        
