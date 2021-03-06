# To-do List

Projeto de desenvolvimento de um To-do List inspirado no challenge https://github.com/AlayaCare/backend-python-test.

## π ComeΓ§ando
Essas instruΓ§Γ΅es permitirΓ£o que vocΓͺ obtenha uma cΓ³pia do projeto em operaΓ§Γ£o na sua mΓ‘quina local para fins de desenvolvimento e teste.

### π PrΓ©-requisitos

De que coisas vocΓͺ precisa para instalar o software e como instalΓ‘-lo?
Primeiro, clone este projeto em sua mΓ‘quina, crie um ambiente virtual e ative. Feito isso, execute o seguinte comando para instalar todas as suas dependΓͺncias:

```
pip install -r requirements.txt
```

Caso queira fazer melhorias ou alteraΓ§Γ΅es no projeto, execute este comando:
```
pre-commit install
```

ApΓ³s isso, execute este comando para criaΓ§Γ£o e migraΓ§Γ΅es do banco de dados:
```
flask db upgrade
```

Agora vocΓͺ jΓ‘ pode executar este ultimo comando para iniciar a aplicaΓ§Γ£o:
```
python app.py runserver
```

## π¨οΈ PΓ‘gina inicial do projeto

![](todolist/blueprints/users/static/images/index.jpg)

## π οΈ Estrutura do projeto
```
todo-list-app
βββ todolist/
β   βββ __init__.py
β   βββ storage.db
β   βββ blueprints/
β   β   βββ __init__.py
β   β   βββ todos/
β   β   β   βββ __init__.py
β   β   β   βββ todos.py
β   β   β   βββ templates
β   β   β       βββ todolist.html
β   β   βββ users/
β   β       βββ __init__.py
β   β       βββ users.py
β   β       βββ static/
β   β       β   βββ images/
β   β       β       βββ index.jpg
β   β       β       βββ todolist.jpg
β   β       βββ templates/
β   β           βββ base.html
β   β           βββ index.html
β   β           βββ login.html
β   β           βββ register.html
β   βββ infra/
β       βββ __init__.py
β       βββ forms/
β       β   βββ __init__.py
β       β   βββ form_login.py
β       β   βββ form_register.py
β       βββ sqlalchemy/
β           βββ __init__.py
β           βββ models/
β           |   βββ __init__.py
β           |   βββ todos.py
β           |   βββ users.py
β           βββ repositories/
β           |   βββ __init__.py
β           |   βββ repository_todo.py
β           |   βββ repository_user.py
β           βββ verifications/
β               βββ __init__.py
β               βββ verification_user.py
βββ migrations/
βββ venv/
βββ .flake8
βββ .gitignore
βββ .pre-commit-config.yaml
βββ .pylint
βββ app.py
βββ config.py
βββ README.md
βββ requirements.txt

```

## π§ ConstruΓ­do com

Ferramentas utilizadas para o desenvolvimento deste projeto:

* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Framework
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) - Database
* [Pylint](https://pypi.org/project/pylint/) - Ferramenta de anΓ‘lise de cΓ³digo estΓ‘tico do Python
* [Bootstrap](https://getbootstrap.com/docs/5.1/getting-started/introduction/) - Framework