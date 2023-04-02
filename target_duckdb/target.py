from singer_sdk import SQLTarget

from singer_duckdb.config import target_config
from singer_duckdb.sink import DuckDBSink

DB_PATH_CONFIG = "path_to_db"


class DuckDBTarget(SQLTarget):
    """The Tap class for DuckDB."""

    name = "target-duckdb-sample"
    default_sink_class = DuckDBSink
    max_parallelism = 1

    config_jsonschema = target_config.to_dict()
