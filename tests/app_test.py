import pytest

from tests.fixtures import flask_app, client


@pytest.mark.usefixtures('flask_app', 'client')
def test_smoke(client):
    pass
