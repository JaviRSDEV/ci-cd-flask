from flask import Flask, jsonify

PORT = 8000

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/welcome')
def welcome():
    return "Bienvenido Señor"

@app.route('/user/<name>')
def greet_user(name):
    return f"Hola {name}, bienvenido."

@app.route('/status')
def get_status():
    return jsonify({
        "status": "online",
        "version": "1.1.0",
        "port": PORT
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)