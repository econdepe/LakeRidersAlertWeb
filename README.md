# LAKERIDERS ALERT WEB

Toy Django application that runs the lakeriders-alert script as a background task, and offers some UI to display its results

## LOGIC

* Refer to [lakeriders-alert](https://github.com/econdepe/LakeRidersAlert) for the inner workings of the script, although here its code has been modified slightly to work as a task instead of as a CLI command.
* The Django app uses [Celery](https://pypi.org/project/celery/) beat to run the script periodically. This requires a broker to communicate with Django. Redis has been selected for the task.

## RUNNING LAKERIDERS ALERT WEB LOCALLY

The project has been set up with [Poetry](https://python-poetry.org/docs/), so you can easily install dependencies in a virtual environment with
```
poetry shell
poetry install --no-root
```
Navigate to `lakeridersalert_web` from the root directory. Start your Redis server (the port is hardcoded at the moment), and the Django server.
```
redis-server --port 7777
python manage.py migrate
python manage.py runserver
```
Create a Celery worker and start the Celery beat scheduler
```
python -m celery -A lakeridersalert_web worker -l info
python -m celery -A lakeridersalert_web beat -l info
```

Now you can navigate to the app main page `{APP_URL}` by adding `/app` to your local Django server address (typically `http://localhost:8000/app/`). If everything has gone alright you should see the sessions of the current week, together with a list of the last five alerts emitted. At `{APP_URL}/db` you can find the current state of the DB, while `{APP_URL}/alerts` contains a list of all emitted alerts.