from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1><p>This is running inside a Docker Container!</p>'

if __name__ == '__main__':
    # We host it on 0.0.0.0 so it's accessible outside the container
    app.run(host='0.0.0.0', port=5000)