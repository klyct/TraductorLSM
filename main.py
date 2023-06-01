import speech_recognition as sr
import tkinter as tk
import re
import contractions
import stanza
import cv2
from PIL import Image, ImageTk

# Variable global para almacenar el texto reconocido
recognized_text = ""

def start_recording():
    global recognized_text

    r = sr.Recognizer()

    # Uso de micrófono
    with sr.Microphone(device_index=1) as source2:
        # Obtención de audio
        print("Recording")

        # Actualizar el ícono del micrófono a rojo
        microphone_image = Image.open("microphone_red.png")
        microphone_image = microphone_image.resize((30, 30), Image.ANTIALIAS)
        microphone_icon = ImageTk.PhotoImage(microphone_image)
        microphone_label.config(image=microphone_icon)
        microphone_label.image = microphone_icon

        # Forzar la actualización de la interfaz gráfica
        root.update()

        # Apagar el micrófono 2s después de un silencio, en ruido ambiental
        r.adjust_for_ambient_noise(source2, duration=0.2)
        audio2 = r.listen(source2)
        print("Done")

        # Actualizar el ícono del micrófono a gris
        microphone_image = Image.open("microphone_gray.png")
        microphone_image = microphone_image.resize((30, 30), Image.ANTIALIAS)
        microphone_icon = ImageTk.PhotoImage(microphone_image)
        microphone_label.config(image=microphone_icon)
        microphone_label.image = microphone_icon

        # Conversión voz -> texto
        recognized_text = r.recognize_google(audio2, language='es-MX')
        recognized_text = recognized_text.lower()  # En minúsculas

        # Mostrar en consola
        print("Texto reconocido:\n" + recognized_text)

        translate_button.config(state=tk.NORMAL)

def translate_text():
    global recognized_text

    if recognized_text:
        # Realizar las operaciones adicionales con el texto reconocido
        def remove_between_square_brackets(text):
            # Elimina los caracteres entre corchetes
            return re.sub('\[[^]]*\]', '', text)

        def replace_contractions(text):
            # Reemplaza las contracciones por la versión extendida de las palabras
            return contractions.fix(text)

        def denoise_text(text):
            text = remove_between_square_brackets(text)
            text = replace_contractions(text)
            return text

        MyText = denoise_text(recognized_text)
        print("Denoise:\n" + MyText)

        # stanza.download("es")
        ## Definimos el idioma----------#Definimos los procesos que se estarán utilizando
        nlp = stanza.Pipeline(lang='es', processors='tokenize,mwt,pos,lemma,depparse')
        # se maneja en formato de documento por lo tanto mandamos nuestra muestra
        doc = nlp(MyText)

        ## Obtenemos las palabras lematizadas
        palabras = [f'{word.lemma}' for sent in doc.sentences for word in sent.words]
        print(palabras)

        for nom in palabras:
            nomVideo = lsm[nom]  ## Envío de palabras mediante lista
            print(nomVideo)  ## Control
            video = cv2.VideoCapture(nomVideo)  ## Obtener video del diccionario

            # Definir el tamaño de la ventana de video
            cv2.namedWindow('video', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('video', 640, 480)

            while video.isOpened():  ## Reproducción del video
                ret, imagen = video.read()
                if ret == False:  ## No hay más cuadros
                    break
                cv2.imshow('video', imagen)  ## Reproduce el video a
                if cv2.waitKey(30) == ord('s'):  ## 30 fps  con 's' como tecla de escape
                    break
        cv2.destroyAllWindows()
    else:
        print("No se ha realizado ninguna grabación previa.")

# Creamos el diccionario
lsm = {
    "abeja": 'abeja.mp4',
    "abandono": 'abandonar.mp4',
    "abandonar": 'abandonar.mp4',
    "abandonado": 'abandonar.mp4',
    "abogado": 'abogado.mp4',
    'abrazo': 'abrazo.mp4',
    'abreviatura': 'abreviatura.mp4',
    "abril": 'abril.mp4',
    'absorber': 'absorber.mp4',
    'abstener': 'abstener.mp4',
    'abstenerse': 'abstenerse.mp4',
    'absurdo': 'absurdo.mp4',
    'abuela': 'abuela.mp4',
    'abuelo': 'abuelo.mp4',
    'acabar': 'acabar.mp4',
    'aceite': 'aceite.mp4',
    'acelera': 'acelera.mp4',
    'acerca': 'acerca.mp4',
    'aclaracion': 'aclaracion.mp4',
    'aclarar': 'aclarar.mp4',
    'acordar': 'acordar.mp4',
    'acostumbrar': 'acostumbrar.mp4',
    'actividad': 'actividad.mp4',
    'actor': 'actor.mp4',
    'actual': 'actual.mp4',
    'acuerdo': 'acuerdo.mp4',
    'ahora': 'ahora.mp4',
    'artista': 'artista.mp4',
    'claramente': 'claramente.mp4',
    'claro': 'claro.mp4',
    'costumbre': 'costumbre.mp4',
    'obviamente': 'obviamente.mp4',
    'obvio': 'obvio.mp4',
    'presente': 'presente.mp4',
    'ridiculo': 'ridiculo.mp4',
    'sobre': 'sobre.mp4',
    'terminar': 'terminar.mp4',
    'auto': 'auto.mp4',
    'automóvil': 'automóvil.mp4',
    'coche': 'coche.mp4',
    'comer': 'comer.mp4',
    'comida': 'comida.mp4',
    'reclamar': 'reclamar.mp4',
    'reprochar': 'reprochar.mp4',
    'vehículo': 'vehículo.mp4',
    'viento': 'viento.mp4',
}

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Traductor a LSM")
root.geometry("620x480")
root.configure(bg="#F0F0F0")  # Cambiar el color de fondo

# Etiqueta de título
title_label = tk.Label(root, text="Para hacer la traducción de tu voz a LSM, primero presiona 'Iniciar grabación' y una vez tengas la grabación, presiona 'Traducir'", font=("Arial", 18), wraplength=500)
title_label.pack(pady=10)

# Cargar el ícono del micrófono
microphone_image = Image.open("microphone_gray.png")
microphone_image = microphone_image.resize((30, 30), Image.ANTIALIAS)
microphone_icon = ImageTk.PhotoImage(microphone_image)

# Etiqueta del ícono del micrófono
microphone_label = tk.Label(root, image=microphone_icon, bg="#F0F0F0")
microphone_label.pack(pady=10)

# Botón de inicio de grabación
record_button = tk.Button(root, text="Iniciar grabación", font=("Arial", 14), command=start_recording)
record_button.pack(pady=10)  # Agregar espaciado vertical

# Botón de traducción
translate_button = tk.Button(root, text="Traducir", font=("Arial", 14), command=translate_text, state=tk.DISABLED)
translate_button.pack(pady=10)  # Agregar espaciado vertical

# Ejecutar la aplicación
root.mainloop()