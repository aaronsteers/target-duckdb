"""The DuckDB Connection class."""
from __future__ import annotations

import typing as t

import sqlalchemy

from singer_sdk import typing as th

if t.TYPE_CHECKING:
    import sqlalchemy

from singer_sdk import SQLConnector


class NonSerialIntType(sqlalchemy.types.UserDefinedType):
    # TODO: Remove after resolved: https://github.com/Mause/duckdb_engine/issues/595

    cache_ok = True

    def __init__(self):
        pass

    def get_col_spec(self, **kw):
        return "INT"

    def bind_processor(self, dialect):
        def process(value):
            return value

        return process

    def result_processor(self, dialect, coltype):
        def process(value):
            return value

        return process

    @property
    def python_type(self) -> type:
        return int


class DuckDBConnector(SQLConnector):
    """The connector for DuckDB.

    This class handles all DDL and type conversions.
    """

    allow_column_add = True
    allow_column_alter = False
    allow_column_rename = True
    allow_merge_upsert = True
    allow_temp_tables = False

    def get_sqlalchemy_url(self, config: dict[str, t.Any]) -> str:
        """Generates a SQLAlchemy URL for DuckDB."""
        return f"duckdb:///{config['filepath']}"

    def create_sqlalchemy_connection(self) -> sqlalchemy.engine.Connection:
        """Return a new SQLAlchemy connection using the provided config.

        This override simply provides a more helpful error message on failure.

        Returns:
            A newly created SQLAlchemy engine object.
        """
        try:
            return super().create_sqlalchemy_connection()
        except Exception as ex:  # noqa: BLE001  # Blind catch of Exception
            raise RuntimeError(
                f"Error connecting to DB at '{self.config['filepath']}'",
            ) from ex

    @staticmethod
    def to_sql_type(jsonschema_type: dict) -> sqlalchemy.types.TypeEngine:
        """Return a JSON Schema representation of the provided type.

        By default will call `typing.to_sql_type()`.

        Developers may override this method to accept additional input argument types,
        to support non-standard types, or to provide custom typing logic.
        If overriding this method, developers should call the default implementation
        from the base class for all unhandled cases.

        Args:
            jsonschema_type: The JSON Schema representation of the source type.

        Returns:
            The SQLAlchemy type representation of the data type.
        """

        result = th.to_sql_type(jsonschema_type)
        # TODO: Remove after resolved: https://github.com/Mause/duckdb_engine/issues/595
        if (
            isinstance(result, sqlalchemy.types.INTEGER)
            # "int"
            # in repr(result).lower()
        ):
            return NonSerialIntType()

        return result
