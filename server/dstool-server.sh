function dstool-server-help(){
cat <<EOF
dstool-server is used to start and stop background Flask apps.

Install
---
(pyenv)$ pip3 install -r requirements.txt

Run
---
# nohup - don't kill children of closing shell
# python3 - mediated by pyenv (virtualenv)
# app.py - the application, serves PWD on PORT
# 2>&1  - redirct stderr (2) to stdout (1)
# > log.txt - write stdout to file

nohup python3 app.py > log.txt 2>&1 &

Notes
---
https://flask-executor.readthedocs.io/en/latest/
https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application
EOF
}

dstool-jupyter-start(){
   cd ~/src/ds-study-group/jupyter/
   jupyter-lab 
}
dstool-server-start-nohup(){
  nohup python3 app.py > log.txt 2>&1 &
}

dstool-server-list(){
 ps -ef | grep app.py | grep -v grep
}

dstool-server-kill(){
  echo 'use "kill PID" where PID is left-most column of dstool-server-list'
}
