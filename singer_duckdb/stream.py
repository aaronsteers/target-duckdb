"""A sample implementation for DuckDB."""

from singer_sdk import SQLStream

from singer_duckdb.connector import DuckDBConnector


class DuckDBStream(SQLStream):
    """The Stream class for DuckDB.

    This class allows developers to optionally override `process_batch()` and other
    sink methods in order to improve performance beyond the default SQLAlchemy-based
    interface.

    DDL and type conversion operations are delegated to the connector logic specified
    in `connector_class` or by overriding the `connector` object.
    """

    connector_class = DuckDBConnector
