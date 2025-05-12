#!/bin/bash
DS_DIR=/home/devops/src/ds-study-group
DS_ENV=/home/devops/ds-env
source $DS_ENV/bin/activate
cd $DS_DIR/notebooks
jupyter-lab .
