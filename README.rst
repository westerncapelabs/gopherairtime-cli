Gopher Airtime command line interface
==============================

A command line interface for `Gopher Airtime`_ HTTP APIs.

.. _Gopher Airtime: http://github.com/westerncapelabs/gopherairtime


Installation
------------

Install with::

  $ pip install --user gopherairtime-cli

Then run::

  $ gopherairtime-cli --help

and read the usage instructions.


Loading airtime requests
----------------

Run::

  $ gopherairtime-cli load --help

to learn about the options available for queuing.

Example message sending::

  $ gopherairtime-cli \
             --token secret-token-provided \
             load \
             --project projectname \
             --csv queue.csv

Where `queue.csv` looks something like (where amount is value in Rand)::

  msisdn,amount
  +12345678,10
  +12345679,5




Reporting issues
----------------

You can contact the Gopher Airtime development team in the following ways:

* via *email* to `support@westerncapelabs.com`

Issues can be filed in the GitHub issue tracker. Please don't use the issue
tracker for general support queries.


Thanks
----------------

To Praekelt Foundation for their inspiration via the Vumi Go CLI tool
