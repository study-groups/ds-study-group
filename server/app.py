from flask import Flask
from flask import request
from flask import jsonify
from flask import send_file
from flask import render_template
from flask import send_from_directory
from pprint import pprint
import os
import markdown

app = Flask(__name__,  static_url_path='/static')

#Optional
from flask_autoindex import AutoIndex                                           
AutoIndex(app, browse_root='./write')  

def html(content):
   return '<html><head></head><body>' + content + '</body></html>'

@app.route("/notes")
def get_notes():
    #return send_file("./write/ds-notes-2022-html_page001.svg") 
    print(f"In get_notes() with request.headers: {request.headers}", flush=True)
    return send_from_directory("./notes","ds-notes-2022-html_page001.svg") 

@app.route("/test/<path:file>")
def get_test(file):
    info=pprint(vars(request))
    str=f'request.headers:<pre>{request.headers}</pre>'
    str+=f'<br>info:<pre>{info}</pre>'
    return html(str)


@app.route("/docs")
def get_docs():
    return send_file('docs/_build/html/index.html')

@app.route("/readme")
def get_readme():
    readme_file = open("../README.md", "r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code"]
    )
    return md_template_string

@app.route('/pdb')
def pdb():
   """Enter python debugger in terminal"""
   import sys
   print("\n'/pdb' endpoint hit. Dropping you into python debugger. globals:")
   print("%s\n" % dir(sys.modules[__name__]))
   import pdb; pdb.set_trace()
   return 'After PDB debugging session, now execution continues...'

@app.route('/index')
def index():
        return render_template('index.html')

@app.route("/json")
def get_json():
    return jsonify(request.data)

if __name__ == '__main__':
    port=os.getenv("DS_PORT",9992)
    print(f'Using port: {port}')
    app.run(debug=0, host='0.0.0.0', port=port) 
