# Aplicação de simulado em Django 4, SQLite e Bootstrap 5

## Este projeto foi feito com

* [Python 3.10.6](https://www.python.org/)
* [Django 4.1.7](https://www.djangoproject.com/)

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/msjrdev/quiz_django.git
cd quiz_django
python3 -m venv quizenv
source quizenv/bin/activate
pip install -r requirements.txt


cd quizapp
python manage.py migrate
python manage.py createsuperuser --email="admin@email.com"
python manage.py runserver
```

## Características

------------------

* Categoria do questionário
  * Nome
  * Detalhe
  * Imagem
* Perguntas do questionário de acordo com a categoria
  * Categoria
  * Pergunta
  * Opção 1
  * Opção 2
  * Opção 3
  * Opção 4
  * Opção 5
  * Nível de dificuldade
  * Limite de tempo em segundos
  * Resposta correta
* Usuário
  * Registro
  * Conecte-se
  * Esqueceu a senha
  * Painel
    * Veja o questionário enviado de acordo com a categoria
    * Ver resultado do questionário
