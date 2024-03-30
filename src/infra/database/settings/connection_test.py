import pytest
from .connection import DBConnectionHandler


@pytest.mark.skip(reason="Sensive test")
def test_create_database_engine():
    db_connection = DBConnectionHandler()
    engine = db_connection.get_engine()
    print(engine)
    assert engine is not None
