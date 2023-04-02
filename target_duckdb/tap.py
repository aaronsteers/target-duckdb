from singer_sdk import SQLTap

from singer_duckdb.config import tap_config
from singer_duckdb.stream import DuckDBStream


class DuckDBTap(SQLTap):
    """The Tap class for DuckDB."""

    name = "target-duckdb-sample"
    default_stream_class = DuckDBStream
    max_parallelism = 1

    config_jsonschema = tap_config.to_dict()
