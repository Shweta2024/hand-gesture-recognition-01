# import multiprocessing
from log_maker import Console
console = Console()

console.logInfo("Importing Packages Start ...")
from flask import Flask, request, jsonify
from flask_cors import CORS
from app import recognizeHandGesture

import base64
console.logInfo("Importing Packages End ...")


console.logInfo("Flask App Loading Start ...")
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
console.logInfo("Flask App Loading End ...")



@app.route("/")
def hello():
    return "hello world"


@app.route("/res", methods = ['GET', 'POST'])
def getresponse():
    if(request.method=='POST'):
        # Receive base64 encoded image data from the frontend
        data = request.get_json()
        base64_image_data = data.get('image_data')

        if base64_image_data:
            image_data = base64.b64decode(base64_image_data)
            gesture = recognizeHandGesture(image_data)
            response_data = {"gesture": gesture}
            return jsonify(response_data)
        
        else:
            return jsonify({'success': 'false'})
    else:
        return "Action Not Supported"





if __name__ == "__main__":
    console.logInfo("Flask App is going to run ...")
    app.run(debug=True,port=8000)