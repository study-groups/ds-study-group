export DS_PORT=9992
function ds-server-help(){
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

nohup python3 app.py 9993 > log.txt 2>&1 &

Notes
---
https://flask-executor.readthedocs.io/en/latest/
https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application
EOF
}

# https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html
# nohup tells python to ignore SIGHUP (which shell sends when it exits)
# 2>&1  means redirect file descriptor 2 (stderr) to location of 1 (stdout)
# & at the end tells the shell to start in the background
function ds-server-start(){
  port=${1:-9992}
  appname="./ds-server.py"
  #mkfifo ./logs/$port.fifo 
  nohup python3 $appname $port > ./logs/$port.txt 2>&1 &
  ds_server_pid=$!
}

function ds-server-restart(){
  kill $ds_server_pid
  ds-server-start $DS_PORT
}

function ds-server-list(){
  ps -ef | grep "python3 ./ds-server.py" | grep -v grep # ignore the grep process 
}

function ds-server-kill(){
  echo 'assumes name starts with ds-server'
  ps -ef | grep ds-server | grep -v grep | awk '{print $2}' | xargs kill $1

}

                                                                                
function ds-server-activate(){                                                     source ds-dev/bin/activate                                             
} 
