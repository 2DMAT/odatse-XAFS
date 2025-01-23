#!/bin/sh

export PYTHONUNBUFFERED=1

odatse-FEFF input.toml

python3 gen_mockdata.py
