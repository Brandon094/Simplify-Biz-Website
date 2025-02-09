from flask import Flask, render_template, request
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

# Cargar las variables de entorno
load_dotenv()

app = Flask(__name__)

# Configuración de Flask-Mail usando variables de entorno
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

mail = Mail(app)

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/documentacion', methods=['GET'])
def documentacion():
    return render_template('documentacion.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    mensaje_confirmacion = None
    popup_visible = False  # Inicializar la variable para el popup

    if request.method == 'POST':
        # Obtener los datos del formulario
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        try:
            # Crear el mensaje de correo electrónico
            msg = Message("Nuevo mensaje desde el formulario de contacto de Simplify Biz site", recipients=['dazace94@gmail.com'])
            msg.body = f"Mensaje de {name} ({email}):\n\n{message}"

            # Enviar el correo electrónico
            mail.send(msg)

            # Si el correo fue enviado, muestra el mensaje de éxito
            mensaje_confirmacion = "¡Mensaje enviado con éxito! Gracias por contactarnos."
            popup_visible = True  # Mostrar el popup de confirmación
        except Exception as e:
            # Si ocurre un error al enviar el correo, muestra un mensaje de error
            mensaje_confirmacion = f"Hubo un problema al enviar tu mensaje. Intenta nuevamente. Error: {str(e)}"
            popup_visible = True  # Mostrar el popup de error

    return render_template('contact.html', mensaje_confirmacion=mensaje_confirmacion, popup_visible=popup_visible)


@app.route('/download', methods=['GET'])
def download():
    return render_template('download.html')

@app.route('/pago/<software>', methods=['GET', 'POST'])
def payment(software):
    mensaje_confirmacion = None
    codigo_validacion = None
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        monto = request.form['monto']
        
        # Aquí asignas el monto según el software
        if software == 'Windows':
            monto = 10
        elif software == 'macOS':
            monto = 8
        elif software == 'Linux':
            monto = 6
        
        try:
            # Crear mensaje de confirmación
            msg = Message("Confirmación de pago", recipients=[email])
            msg.body = f"Gracias {nombre}, tu pago de ${monto} ha sido recibido por la versión de {software}. ¡Puedes proceder con la descarga!"
            mail.send(msg)
            
            # Generar un código de validación (puedes mejorar esto generando uno único)
            codigo_validacion = 'ABCD1234'  # Genera o utiliza uno real aquí
            
            # Muestra el mensaje de éxito y redirige
            mensaje_confirmacion = f"¡Pago realizado con éxito! Se ha enviado un código de validación a tu correo."
            return redirect(url_for('validar_codigo', codigo=codigo_validacion))  # Pasa el código de validación a la página de validación
        except Exception as e:
            mensaje_confirmacion = f"Hubo un problema al procesar tu pago. Error: {str(e)}"
    
    return render_template('payment.html', software=software, mensaje_confirmacion=mensaje_confirmacion)

@app.route('/validar_codigo', methods=['GET', 'POST'])
def validar_codigo():
    mensaje_validacion = None
    codigo_validacion = request.args.get('codigo')  # Obtener el código desde la URL
    
    if request.method == 'POST':
        codigo_ingresado = request.form['codigo']
        
        # Verificar si el código es correcto
        if codigo_ingresado == codigo_validacion:
            mensaje_validacion = "Código validado con éxito. Ahora puedes descargar el software."
        else:
            mensaje_validacion = "Código no válido. Por favor, revisa tu correo y vuelve a intentarlo."
    
    return render_template('verificar_codigo.html', mensaje_validacion=mensaje_validacion)

if __name__ == "__main__":
    app.run(debug=True)
