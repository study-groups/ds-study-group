DS_DIR=~/src/ds-study-group

source $DS_DIR/server/ds-server.sh

function ds-help(){
cat <<EOF
ds- is a collection of shell functions used to build 
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

ds-activate(){
  source $DS_DIR/ds-dev/bin/activate
}

ds-install(){
  sudo apt-get install python3-dev # needed for compiling
  ds-install-pyenv
}

ds-install-pyenv(){
  DS_DIR=${DS_DIR:-"$PWD/ds-dev"}
  echo "Instaiing in $DS_DIR/ds-dev"
 # creates a Python3 virtualenv
  python3 -m venv $DS_DIR/ds-dev
}

ds-install-jupyter-lab(){
  source $DS_DIR/ds-dev/bin/activate
  pip install jupyterlab 
}


ds-install-python-packages(){
  false && ( 
    wget https://github.com/ydataai/pandas-profiling/archive/master.zip
    unzip master
    cd pandas_profiling
    python setup.py install )

}

ds-install-rjupyter(){
  jupyter="$(which jupyter-lab)"  # ENV var used in R
  cat <<EOF
    #Run inside of R
    IRkernel::installspec()  # register kernel in current R installation
EOF
}

ds-start-jupyterlab(){
   cd ~/src/ds-study-group/notebooks/
  jupyter-lab  .
}

