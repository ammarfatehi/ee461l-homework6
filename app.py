from flask import Flask, jsonify
from flask.helpers import send_from_directory
#from flask_cors import CORS

app = Flask(__name__, static_folder="frontend/build", static_url_path="")


@app.route('/<string:name>',methods=['GET'])
def hello_world(name): 
    if name=='Ammar' or name=='ammar':
        return jsonify(
            status=200,
            payload="Fatehi"
        )
    else:
        return jsonify(
            status=404,
            payload="User Not Found"
        )

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0")