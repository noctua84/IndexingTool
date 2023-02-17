from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello there'


@app.route('/search', methods=['GET'])
def search_index():
    return 'do some searching'


@app.route('/ignored', methods=['GET, POST, DELETE'])
def ignored_documents():
    return 'ignoring things'


if __name__ == '__main__':
    app.run()
