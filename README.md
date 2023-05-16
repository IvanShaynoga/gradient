# gradient
actors agensy

для запуска:
python -m venv venv
source venv/scripts/activate
cd gradient
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

создание админа 
python manage.py createsuperuser

актёры доступны по эндпоинту api/actors
