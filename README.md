# sage-numerical-backends-coin: COIN-OR mixed integer linear programming backend for SageMath

[![PyPI](https://img.shields.io/pypi/v/sage-numerical-backends-coin)](https://pypi.org/project/sage-numerical-backends-coin/ "PyPI: sage-numerical-backends-coin")
[![GitHub Workflow Status](https://github.com/sagemath/sage-numerical-backends-coin/workflows/Build%20and%20test%20Python%20package/badge.svg)](https://github.com/sagemath/sage-numerical-backends-coin/actions "GitHub Actions: sage-numerical-backends-coin")

`CoinBackend` has previously been available as part of the [SageMath](http://www.sagemath.org/) source tree,
from which it is built as an "optional extension" when the `cbc` Sage package is installed.
However, it has not been available in binary distributions.

The present standalone Python package `sage-numerical-backends-coin` has been created from the SageMath sources, version 9.0.beta10; the in-tree version of `CoinBackend` has been removed in Sage ticket https://trac.sagemath.org/ticket/28175.  SageMath 9.1 and later makes the package available as an optional Sage package (SPKG).

The current version of this package can also be installed on top of various Sage installations using pip.
(Your installation of Sage must be based on Python 3; if your SageMath is version 9.2 or newer, it is.)

## Installation

CBC can either be installed using its Sage package using

    $ sage -i cbc

or any of the methods explained at https://github.com/coin-or/Cbc .

This package finds the CBC installation by means of ``pkgconfig``.

Install this package from PyPI using

    $ sage -pip install sage-numerical-backends-coin

or from GitHub using

    $ sage -pip install git+https://github.com/sagemath/sage-numerical-backends-coin

(See [`.github/workflows/build.yml`](.github/workflows/build.yml) for details about package prerequisites on various systems.)

## Using this package

After a successful installation, Sage will automatically make this new backend
the default MIP solver.

To select the `'Coin'` solver explicitly as the default MIP backend, additionally use the following command.

    sage: default_mip_solver('Coin')

To make these settings permanent, add this command to your `~/.sage/init.sage` file.
Note that this setting will not affect doctesting (`sage -t`) because this file is ignored in doctesting mode.

## Running doctests

To run the (limited) testsuite of this package, use:

    $ sage setup.py test

To run the Sage testsuite with the default MIP solver set to the backend provided by this package, use:

    $ sage setup.py check_sage_testsuite

## Running tests with tox

The doctests can also be invoked using `tox`:

    $ tox -e local
    $ tox -e local-sage_testsuite

If you have `docker` installed, more tests can be run:

    $ tox -e docker-sage_binary-cbc_coinbrew

See `tox.ini` for the available options.
