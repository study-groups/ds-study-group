from flask import Flask,jsonify,request
from flask import render_template
#import ipdb;

app = Flask(__name__,  static_url_path='/public')
serverstate = {'status':'Waiting for stream'}
alldata = {'labels':[]}

@app.route("/")
def get_app():
        return render_template('app.html')

@app.route('/getState')
def get_state():
        global serverstate
        return jsonify(serverstate)

@app.route('/getData')
def get_data():
        global alldata
        return jsonify(alldata)

@app.route('/postData', methods=['POST'])
def post_data():
        #ipdb.set_trace()
        global alldata, serverstate
        if request.form:
            serverstate['status'] = 'Running'
        else:
            print('no data or no form')
            return "error",400
        batch = request.form.to_dict()
        print("Received: ", batch)
        #Update data with the latest batch
        serverstate['topics'] = [topic for topic in batch.keys()]
        for key in batch.keys():
            if key not in alldata.keys():
                alldata[key] = []
            alldata[key].append(batch[key])
        alldata['labels'].append('')
        return "success",201
if __name__ == "__main__":
        app.run(host='0.0.0.0', port=9991) 
