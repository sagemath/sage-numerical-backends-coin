# sage-numerical-backends-coin: COIN-OR mixed integer linear programming backend for SageMath

[![PyPI](https://img.shields.io/pypi/v/sage-numerical-backends-coin)](https://pypi.org/project/sage-numerical-backends-coin/ "PyPI: sage-numerical-backends-coin")
[![GitHub Workflow Status](https://github.com/mkoeppe/sage-numerical-backends-coin/workflows/Build%20and%20test%20Python%20package/badge.svg)](https://github.com/mkoeppe/sage-numerical-backends-coin/actions "GitHub Actions: sage-numerical-backends-coin")

CoinBackend has previously been available as part of the [SageMath](http://www.sagemath.org/) source tree,
from which it is built as an "optional extension" when then cbc Sage package is installed.

However, it is not available in binary distributions such as:
- the Sage binary distribution (which does not package any optional packages),
- Ubuntu (bionic 18.04LTS ships SageMath 8.1, with various optional packages including CBC, but not the optional extension module CoinBackend),
- conda-forge (which ships SageMath and CBC but not the optional extension).

The present standalone Python package `sage-numerical-backends-coin` has been created from the SageMath sources, version 9.0.beta10.  It can be installed on top of various Sage installations using pip, including older versions of Sage such as 8.1 (as shipped by Ubuntu bionic).

## Installation

CBC can either be installed using its Sage package using

    $ sage -i cbc

or any of the methods explained at https://github.com/coin-or/Cbc .

This package finds the CBC installation by means of ``pkgconfig``.

Install this package from PyPI using

    $ sage -pip install sage-numerical-backends-coin

or from GitHub using

    $ sage -pip install git+https://github.com/mkoeppe/sage-numerical-backends-coin

Installation in Ubuntu bionic:

    $ SAGE_LOCAL=/usr SAGE_ROOT=$(sage -root) pip install git+https://github.com/mkoeppe/sage-numerical-backends-coin

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

Setting it as the default backend for `MixedIntegerLinearProgram`, as of SageMath 9.0.beta10, requires some trickery:

    sage: import sage_numerical_backends_coin.coin_backend as coin_backend, sage.numerical.backends as backends, sys
    sage: sys.modules['sage.numerical.backends.coin_backend'] = backends.coin_backend = coin_backend
    sage: default_mip_solver('Coin')

To patch this in permanently (at your own risk):

    $ sage -c 'import os; import sage.numerical.backends as dm; import sage_numerical_backends_coin.coin_backend as sm; s = sm.__file__; f = os.path.basename(s); d = os.path.join(dm.__path__[0], f); (os.path.exists(d) or os.path.lexists(d)) and os.remove(d); os.symlink(s, d);'
