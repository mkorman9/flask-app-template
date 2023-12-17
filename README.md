```sh
#!/usr/bin/env bash

PROJECT_NAME="$1"

if [[ -z "$PROJECT_NAME" ]]; then
  echo "usage: create-flask-project <PROJECT_NAME>"
  exit 1
fi

git clone git@github.com:mkorman9/flask-app-template.git "${PROJECT_NAME}" && \
    cd "${PROJECT_NAME}"
    rm -rf .git README.md && \
    cp .env.template .env && \
    make config && \
    .venv/bin/pip freeze > pip-freeze.tmp && \
    sed 's/$/==/' requirements.txt | grep -F -f - pip-freeze.tmp > requirements.txt.frozen && \
    mv requirements.txt.frozen requirements.txt && \
    sed 's/$/==/' requirements-dev.txt | grep -F -f - pip-freeze.tmp > requirements-dev.txt.frozen && \
    mv requirements-dev.txt.frozen requirements-dev.txt && \
    rm -f pip-freeze.tmp
```
