""" Tests for go_cli.main. """

from unittest import TestCase

from click.testing import CliRunner

from gopherairtime_cli.main import cli


class TestCli(TestCase):
    def test_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['--help'])
        self.assertEqual(result.exit_code, 0)
        self.assertTrue("Gopher Airtime command line utility."
                        in result.output)
        self.assertTrue(
            "load             Load recharges via a HTTP API session..."
            in result.output)

    def test_version(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['--version'])
        self.assertEqual(result.exit_code, 0)
        self.assertTrue("gopherairtime-cli, version " in result.output)
