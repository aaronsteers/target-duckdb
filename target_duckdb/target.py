from singer_sdk import SQLTarget
from singer_sdk import typing as th

from target_duckdb.sink import DuckDBSink

DB_PATH_CONFIG = "filepath"


class DuckDBTarget(SQLTarget):
    """The Tap class for DuckDB."""

    name = "target-duckdb"
    default_sink_class = DuckDBSink
    max_parallelism = 1

    config_jsonschema = th.PropertiesList(
        th.Property(
            "filepath",
            th.StringType,
            description="The path to your DuckDB database file(s).",
            required=True,
        )
    )
