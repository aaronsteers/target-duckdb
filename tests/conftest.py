"""Shared fixtures."""


from pathlib import Path

import pytest
from singer_sdk.helpers._singer import Catalog
from singer_sdk.testing import _get_tap_catalog

from singer_duckdb import DuckDBConnector, DuckDBTap, DuckDBTarget

# Sample DB Setup and Config


@pytest.fixture
def path_to_sample_data_db(tmp_path: Path) -> Path:
    return tmp_path / Path("foo.db")


@pytest.fixture
def duckdb_sample_db_config(path_to_sample_data_db: str) -> dict:
    """Get configuration dictionary for target-csv."""
    return {"path_to_db": str(path_to_sample_data_db)}


@pytest.fixture
def duckdb_connector(duckdb_sample_db_config) -> DuckDBConnector:
    return DuckDBConnector(config=duckdb_sample_db_config)


@pytest.fixture
def duckdb_sample_db(duckdb_connector: DuckDBConnector):
    """Return a path to a newly constructed sample DB."""
    _ = duckdb_connector.connection
    for t in range(3):
        # duckdb_connector.connection.execute(f"DROP TABLE IF EXISTS t{t}")
        duckdb_connector.connection.execute(
            f"CREATE TABLE t{t} (c1 int PRIMARY KEY, c2 varchar(10))"
        )
        for x in range(100):
            duckdb_connector.connection.execute(
                f"INSERT INTO t{t} VALUES ({x}, 'x={x}')"
            )


@pytest.fixture
def duckdb_sample_tap(duckdb_sample_db, duckdb_sample_db_config) -> DuckDBTap:
    _ = duckdb_sample_db
    catalog_obj = Catalog.from_dict(
        _get_tap_catalog(DuckDBTap, config=duckdb_sample_db_config, select_all=True)
    )

    # Set stream `t1` to use incremental replication.
    t0 = catalog_obj.get_stream("main-t0")
    t0.replication_key = "c1"
    t0.replication_method = "INCREMENTAL"
    t1 = catalog_obj.get_stream("main-t1")
    t1.key_properties = ["c1"]
    t1.replication_method = "FULL_TABLE"
    t2 = catalog_obj.get_stream("main-t2")
    t2.key_properties = ["c1"]
    t2.replication_key = "c1"
    t2.replication_method = "INCREMENTAL"
    return DuckDBTap(config=duckdb_sample_db_config, catalog=catalog_obj.to_dict())


# Target Test DB Setup and Config


@pytest.fixture
def path_to_target_db(tmp_path: Path) -> Path:
    return Path(f"{tmp_path}/target_test.db")


@pytest.fixture
def duckdb_target_test_config(path_to_target_db: str) -> dict:
    """Get configuration dictionary for target-csv."""
    return {"path_to_db": str(path_to_target_db)}


@pytest.fixture
def duckdb_sample_target(duckdb_target_test_config):
    """Get a sample target object."""
    return DuckDBTarget(duckdb_target_test_config)
