# flask_test

First experiment

To launch:

Create Virtual Environment
```sh
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Set FLASK_APP=microblog.py
Set FLASK_ENV=development or FLASK_ENV=production

Alternatively, you can create a `.flaskenv` file with:
> FLASK_APP=microblog.py
> FLASK_ENV=`development` or `production`

Launch

```sh
$ flask run

```


OR

Use Docker:

```sh
docker run --name microblog -d -p 8000:5000 --rm -e SECRET_KEY=my-secret-key \
microblog:latest
```

To list containers:

```sh
docker ps
```

Find the container_id. To stop:

```sh
docker stop <container_id>
```
