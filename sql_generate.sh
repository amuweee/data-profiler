#!/bin/bash

path=$(pwd)
# query=$1

cd ~/git-repos/data-profiler
source .venv/bin/activate

python -i sql_profiler.py $path

deactivate


