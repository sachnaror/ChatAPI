# django-chat-app-project

A basic realtime chat app project written with the Django framework and Django Channels.

## Local Server

To run the project locally.

- `$ python -m venv venv`
- `$ source venv/bin/activate`
- `$ pip install -r requirements.txt`
- `$ python manage.py migrate`
- Make sure you have >= redis-5.0 installed on your system
- `$ python manage.py channels_layer`
- `$ python manage.py runserver`
- Visit <http://localhost:8000>
