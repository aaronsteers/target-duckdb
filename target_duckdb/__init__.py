"""A Singer Target for DuckDB database."""
from __future__ import annotations

from target_duckdb.connector import DuckDBConnector
from target_duckdb.sink import DuckDBSink
from target_duckdb.target import DuckDBTarget

__all__ = [
    "DuckDBTarget",
    "DuckDBConnector",
    "DuckDBSink",
]
