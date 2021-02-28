import json
import os.path

import ftputil
import pytest

from fixture.application import Application
from fixture.db import DbFixture

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request, config):
    global fixture
    browser = request.config.getoption("--browser")
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser, config=config)
    return fixture


@pytest.fixture(scope="session")
def db(request, config):
    dbfixture = DbFixture(host=config["db"]['host'], database=config["db"]['database'], user=config["db"]['user'],
                          password=config["db"]['password'])

    def fin():
        dbfixture.destroy()

    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def end():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(end)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")


@pytest.fixture(scope="session", autouse=True)
def configure_server(request, config):
    install_server_configuration(config["ftp"]["host"], config["ftp"]["user"], config["ftp"]["password"])

    def fin():
        restore_server_configuration(config["ftp"]["host"], config["ftp"]["user"], config["ftp"]["password"])

    request.addfinalizer(fin)


def install_server_configuration(host, user, password):
    with ftputil.FTPHost(host, user, password) as remote:
        if remote.path.isfile("config_inc.php.bak"):
            remote.remove("config_inc.php.bak")
        if remote.path.isfile("config_inc.php"):
            remote.rename("config_inc.php", "config_inc.php.bak")
        remote.upload(os.path.join(os.path.dirname(__file__), "resources/config_inc.php"), "config_inc.php")


def restore_server_configuration(host, user, password):
    with ftputil.FTPHost(host, user, password) as remote:
        if remote.path.isfile("config_inc.php.bak"):
            if remote.path.isfile("config_inc.php"):
                remote.remove("config_inc.php")
            remote.rename("config_inc.php.bak", "config_inc.php")


@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--target"))
