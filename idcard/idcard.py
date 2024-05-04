import cv2
import pytesseract

def detectar_numero_identificacion(imagen):
    # Leer la imagen
    img = cv2.imread(imagen)

    # Convertir la imagen a escala de grises
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Aplicar umbralización para convertir la imagen a blanco y negro
    _, umbralizada = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Aplicar OCR para reconocer el texto en la imagen
    numero_identificacion = pytesseract.image_to_string(umbralizada)

    return numero_identificacion

if __name__ == "__main__":
    # Ruta de la imagen de la tarjeta de identificación
    ruta_imagen = "discapacidad.jpg"

    # Detectar el número de identificación en la imagen
    numero_identificacion = detectar_numero_identificacion(ruta_imagen)

    # Mostrar el número de identificación detectado
    print("Número de identificación detectado:", numero_identificacion)
