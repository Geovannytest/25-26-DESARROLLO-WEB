from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello, World! clase de programación  Tutoría Semana 9'
if __name__ == '__main__':
    app.run(debug=True)
