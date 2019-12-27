# sage-numerical-backends-coin: COIN-OR mixed integer linear programming backend for SageMath

CoinBackend has previously been available as part of the SageMath source tree,
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

To use this solver (backend) with `MixedIntegerLinearProgram`:

    sage: from sage_numerical_backends_coin.coin_backend import CoinBackend
    sage: M = MixedIntegerLinearProgram(solver=CoinBackend)
    sage: M.get_backend()
    <sage_numerical_backends_coin.coin_backend.CoinBackend object at 0x7fb72c2c7868>

Setting it as the default backend for `MixedIntegerLinearProgram`, as of SageMath 9.0.beta10, requires some trickery:

    sage: import sage_numerical_backends_coin.coin_backend as coin_backend, sage.numerical.backends as backends, sys
    sage: sys.modules['sage.numerical.backends.coin_backend'] = backends.coin_backend = coin_backend
    sage: default_mip_solver('Coin')

To patch this in permanently (at your own risk):

    $ sage -c 'import os, sysconfig, sage.env; f = "coin_backend" + sysconfig.get_config_var("EXT_SUFFIX"); d = os.path.join(sage.env.SAGE_LIB, "sage", "numerical", "backends", f); s = os.path.join("..", "..", "..", "sage_numerical_backends_coin", f); os.path.exists(d) and os.path.remove(d); os.symlink(s, d);'
