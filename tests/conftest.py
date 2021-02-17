import os, json
import socket
from sys import platform

import betamax
import pytest
from betamax import Betamax
from betamax_serializers import pretty_json

from credmgr import CredentialManager
from tests.utils import genCassetteName


def filterRefreshToken(interaction, current_cassette):  # pragma: no cover
    filterItems = ["refresh_token"]
    response = interaction.data["response"]
    body = response["body"]["string"]
    for item in filterItems:
        try:
            value = json.loads(body)[item]
            current_cassette.placeholders.append(
                betamax.cassette.cassette.Placeholder(
                    placeholder=f"<{item.upper()}>", replace=value
                )
            )
        except (KeyError, TypeError, ValueError):
            continue


def env_default(key):
    return os.environ.get(f"test_{key}", f"placeholder_{key}")


placeholders = {x: env_default(x) for x in ["api_token", "password", "username"]}

betamax.Betamax.register_serializer(pretty_json.PrettyJSONSerializer)
with betamax.Betamax.configure() as config:
    config.cassette_library_dir = f"{os.path.dirname(__file__)}/cassettes"
    config.default_cassette_options["serialize_with"] = "prettyjson"
    config.before_record(callback=filterRefreshToken)
    for key, value in placeholders.items():
        config.define_cassette_placeholder(f"<{key.upper()}>", value)


class Placeholders:
    def __init__(self, _dict):
        self.__dict__ = _dict


def pytest_configure():
    pytest.placeholders = Placeholders(placeholders)


if platform == "darwin":
    socket.gethostbyname = lambda x: "127.0.0.1"


@pytest.fixture()
def credentialManager():
    yield CredentialManager(apiToken=pytest.placeholders.api_token)


@pytest.fixture(autouse=True)
def recorder(credentialManager):
    with Betamax(credentialManager._requestor._session).use_cassette(genCassetteName()):
        yield
