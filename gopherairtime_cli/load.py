""" Send messages via an Gopher Airtime HTTP api. """

import csv
import json

import click
import requests


@click.option(
    '--project', '-p',
    help='Project name on gopher')
@click.option(
    '--csv', type=click.File('rb'),
    help=('CSV file with columns msisdn and amount (in Rand)'))
@click.pass_context
def load(ctx, project, csv):
    """ Load recharges via a HTTP API session.
    """
    if not all((ctx.obj.token, project)):
        raise click.UsageError(
            "Please specify authentication token. See --help.")
    if not any((csv, )):
        raise click.UsageError("Please specify --csv to load")
    url = "https://gopherairtime-%s.subsvc.com/api/v1/recharges/" % project
    session = get_session(ctx.obj.token)
    if csv:
        for req in requests_from_csv(csv):
            click.echo("Loading airtime requests for %(msisdn)s." % req)
            session.post(url, data=json.dumps(req))


def requests_from_csv(csv_file):
    reader = csv.DictReader(csv_file)
    if not (set(["msisdn", "amount"]) <= set(reader.fieldnames)):
        raise click.UsageError(
            "CSV file must contain msisdn and amount column headers.")
    for data in reader:
        yield {
            "msisdn": data["msisdn"],
            "amount": data["amount"]
        }


def get_session(token):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Token: %s' % token
    }
    session = requests.Session()
    session.headers.update(headers)
    return session
