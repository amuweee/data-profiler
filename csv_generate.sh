#!/bin/bash

path=$(pwd)
fname=$1

cd ~/git-repos/data-profiler
source .venv/bin/activate

python3 -i csv_profiler.py $path $fname

deactivate


