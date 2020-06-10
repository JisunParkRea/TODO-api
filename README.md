# TODO-api

to-do app api using django rest framework


```sh
$ git clone https://github.com/JisunParkRea/TODO-api.git
$ cd TODO-api

$ python -m venv venv
$ venv\Scripts\activate
$ pip install -r local_requirements.txt
```

## Run locally

```sh
$ python manage.py makemigrations todos
$ python manage.py migrate
$ python manage.py runserver
```
localhost:8000


## Run with docker

modify VM IP address in settings, if your using docker toolbox

```sh
$ docker build -t todo-api .
$ docker run --name todo-api -p 8000:8000 -d todo-api:latest
```

YOUR_VM_IP_ADDRESS:8000