from flask import Flask

app = Flask(__name__)

@app.route('/')
def saludo():
    return '¡Hola, bienvenido a tu app Flask!'

if __name__ == '__main__':
    app.run(debug=True)
