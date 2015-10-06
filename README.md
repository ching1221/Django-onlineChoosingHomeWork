# Courses-choosing online
USAGE:

cd "the project path"

you can run server:

$ python manage.py runserver 0.0.0.0:8080

then you can  view the webpage at localhost:8080, then you can add courses or projects at localhost:8080/admin/ with username:admin, password:admin. If it doesn't work. you can delete the db.sqlite3 and type below:

$ python manage.py syncdb

so you can input your admin name and password, then you run server and should first go localhost:8080/admin to add a project info, so it can work out.
