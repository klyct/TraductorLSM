import speech_recognition as sr ##speech recognition
import tkinter as tk
import re
import contractions
import stanza
import cv2 ##opencv-phyton
def start_recording():
    r = sr.Recognizer()

    # Uso de micrófono
    with sr.Microphone(device_index=1) as source2:
        # Obtención de audio
        print("Recording")
        # Apagar el micrófono 2s después de un silencio, en ruido ambiental
        r.adjust_for_ambient_noise(source2, duration=0.2)
        audio2 = r.listen(source2)
        print("Done")

        # Conversión voz -> texto
        MyText = r.recognize_google(audio2, language='es-MX')
        MyText = MyText.lower()  # En minúsculas

        # Mostrar en consola
        print("Texto reconocido:\n" + MyText)

        # Realizar las operaciones adicionales con el texto reconocido

        def remove_between_square_brackets(text):
            # Elimina los caracteres
            return re.sub('\[[^]]*\]', '', text)

        def replace_contractions(text):
            # Reemplaza las contracciones por la versión extendida de las palabras
            return contractions.fix(text)

        def denoise_text(text):
            text = remove_between_square_brackets(text)
            text = replace_contractions(text)
            return text

        MyText = denoise_text(MyText)
        print("Denoise:\n" + MyText)

        # stanza.download("es")
        ## Definimos el idioma----------#Definimos los procesos que se estarán utilizando
        nlp = stanza.Pipeline(lang='es', processors='tokenize,mwt,pos,lemma,depparse')
        # se maneja en formato de documento por lo tanto mandamos nuestra muestra
        doc = nlp(MyText)

        ## Obtenemos las palabras lematizadas
        palabras = [f'{word.lemma}' for sent in doc.sentences for word in sent.words]
        print(palabras)

        ## Creamos el diccionario
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

        for nom in palabras:
            nomVideo = lsm[nom]  ## Envío de palabras mediante lista
            print(nomVideo)  ## Control
            video = cv2.VideoCapture(nomVideo)  ## Obtener video del diccionario
            while video.isOpened():  ## Reproducción del video
                ret, imagen = video.read()
                if ret == False:  ## No hay más cuadros
                    break
                cv2.imshow('video', imagen)  ## Reproduce el video a
                if cv2.waitKey(30) == ord('s'):  ## 30 fps  con 's' como tecla de escape
                    break

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Grabación de Audio")
root.geometry("300x100")

# Botón de inicio de grabación
record_button = tk.Button(root, text="Iniciar grabación", command=start_recording)
record_button.pack()

# Ejecutar la aplicación
root.mainloop()