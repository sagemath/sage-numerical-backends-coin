# sage-numerical-backends-coin: COIN-OR mixed integer linear programming backend for SageMath

[![PyPI](https://img.shields.io/pypi/v/sage-numerical-backends-coin)](https://pypi.org/project/sage-numerical-backends-coin/ "PyPI: sage-numerical-backends-coin")
[![GitHub Workflow Status](https://github.com/mkoeppe/sage-numerical-backends-coin/workflows/Build%20and%20test%20Python%20package/badge.svg)](https://github.com/mkoeppe/sage-numerical-backends-coin/actions "GitHub Actions: sage-numerical-backends-coin")

`CoinBackend` has previously been available as part of the [SageMath](http://www.sagemath.org/) source tree,
from which it is built as an "optional extension" when then `cbc` Sage package is installed.

However, it is not available in binary distributions such as:
- the Sage binary distribution (which does not package any optional packages),
- homebrew (which just uses the Sage binary distribution),
- Ubuntu (bionic 18.04LTS and several newer versions ship versions of SageMath, with various optional packages including CBC, but not the optional extension module CoinBackend),
- conda-forge (which ships SageMath and CBC but not the optional extension).
- Fedora

The present standalone Python package `sage-numerical-backends-coin` has been created from the SageMath sources, version 9.0.beta10.  It can be installed on top of various Sage installations using pip, including all of the above, including older versions of Sage such as 8.1 (as shipped by Ubuntu bionic 18.04LTS).

## Installation

CBC can either be installed using its Sage package using

    $ sage -i cbc

or any of the methods explained at https://github.com/coin-or/Cbc .

This package finds the CBC installation by means of ``pkgconfig``.

Install this package from PyPI using

    $ sage -python -m pip install sage-numerical-backends-coin

or from GitHub using

    $ sage -python -m pip install git+https://github.com/mkoeppe/sage-numerical-backends-coin

(See [`.github/workflows/build.yml`](.github/workflows/build.yml) for details about package prerequisites on various systems.)

## Using this package

To obtain a solver (backend) instance:

    sage: from sage_numerical_backends_coin.coin_backend import CoinBackend
    sage: CoinBackend()
    <sage_numerical_backends_coin.coin_backend.CoinBackend object at 0x7fb72c2c7528>

Equivalently:

    sage: from sage_numerical_backends_coin.coin_backend import CoinBackend
    sage: from sage.numerical.backends.generic_backend import get_solver
    sage: get_solver(solver=CoinBackend)
    <sage_numerical_backends_coin.coin_backend.CoinBackend object at 0x7fe21ffbe2b8>

To use this solver (backend) with [`MixedIntegerLinearProgram`](http://doc.sagemath.org/html/en/reference/numerical/sage/numerical/mip.html):

    sage: from sage_numerical_backends_coin.coin_backend import CoinBackend
    sage: M = MixedIntegerLinearProgram(solver=CoinBackend)
    sage: M.get_backend()
    <sage_numerical_backends_coin.coin_backend.CoinBackend object at 0x7fb72c2c7868>

