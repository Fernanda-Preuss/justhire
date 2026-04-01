1.Instalar o Python (se não tiver)
Baixar em [python.org/downloads](https://www.python.org/downloads/) — marcar "Add Python to PATH" na instalação.

2.Abrir o terminal na pasta do projeto e rodar:
# Instalar o Django e o driver do banco
`pip install django psycopg2-binary`

# Aplicar as tabelas no banco
`python manage.py migrate`

# Criar o usuário administrador
`python manage.py createsuperuser`

# Iniciar o servidor
`python manage.py runserver`

3.Acessar no navegador:
Site - `http://127.0.0.1:8000`
Admin - `http://127.0.0.1:8000/admin`
