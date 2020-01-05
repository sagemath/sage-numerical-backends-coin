#! /bin/bash
# On Ubuntu bionic, the following fails:
#   sage patch_into_sage_module.py
#   sage -python patch_into_sage_module.py
# with ImportError: No module named coin_backend.
# Hence we workaround as follows.
sage patch_into_sage_module.py || exit 1
## sage -c 'load("patch_into_sage_module.py")' || exit 1
sage check_get_solver_with_name.py || exit 1
## sage -c 'load("check_get_solver_with_name.py")' || exit 1
