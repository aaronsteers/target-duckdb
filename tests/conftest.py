"""Shared test setup and fixtures."""

# register the singer_sdk pytest plugin
from __future__ import annotations

pytest_plugins = ("singer_sdk.testing.pytest_plugin",)
