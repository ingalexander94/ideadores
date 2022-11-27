from flask import Flask, send_from_directory
from flask_cors import CORS
from utils import environment

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = environment.UPLOAD_FOLDER

# Routes
from routes.cens_router import cens_router

app.register_blueprint(cens_router, url_prefix='/api/cens')


CORS(app)

@app.route("/")
def ping():
    return "Todo ok!"

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name), 200
    
if __name__ == "__main__":
    app.run(debug=True, port=environment.PORT, host="0.0.0.0")