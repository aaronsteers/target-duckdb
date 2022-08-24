import os
import json


def get_db_config():
    return {
        "filepath": "/tmp/integration_test.duckdb",
        "default_target_schema": "integration_test",
        "disable_table_cache": None,
        "schema_mapping": None,
        "add_metadata_columns": None,
        "hard_delete": None,
        "flush_all_streams": None,
    }


def get_test_config():
    return get_db_config()


def get_test_tap_lines(filename):
    lines = []
    with open(f"{os.path.dirname(__file__)}/resources/{filename}") as tap_stdout:
        lines.extend(iter(tap_stdout))
    return lines
