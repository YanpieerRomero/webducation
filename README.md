Proyecto Webducation

Crea una nueva carpeta y llamalo proyecto_ihc

Ubicate en aquella carpeta con git bash y aplica git init

Luego aplica -> git remote add origin "https://github.com/yanpieer13/webducation.git"

Aplica git pull origin master

Ubicate mediante el cmd en la carpeta proyecto_ihc

Crea un entorno virtual en la carpeta proyecto_ihc, con el siguiente comando -> python -m venv venv  

Activa el entorno virtual con el siguiente comando -> venv\scripts\activate

Dirigite a la carpeta proyecto_ihc donde se encuentra requirements.txt y aplica en tu cmd -> pip install -r requirements.txt, para instalar las dependencias

Aplica en tu cmd pip freeze y podras visualizar todas las dependencias

Levanta el servidor con el siguiente comando -> python manage.py runserver

