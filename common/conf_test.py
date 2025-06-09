# conf_test.py
import pytest
from common.mysql_client import MySQLClient

@pytest.fixture(scope="function")
def db():
    conn = MySQLClient()
    yield conn
    conn.close()
