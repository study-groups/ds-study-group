DS_DIR=~/src/ds-study-group

source $DS_DIR/server/dstool-server.sh

function dstool-help(){
cat <<EOF
dstool- is a collection of shell functions used to build 
data science pipelines on the commandline.

Requires
---
1. Linux system with Python 3.8+
2. virtualenv

Install
---
python3 -m venv ds-dev # creates a Python3 virtualenv

Run
---
$source ds-dev/bin/activate
(ds-dev)$ 

Install notes
---
https://virtualenv.pypa.io/en/latest/user_guide.html
EOF
}

function dstool-activate(){
  source server/ds-dev/bin/activate
}

dstool-activate(){
  source $DS_DIR/ds-dev/bin/activate
}

dstool-install-dev(){
  sudo apt-get install python3-dev # needed for compiling
  pip install rpy2 # probably don't need r inside of py
}

dstool-install-rjupyter(){
  jupyter="$(which jupyter-lab)"  # ENV var used in R
  cat <<EOF
Run inside of R
IRkernel::installspec()  # to register the kernel in the current R installation
EOF
}

dstool-start-jupyterlab(){
   cd ~/src/ds-study-group/notebooks/
  jupyter-lab 
}


