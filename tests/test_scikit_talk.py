#!/usr/bin/env python

"""Tests for `scikit_talk` package."""


import unittest
from click.testing import CliRunner

from scikit_talk import scikit_talk
from scikit_talk import cli


class TestScikit_talk(unittest.TestCase):
    """Tests for `scikit_talk` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'scikit_talk.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
