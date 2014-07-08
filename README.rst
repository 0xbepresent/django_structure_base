=====================
Django Structure Base
=====================

Provides a structure base for django projects.

{{project_name}} = The name of your project

Create project with template
----------------------------

$ django-admin.py startproject --template=https://github.com/misalabs/django_structure_base/zipball/master --extension=py,rst,gitignore,example {{project_name}}


Quickstart
----------

    $ virtualenv env_{{project_name}}
    $ source env_{{project_name}}/bin/activate
    $ cd /path/to/{{project_name}}/
    $ pip install -r requirements.txt
    $ cp settings/local.py.example settings/local.py
    $ python manage.py runserver 8001
