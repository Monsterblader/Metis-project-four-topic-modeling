from flask import Flask, request, render_template
from flask.helpers import send_from_directory

app = Flask(__name__)

@app.route('/')  # the site to route to, index/main in this case
def hello_world():
    return send_from_directory('.', 'index.html')

@app.route('/favicon.ico')  # the site to route to, index/main in this case
def send_favicon():
    return send_from_directory('./', 'favicon.ico')

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('images', path)

@app.route('/pages/<path:path>')
def send_pages(path):
    return send_from_directory('pages', path)

@app.route('/pages/topic-model/<path:path>')
def get_topic(path):
    return send_from_directory("pages/topic-model", path)

@app.route('/pages/topic-model/graphs/<path:path>')
def get_graph(path):
    return send_from_directory('pages/topic-model/graphs', path)

# This just gets flask running
app.run(port=5000, debug=True)
