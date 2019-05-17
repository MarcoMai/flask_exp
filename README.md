# flask_test


Build the image:

```
docker build -t marco/flask:dev .
```

Run the image:

```
docker run -it -p 5000:5000 marco/flask:dev
```


For fast dev you can do this:

```
docker run -it -v "$PWD":/app marco/flask:dev bash
python run.py
```

Then make local changes in your editor then you can CTRL+C to stop the server then `python run.py` to start again
