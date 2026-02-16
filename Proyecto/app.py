from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello, World! Tarea de Desarrollo de Aplicaciones Web Semana 9'

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f'Bienvenido, {nombre}!'

@app.route('/producto/<nombre>')
def producto(nombre):
    return f"Producto: {nombre} – disponible."

@app.route('/contactos')
def contactos():
    return 'Puedes contactar a traves de nuestro correo electronico: geovannygrefa86@gmail.com'

if __name__ == '__main__':
    app.run(debug=True)

