# To-do List

Projeto de desenvolvimento de um To-do List inspirado no challenge https://github.com/AlayaCare/backend-python-test.

## 🚀 Começando
Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

### 📋 Pré-requisitos

De que coisas você precisa para instalar o software e como instalá-lo?
Primeiro, clone este projeto em sua máquina, crie um ambiente virtual e ative. Feito isso, execute o seguinte comando para instalar todas as suas dependências:

```
pip install -r requirements.txt
```

Após isso, execute estes comandos para criação e migrações do banco de dados:
```
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

Agora você já pode executar este ultimo comando para iniciar a aplicação:
```
python app.py runserver
```

## 🛠️ Construído com

Ferramentas utilizadas para o desenvolvimento deste projeto:

* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Framework
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) - Database
* [Pylint](https://pypi.org/project/pylint/) - Ferramenta de análise de código estático do Python