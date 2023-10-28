#!/bin/bash
DS_DIR=/home/devops/src/ds-study-group
source $DS_DIR/ds.sh
ds-activate
cd $DS_DIR/notebooks
jupyter-lab .
