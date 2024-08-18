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


