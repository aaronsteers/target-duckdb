from typing import Any, Dict

import pytest
from singer_sdk.testing import get_target_test_class

from target_duckdb.target import DuckDBTarget

SAMPLE_CONFIG: Dict[str, Any] = {
    "filepath": "./test-db.duckdb"
    # TODO: Initialize minimal target config
}

# Run standard built-in target tests from the SDK:
StandardTargetTests = get_target_test_class(
    target_class=DuckDBTarget, config=SAMPLE_CONFIG
)


class TestDuckDBTarget(StandardTargetTests):
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
