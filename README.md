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
$ python model_gen.py test/xls/ test/generated/
```

### Test in Django project:
```
# go to test folder
$ cd test

# install Django
$ pip install -r requirements.txt

# copy generated model files to correct directory
$ sh cp_files.sh

# test migrations
$ python django_test/manage.py makemigrations
```
