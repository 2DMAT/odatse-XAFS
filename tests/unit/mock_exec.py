#!/usr/bin/env python3

import os
import shutil

base_dir = os.path.dirname(__file__)

cwd = os.getcwd()
subdir = cwd.split("/")[-1]
idx = int(subdir.split("_")[-1])

mock_file = os.path.join(base_dir, f"chi_{idx}.dat")
try:
    shutil.copy(mock_file, "chi.dat")
except FileNotFoundError as e:
    print(e)



    
