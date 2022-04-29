## Projeto desenvolvido no curso Desenvolvedor Contratado

# api-agenda-evento
Api de Agenda de Evento

<a href='https://api-agenda-evento.herokuapp.com/teste' target='_blank'><img src="https://img.shields.io/badge/aplicação-prod-gree.svg"></a>
[![codecov](https://codecov.io/gh/michellesantosdev/api-agenda-evento/branch/main/graph/badge.svg?token=VUGSREDJOL)](https://codecov.io/gh/michellesantosdev/api-agenda-evento)



# Passo a passo para rodar a aplicação

Foi utilizado o Python 3.9

## Instalar dependências
```
pip install -r requirements-dev.txt
```

## Subir base de dados Postgres
```
docker-compose up -d
```

## Executar aplicação
```
python manage.py runserver
```

# Documentação da API
A documentação da api está disponível em `http://127.0.0.1:8000/swagger/`


# Convenções de código e testes
## Rodar convenção de código
```
flake8
```

## Rodar testes
```
pytest
```

Obs: Ambos foram implementados no CI (Github Actions)
