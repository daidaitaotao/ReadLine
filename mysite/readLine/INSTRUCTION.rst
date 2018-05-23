=====
ReadLine
=====

ReadLine is a Django app that allows users to read the line of a file by given line number

This is version 0.1.1 of this app.

Quick start
-----------

Pre-step. Create a virtualenv and install django:
    a. 'pip3 install virtualenv'
    b. 'python3 -m venv salsify'
    c. 'cd salsify'
    d. 'source bin/activate'
    e. 'pip3 install django'

1. Check the requirements for this app in requirement.txt in 'mysite/requirements.txt' `pip3 freeze > requirements.txt`
    If you wish to install all required libraries, simply run 'pip3 install -r requirements.txt'

2. Add "ReadLine" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        'rest_framework',
        'readLine.apps.ReadlineConfig',
    ]

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
            'OPTIONS': {
                'server_max_value_length': 1024 * 1024 * 2,
            }
        }
    }

3. Make sure you have memcached installed and configured:
    a. Run `brew install memcached`
    b. Run `pip3 install python-memcached`
    c. Run `brew services start memcached`

3. Include the readLine URLconf in your project urls.py like this::

    urlpatterns = [
        path('lines/', include('readLine.urls')),
        path('admin/', admin.site.urls),
    ]

4. Run 'python3 manage.py shell < readLine/create_small_test_data_file.py' to create a input file to test against.

5. Run 'python3 manage.py shell < readLine/create_index_file.py' to create the index file and the meta file.

6. Run 'python manage.py runserver' to start the server

7. Go to the front page http://127.0.0.1:8000/lines/, there will be a short introduction of the API.

8. To make a reading line request such as line #1, go to http://127.0.0.1:8000/lines/1/, you should be able to read the
    line from the page.

9. (Optional) to run the unit tests, Run 'python manage.py test'

Additional Steps if you wish to store the index file into database

10. Run 'python3 manage.py migrate' to create the readline models.

11. Run 'python3 manage.py shell < readLine/create_index_in_db.py' to insert file line index to database.

12. Go to `readLine/views.py` change the following function names
    from
    'find_max_line_number_from_meta_file' and 'find_line_from_index_file'
    to
    'find_max_line_number_from_db' and 'find_line_from_db'

13. repeat step 8, you should be able to making the requests.

