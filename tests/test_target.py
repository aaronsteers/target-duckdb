"""Tests for the DuckDB Target."""
from __future__ import annotations

import typing as t

from singer_sdk.testing import TargetTestRunner, get_target_test_class
from target_duckdb.target import DuckDBTarget

SAMPLE_CONFIG: dict[str, t.Any] = {
    "filepath": "./test-db.duckdb",
    # TODO: Initialize minimal target config
}

# Run standard built-in target tests from the SDK:
StandardTargetTests = t.cast(
    type[TargetTestRunner],
    get_target_test_class(
        target_class=DuckDBTarget,
        config=SAMPLE_CONFIG,
    ),
)
StandardTargetTestsAlias: t.TypeAlias = StandardTargetTests


class TestDuckDBTarget(StandardTargetTests):  # type: ignore  # noqa: PGH003
    """Standard Target Tests."""

    # @pytest.fixture(scope="class")
    # def resource(self):
    #     """Generic external resource.

    #     This fixture is useful for setup and teardown of external resources,
    #     such output folders, tables, buckets etc. for use during testing.

    #     Example usage can be found in the SDK samples test suite:
    #     https://github.com/meltano/sdk/tree/main/tests/samples
    #     """
    #     yield "resource"
    #     yield "resource"
