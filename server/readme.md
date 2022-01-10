# data science server

`ds-server` is a a collection of shell functions that provides
procedures for running a background Flask App in a Linux 
environment. To use, `source ds-server.sh` which will 
define functions starting with `ds-server` 
in your current shell.

Type `ds-server-` followed by `<tab>` to see options.

Type `ds-server-install` to install virtualenv

Type `ds-server-start` to start serving current directory
via routes defined by app.py

Note that app.py defaults to listening on port 9992 on the 
current insecure server, e.g. http://study-groups.org:9992.

To for a proper HTTPS, use Ngnix to listen on 443 and to 
reslove the TLS handshake and then configure Nginx to 
proxy the GET/POST requests to localhost:9992.


## Dev notes

### To create directory indexes
```python
# To create directory indexes:
#
from flask_autoindex import AutoIndex                                           
app = Flask(__name__,  static_url_path='/static')                               
AutoIndex(app, browse_root='./static')  
```

### Using pdb

- https://realpython.com/python-debugging-pdb/
