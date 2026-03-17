<<<<<<< HEAD
print("Hello, World!")
print("Hello, World!")
print("Hello 16/3 2026, World!")
=======
from flask import Flask
>>>>>>> e9cd99c89c6fba06260916a492f74b01fdb8988b

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1><p>This is running inside a Docker Container!</p>'

if __name__ == '__main__':
    # We host it on 0.0.0.0 so it's accessible outside the container
    app.run(host='0.0.0.0', port=5000)