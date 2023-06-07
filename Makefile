coverage:
	@coverage run --omit=my_polling_project/wsgi.py,my_polling_project/asgi.py,manage.py manage.py test > /dev/null 2>&1
	@coverage report
