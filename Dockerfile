# -*- Dockerfile -*- for testing
# docker build . -f Dockerfile-test
ARG BASE_IMAGE=mkoeppe/sage_binary-cbc_spkg:latest
FROM ${BASE_IMAGE}
ADD . /src
WORKDIR /src
RUN sage setup.py test && sage -python -m pip install .
RUN (sage setup.py check_sage_testsuite || echo "Ignoring failures")
RUN ./patch_and_check.sh
## Traceback (most recent call last):
##   File "/usr/local/opt/sage/sage-8.9/src/bin/sage-runtests", line 179, in <module>
##     err = DC.run()
##   File "/usr/local/opt/sage/sage-8.9/local/lib/python2.7/site-packages/sage/doctest/control.py", line 1206, in run
##     self.test_safe_directory()
##   File "/usr/local/opt/sage/sage-8.9/local/lib/python2.7/site-packages/sage/doctest/control.py", line 643, in test_safe_directory
##     .format(os.getcwd()))
## RuntimeError: refusing to run doctests from the current directory '/usr/local/opt/sage/sage-8.9/local/lib/python2.7/site-packages/sage' since untrusted users could put files in this directory, making it unsafe to run Sage code from
