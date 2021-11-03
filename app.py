from flask import Flask, jsonify
from flask.helpers import send_from_directory
#from flask_cors import CORS

app = Flask(__name__, static_folder="../frontend/public", static_url_path="")

#CORS(app)

@app.route('/<string:name>',methods=['GET'])
def hello_world(name):  # put application's code here
    if name=='Ammar' or name=='ammar':
        return jsonify(
            status=200,
            message="Fatehi"
        )
    else:
        return jsonify(
            status=404,
            message="User Not Found"
        )

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0")