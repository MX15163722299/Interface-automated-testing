# conftest.py
import pytest
from common.mysql_client import MySQLClient

@pytest.fixture(scope="module")
def db():
    conn = MySQLClient()
    yield conn
    conn.close()
