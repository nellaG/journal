### installing rye

```
$ curl -sSf https://rye.astral.sh/get | bash

$ rye init .
```

### add dependency to rye
```
$ source .venv/bin/activate.fish
$ rye add django
$ rye sync
# see with `rye list`, requirements.lock file
```

### add pre-commit and ruff
```
$ rye add pre-commit
$ rye add ruff
add .pre-commit-config.yaml and ruff.toml

```

### django
- setting
```
$ python manage.py startapp journal
```

- create database
```
createuser -U postgres -s gallen
createdb -U gallen journal
psql -U gallen -d journal
```

- db configuration
```
src.settings.py.DATABASES
```

- db migration
```
python manage.py makemigrations journal
python manage.py migrate journal
python manage.py migrate    # auth, admin, sessions
python manage.py createsuperuser  # add admin user
```
