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
    .venv/bin/pip freeze | grep -F -f requirements.txt > requirements.txt.frozen && \
    mv requirements.txt.frozen requirements.txt && \
    .venv/bin/pip freeze | grep -F -f requirements-dev.txt > requirements-dev.txt.frozen && \
    mv requirements-dev.txt.frozen requirements-dev.txt
```
