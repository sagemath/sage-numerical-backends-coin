#! /bin/bash
sage -c 'load("patch_into_sage_module.py")' || exit 1
sage -c 'load("check_get_solver_with_name.py")' || exit 1
