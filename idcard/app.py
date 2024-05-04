from flask import Flask, request, render_template
import cv2
import pytesseract
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'  # Asegúrate de que este directorio exista

def detectar_numero_identificacion(imagen_path):
    img = cv2.imread(imagen_path)
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, umbralizada = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    numero_identificacion = pytesseract.image_to_string(umbralizada)
    return numero_identificacion

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(save_path)
            numero_identificacion = detectar_numero_identificacion(save_path)
            return f'Número de identificación detectado: {numero_identificacion}'
    return '''
    <!doctype html>
    <title>OCR Web App</title>
    <h1>Subir imagen para reconocimiento OCR</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Procesar>
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)