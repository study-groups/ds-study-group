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

def htmlHistogram(props):
     html='''
<div style="border:1px blue solid;">
<canvas id="histogramCanvasId"></canvas>
</div>
'''
     return html



@app.route("/ajax")
def ajax():
  return "Agax route hit"

@app.route("/")
def hello():
    htmlA=htmlHistogram([])
    return '''
<h1>Box Cox power transformation</h1>
<div id='controls' class="controls">
<button onClick="reload();">reload</button>
<button onClick="loadA();">loadA</button>
</div>
<div id="a" class="histogram"  style="border:1px blue solid;">
<canvas id="histogramCanvasId"></canvas>
</div>
<script>
let state ={};

function loadA(){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     var j = JSON.parse(this.responseText);
     console.log(`Got ${j}`);
     document.getElementById("a").innerHTML = j;
    }
  };
  xhttp.open("GET", "/a/json", true);
  xhttp.send();
}
function reload(){
    var evt = document.createEvent('Event');  
    evt.initEvent('load', false, false);  
    window.dispatchEvent(evt);
}

window.addEventListener('load', (function() {
    const pallet = [ "rgb(255,255,0)",
                     "rgb(255,128,0)",
                     "rgb(255,0,0)",
                     "rgb(128,255,0)",
                     "rgb(128,128,0)",
                     "rgb(128,0,0)",
                     "rgb(0,255,0)",
                     "rgb(0,128,0)",
                     "rgb(0,0,0)"];

    let palletIndex = 0;
    return function() {
             const canvas = document.getElementById('histogramCanvasId');
             const ctx = canvas.getContext('2d');
             ctx.fillStyle = pallet[palletIndex];
             palletIndex= (palletIndex+1) % pallet.length;
             ctx.fillRect(10,20,30,40);
             state.a={mean:0,std:1};
             console.log(`event:load: palletIndex=${palletIndex}`);
        };
})() );
</script>
'''

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

