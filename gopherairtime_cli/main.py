""" Command line interface to Gopher Airtime's HTTP APIs. """

import click

import gopherairtime_cli.load


class GopherAirtimeCliContext(object):
    def __init__(self):
        self.token = None


@click.group(name="gopherairtime-cli")
@click.version_option()
@click.option('--token', '-t', help='Gopher Airtime Auth Token')
@click.pass_context
def cli(ctx, token):
    """ Gopher Airtime command line utility. """
    ctx.auto_envvar_prefix = 'GOPHERAIRTIME_CLI'
    ctx.obj = GopherAirtimeCliContext()
    ctx.obj.token = token


cli.command('load')(gopherairtime_cli.load.load)
