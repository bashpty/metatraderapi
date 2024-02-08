from flask import Flask, jsonify, render_template, request, jsonify
from flask_restful import Api
from dotenv import load_dotenv
import os
import sys
from flask_cors import CORS

from controllers.MtManagerController import MtManagerController

sys.path.append(os.path.split(os.getcwd())[0])

load_dotenv()

SWAGGER_URL = "/swagger"
API_URL = "/static/docs.json"
AUTH0_DOMAIN = os.getenv('AUTH0_DOMAIN')
API_IDENTIFIER = os.getenv('API_IDENTIFIER')
ALGORITHMS = os.getenv('ALGORITHMS')


# creating a Flask app
app = Flask(__name__)
api = Api(app)

api.add_resource(MtManagerController, "/manager")

CORS(app, resources={r"/*": {"origins": "*"}})
@app.route('/api/docs')
def get_docs():
    print('sending docs')
    return render_template('swaggerui.html')


@app.route('/', methods=['GET', 'POST'])
def home():
    if (request.method == 'GET'):

        data = "liveness Probe"
        return jsonify({'data': data})


# driver function
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=False)