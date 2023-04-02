"""A sample implementation for DuckDB."""

from singer_sdk import SQLSink

from target_duckdb.connector import DuckDBConnector


class DuckDBSink(SQLSink):
    """The Sink class for DuckDB.

    This class allows developers to optionally override `get_records()` and other
    stream methods in order to improve performance beyond the default SQLAlchemy-based
    interface.

    DDL and type conversion operations are delegated to the connector logic specified
    in `connector_class` or by overriding the `connector` object.
    """

    MAX_SIZE_DEFAULT = 100000
    connector_class = DuckDBConnector
