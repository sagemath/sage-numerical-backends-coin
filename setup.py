#! /usr/bin/env python
## -*- encoding: utf-8 -*-

from __future__ import print_function

import os
import sys
from setuptools import setup
from setuptools import Extension
from setuptools.command.test import test as TestCommand # for tests
from Cython.Build import cythonize
from Cython.Compiler.Errors import CompileError
from codecs import open # To open the README file with proper encoding
from sage.env import sage_include_directories

# For the tests
class SageTest(TestCommand):
    def run_tests(self):
        # Passing optional=sage avoids using sage.misc.package.list_packages,
        # which gives an error on Debian unstable as of 2019-12-27:
        # FileNotFoundError: [Errno 2] No such file or directory: '/usr/share/sagemath/build/pkgs'
        errno = os.system("PYTHONPATH=`pwd` sage -t --force-lib --optional=sage sage_numerical_backends_coin")
        if errno != 0:
            sys.exit(1)

# Get information from separate files (README, VERSION)
def readfile(filename):
    with open(filename, encoding='utf-8') as f:
        return f.read()

 # Cython modules
import pkgconfig

try:
    cbc_pc = pkgconfig.parse('cbc')
except pkgconfig.PackageNotFoundError:    # exception handling from sage trac #28883 for pkgconfig version 1.5.1
    from collections import defaultdict
    cbc_pc = defaultdict(list, {'libraries': ['Cbc']})

if cbc_pc:
    print("Using pkgconfig: {}".format(sorted(cbc_pc.items())), file=sys.stderr)
cbc_libs = cbc_pc['libraries']
cbc_library_dirs = cbc_pc['library_dirs']
cbc_include_dirs = cbc_pc['include_dirs']


ext_modules = [Extension('sage.numerical.backends.coin_backend',
                         sources=[os.path.join('sage/numerical/backends',
                                    'coin_backend.pyx')],
                         libraries=cbc_libs,
                         include_dirs=sage_include_directories() + cbc_include_dirs,
                         library_dirs=cbc_library_dirs,
                         extra_compile_args=['-std=c++11'])
    ]


## SageMath 8.1 (included in Ubuntu bionic 18.04 LTS) does not have sage.cpython.string;
## it was introduced in 8.2.
compile_time_env = {'HAVE_SAGE_CPYTHON_STRING': False,
                    'HAVE_ADD_COL_UNTYPED_ARGS': False}

print("Checking whether HAVE_SAGE_CPYTHON_STRING...", file=sys.stderr)
try:
    import sage.cpython.string
    compile_time_env['HAVE_SAGE_CPYTHON_STRING'] = True
except ImportError:
    pass

## SageMath 8.7 changed the signature of add_col.
print("Checking whether HAVE_ADD_COL_UNTYPED_ARGS...", file=sys.stderr)
try:
    cythonize(Extension('check_add_col_untyped_args',
                        sources=['check_add_col_untyped_args.pyx'],
                        include_dirs=sage_include_directories()),
              quiet=True,
              include_path=sys.path)
    compile_time_env['HAVE_ADD_COL_UNTYPED_ARGS'] = True
except CompileError:
    pass

print("Using compile_time_env: {}".format(compile_time_env), file=sys.stderr)

setup(
    name="sage.numerical.backends.coin_backend",
    version=readfile("VERSION").strip(),
    description="COIN-OR backend for Sage MixedIntegerLinearProgram",
    long_description = readfile("README.md"), # get the long description from the README
    long_description_content_type='text/markdown', # https://packaging.python.org/guides/making-a-pypi-friendly-readme/
    url="https://github.com/mkoeppe/sage-numerical-backends-coin",
    # Author list obtained by running the following command on sage 9.0.beta9:
    # for f in coin_backend.p*; do git blame -w -M -C -C --line-porcelain "$f" | grep -I '^author '; done | sort -f | uniq -ic | sort -n
    # cut off at < 10 lines of attribution.
    author='Nathann Cohen, Yuan Zhou, John Perry, Zeyi Wang, Martin Albrecht, Jori Mäntysalo, Matthias Koeppe, Erik M. Bray, Jeroen Demeyer, Nils Bruin, Julien Puydt, Dima Pasechnik, and others',
    author_email='mkoeppe@math.ucdavis.edu',
    license='GPLv2+', # This should be consistent with the LICENCE file
    classifiers=['Development Status :: 5 - Production/Stable',
                 "Intended Audience :: Science/Research",
                 'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
                 "Programming Language :: Python",
                 "Programming Language :: Python :: 2",
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 ],
    ext_modules = cythonize(ext_modules, include_path=sys.path,
                            compile_time_env=compile_time_env),
    cmdclass = {'test': SageTest}, # adding a special setup command for tests
    keywords=['milp', 'linear-programming', 'optimization'],
    packages=['sage.numerical.backends'],
    package_data={'sage.numerical.backends': ['*.pxd']},
    install_requires = [# 'sage>=8',    ### On too many distributions, sage is actually not known as a pip package
                        'sphinx'],
    setup_requires   = ['pkgconfig'],

)
