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
