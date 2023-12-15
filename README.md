```sh
#!/usr/bin/env bash

PROJECT_NAME="$1"

if [[ -z "$PROJECT_NAME" ]]; then
  echo "usage: create-flask-project <PROJECT_NAME>"
  exit 1
fi

git clone git@github.com:mkorman9/flask-app-template.git "${PROJECT_NAME}" && \
    rm -rf "${PROJECT_NAME}/.git" "${PROJECT_NAME}/README.md" && \
    cp "${PROJECT_NAME}/.env.template" "${PROJECT_NAME}/.env"
```
