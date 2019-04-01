import os

from flask import Flask
from flask import send_from_directory

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'public')
app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory(static_file_dir, 'index.html')

@app.route('/results')
def results():
    return send_from_directory(static_file_dir, 'results.html')

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')