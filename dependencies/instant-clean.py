# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 11:11:52 2018

@author: ani228
"""

#!/usr/bin/env python
#
# This script cleans the Instant cache

__author__ = "Ilmar Wilbers (ilmarw@simula.no)"
__date__ = "2008-08-08 -- 2013-05-02"
__copyright__ = "Copyright (C) 2008 Ilmar Wilbers"
__license__  = "GNU GPL version 3 or any later version"

# Modified by Martin Alnes

import os, sys, shutil, glob, re
try:
    import instant
except:
    print("Instant not installed, exiting...")
    sys.exit(1)

instant_tmp_dir_suffix = instant.compute_checksum(instant.get_instant_dir())

# Check if any temp directories exists
tmp = instant.get_temp_dir()
tmp_dir_prefix = os.path.split(tmp)[0]
# FIXME: Is it safe to assume that the prefix to tempdirs is constant on a platform?
s = re.search(r"(.*)%s[^%s]*instant_%s" % (os.path.pathsep, os.path.pathsep, \
                                           instant_tmp_dir_suffix), tmp) 
instant.delete_temp_dir()
tmp_dirs = glob.glob(os.path.join(tmp_dir_prefix, '*instant_' + instant_tmp_dir_suffix))
for d in tmp_dirs:
    if os.path.isdir(d):
        print("Deleting temp directory", d)
        shutil.rmtree(d, ignore_errors=True)

# Get default cache dir (won't and can't touch userdefined cache dirs in this script)
cache_dir = instant.get_default_cache_dir()
error_dir = instant.get_default_error_dir()

# Check if directory exists (it always should after calling get_default_cache_dir)
assert os.path.isdir(cache_dir)
assert os.path.isdir(error_dir)

# Get list of cached forms
modules = os.listdir(cache_dir)
error_logs = os.listdir(error_dir)
if len(modules+error_logs) == 0:
    print("Instant cache is empty")
    sys.exit(0)

# Remove cached forms
lockfiles = [m for m in modules if     m.endswith(".lock")]
modules   = [m for m in modules if not m.endswith(".lock")]
error_lockfiles  = [f for f in error_logs if     f.endswith(".lock")]
error_logs       = [f for f in error_logs if not f.endswith(".lock")]
print("Removing %d modules from Instant cache..." % len(modules))
for module in modules:
    directory = os.path.join(cache_dir, module)
    shutil.rmtree(directory, ignore_errors=True)

print("Removing %d error logs from Instant cache..." % len(error_logs))
for error_log in error_logs:
    if os.path.isdir(os.path.join(error_dir, error_log)):
        shutil.rmtree(os.path.join(error_dir, error_log))
    else:
        os.remove(os.path.join(error_dir, error_log))

print("Removing %d lock files from Instant cache..." % len(lockfiles+error_lockfiles))
for lf in lockfiles:
    f = os.path.join(cache_dir, lf)
    os.remove(f)

for lf in error_lockfiles:
    f = os.path.join(error_dir, lf)
    os.remove(f)
