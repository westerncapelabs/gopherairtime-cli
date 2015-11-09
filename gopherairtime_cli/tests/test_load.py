""" Tests for go_cli.send. """

from unittest import TestCase
from StringIO import StringIO
import json
import types

import click
from click.testing import CliRunner

import gopherairtime_cli.load
from gopherairtime_cli.main import cli
from gopherairtime_cli.load import requests_from_csv


class TestSendCommand(TestCase):
    def setUp(self):
        self.runner = CliRunner()
        # self.api_helper = ApiHelper(self)
        # self.api_helper.patch_api(go_cli.send, 'HttpApiSender')

    def tearDown(self):
        pass

    def test_load_help(self):
        result = self.runner.invoke(cli, ['load', '--help'])
        self.assertEqual(result.exit_code, 0)
        print result.output
        self.assertTrue(
            "Load recharges via a HTTP API session"
            in result.output)
