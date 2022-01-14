from flask import Flask
from flask import request
from flask import jsonify
from flask import send_file
from flask import render_template
from flask import send_from_directory
from pprint import pprint
import os
import sys
import markdown

app = Flask(__name__,  static_url_path='/_static')

#Optional
#from flask_autoindex import AutoIndex                                           #AutoIndex(app, browse_root='./write')  

def html(content):
   return '<html><head></head><body>' + content + '</body></html>'

@app.route("/")
def slash():
    return render_template("index.html")

@app.route("/notes")
def get_notes():
    #print(f"In get_notes() with request.headers:\n\n{request.headers}",
    #    flush=True)
    return send_file("./notes/ds-notes-2022-html_page001.svg") 

@app.route("/test/<path:file>")
def get_test(file):
    str=f'request.headers:<pre>{request.headers}</pre>'
    return html(str)

@app.route("/markdown")
def get_readme():
    readme_file = open("../README.md", "r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code"]
    )
    return md_template_string

@app.route('/pdb')
def pdb():
   """Enter python debugger in terminal"""
   print("\n'/pdb' endpoint hit. Dropping you into python debugger. globals:")
   print("%s\n" % dir(sys.modules[__name__]))
   import pdb; pdb.set_trace()
   return 'After PDB debugging session, now execution continues...'

@app.route("/json-hook", methods = ['POST', 'GET'])
def json_hook():
   out = os.popen("./json-hook").read()
   return out
 
@app.route("/json")
def get_json():
    return jsonify({"a":1,"b":2})

if __name__ == '__main__':
    portEnv=os.getenv("DS_PORT",9992)
    port=sys.argv[1]
    port = port if port else envPort 
    print(f'Using port: {port}')
    app.run(debug=1, host='0.0.0.0', port=port) 
