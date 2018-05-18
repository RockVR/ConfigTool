# ConfigTool
Convert xls to model class

### Use [Virtualenv](https://virtualenv.pypa.io/en/stable/)
```
$ virtualenv env -p python3
```

### Install [OpenPyXL](https://openpyxl.readthedocs.io/en/stable/index.html)
```
$ pip install openpyxl
```

### Generate model files:
```
# set XLS_FOLDER and TARGET_FOLDER
$ python model_gen.py
```

### Test in Django project:
```
# go to test folder
$ cd test

# install Django
$ pip install -r requirements.txt

# test migrations
$ python django_test/manage.py makemigrations
$ python django_test/manage.py migrate
```

### Upsert data to Django db:
```
# in test folder
# copy required scripts to project folder
$ sh cp_scripts.sh

# go to project folder
$ cd django_test

# run django shell
$ python manage.py shell

# upsert data
>> exec(open('data_gen.py').read())
```