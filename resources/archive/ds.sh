DS_ENV=${DS_ENV:-"$HOME/ds-env"}
DS_SRC=${DS_SRC:-"$HOME/src/ds-study-group"}

echo "  Data Science Tools: DS_SRC=$DS_SRC"
echo "  Data Science Tools: DS_ENV=$DS_ENV"

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
source ds-dev/bin/activate
(ds-dev)$ 

Install notes
---
https://virtualenv.pypa.io/en/latest/user_guide.html
EOF
}

ds-activate(){
  source $DS_ENV/bin/activate
}

ds-install-bootstrap(){
  echo "This allows system python to install pyenv"
  sudo apt-get install python3-dev
  echo "Now run ds-install-env"
}

ds-install-env(){
  echo "Creating Python venv at DS_ENV=$DS_ENV return to continue"
  read
  echo "Creating virtual env at $DS_ENV"
  python3 -m venv "$DS_ENV"
  ds-activate
  echo "Now ds-install-requirements"
}

ds-install-requirements(){
  pip install -r $DS_SRC/requirements.txt
}

ds-install-jupyter-lab(){
  source $DS_ENV/bin/activate
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
   cd $DS_SRC/notebooks/
  jupyter-lab  .
}

