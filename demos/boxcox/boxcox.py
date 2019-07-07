from IPython.core import debugger
from flask import escape
from flask import json
#import json

debug = debugger.Pdb().set_trace
def buggy_method():
    debug()

from flask import Flask
import numpy as np
app = Flask(__name__)

def py2web(py):
    py_json = json.dumps(py.tolist())
    strtype= type(py)
    str = "<pre>"
    str += "py2web called with py:<br>"
    str += "type: {arg}\n".format(arg=escape(strtype))
    str += "shape: {shape})\n".format(shape=escape(py.shape))
    str += "{arg}".format(arg=py)
    str +="</pre>"
    return str;


@app.route("/")
def hello():
    return "<h1>Box Cox Demo</h1>"

@app.route("/a")
def displayA():
    a=np.random.rand(100,1)
    return py2web(a)

@app.route("/a/json")
def a_json():
    a=np.random.rand(100,1)
    response = app.response_class(
        response=json.dumps(a.tolist()),
        mimetype='application/json'
    )
    return response
    return json.dumps(a.tolist())


@app.route("/b")
def displayB():
    b = np.random.rand(1,100)
    return py2web(b) 

