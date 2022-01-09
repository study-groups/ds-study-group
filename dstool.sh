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
