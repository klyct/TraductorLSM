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
        microphone_image = microphone_image.resize((30, 30),  Image.LANCZOS)
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
        microphone_image = microphone_image.resize((30, 30),  Image.LANCZOS)
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
    'aclaración': 'aclaracion.mp4',
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
    'presente': 'presente.mp4',
    'ridículo': 'ridiculo.mp4',
    'sobre': 'sobre.mp4',
    'terminar': 'terminar.mp4',
    'auto': 'auto.mp4',
    'automóvil': 'automóvil.mp4',
    'coche': 'coche.mp4',
    'reclamar': 'reclamar.mp4',
    'reprochar': 'reprochar.mp4',
    'vehículo': 'vehículo.mp4',
'baño': 'baño.mp4',
"barco": 'barco.mp4',
"bebé": 'bebe.mp4',
"beber": 'beber.mp4',
"besar": 'besar.mp4',
"biblioteca": 'biblioteca.mp4',
"bicicleta": 'bicicleta.mp4',
"blanco": 'blanco.mp4',
"bombero": 'bombero.mp4',
"botella": 'botell.mp4',
"brincar": 'brincar.mp4',
"buscar": 'buscar.mp4',
"café": 'cafe.mp4',
"caliente": 'caliente.mp4',
"calle": 'calle.mp4',
"caminar": '.mp4',
"camión": '.mp4',
"cancelar": '.mp4',
"cantar": '.mp4',
"cara": '.mp4',
"carne": '.mp4',
"carta": '.mp4',
"casa": '.mp4',
"castigo": '.mp4',
"celoso": '.mp4',
"cena": '.mp4',
"cerca": '.mp4',
"círculo": '.mp4',
"ciudad": '.mp4',
"cocinar": '.mp4',
"comer": '.mp4',
"comida": '.mp4',
"compañero": '.mp4',
"compartir": '.mp4',
"computadora": '.mp4',
"confiar": '.mp4',
"contento": '.mp4',
"coquetear": '.mp4',
"corazón": '.mp4',
"correo": '.mp4',
"cuadrado": '.mp4',
"cuerpo": '.mp4',
"derecha": '.mp4',
"desayunar": 'desayunar.mp4',
"descansar": 'descansar.mp4',
"descargar": 'descargar.mp4',
"despertar": 'despertar.mp4',
"difícil": 'dificil.mp4',
"dinero": 'dinero.mp4',
"dolor": 'dolor.mp4',
"domingo": 'domingo.mp4',
"edad": 'edad.mp4',
"edificio": 'edificio.mp4',
"ella": 'ella.mp4',
"el": 'ella.mp4',
"enojar": 'enojar.mp4',
"escalera": 'escalera.mp4',
"escribir": 'escribir.mp4',
"escuela": 'escuela.mp4',
"estudio": 'estudio.mp4',
"energía": 'energia.mp4',
"equipo": 'equipo.mp4',
"falso": 'falso.mp4',
"fácil": 'facil.mp4',
"familia": 'familia.mp4',
"febrero": 'febrero.mp4',
"forma": 'forma.mp4',
"fruta": 'fruta.mp4',
"fuego": 'fuego.mp4',
"futuro": 'futuro.mp4',
"gasolina": 'gasolina.mp4',
"gato": 'gato.mp4',
"gente": 'gente.mp4',
"gracias": 'gracias.mp4',
"grande": 'grande.mp4',
"grosero": 'grosero.mp4',
"grave": 'grave.mp4',
"hacer": 'hacer.mp4',
    "ser":'ser.mp4',
"él":'ser.mp4',
"se":'ser.mp4',
"hambre": 'hambre.mp4',
"hermana": 'hermana.mp4',
"hermano": 'hermano.mp4',
"hijo": 'hijo.mp4',
"historia": 'historia.mp4',
"hombre": 'hombre.mp4',
"hora": 'hora.mp4',
"hospital": 'hospital.mp4',
"hoy": 'hoy.mp4',
"igual": 'igual.mp4',
"increíble": 'increible.mp4',
"intentar": 'intentar.mp4',
"internet": 'internet.mp4',
"izquierda": 'izquierda.mp4',
"irse": 'irse.mp4',
"interesante": 'interesante.mp4',
"joven": 'joven.mp4',
"jueves": 'jueves.mp4',
"jugar": 'jugar.mp4',
"julio": 'julio.mp4',
"junio": 'junio.mp4',
"jamás": 'jamas.mp4',
"jefe": 'jefe.mp4',
"laptop": 'laptop.mp4',
"lavar": 'lavar.mp4',
"leer": 'leer.mp4',
"lejos": 'lejos.mp4',
"lento": 'lento.mp4',
"libro": 'libro.mp4',
"líder": 'lider.mp4',
"limpiar": 'limpiar.mp4',
"llorar": 'llorar.mp4',
"lugar": 'lugar.mp4',
"lunes": 'lunes.mp4',
"maestro": 'maestro.mp4',
"malo": 'malo.mp4',
"mamá": 'mama.mp4',
"mañana": 'mañana.mp4',
"martes": 'martes.mp4',
"marzo": 'marzo.mp4',
"mayo": 'mayo.mp4',
"médico": 'medico.mp4',
"mentir": 'mentir.mp4',
"mesa": 'mesa.mp4',
"milagro": 'milagro.mp4',
"miercoles": 'miercoles.mp4',
"mío": 'mio.mp4',
    "mi": 'mio.mp4',
"mirar": 'mirar.mp4',
"mojar": 'mojar.mp4',
"mitad": 'mitad.mp4',
    "morir": 'morir.mp4',
"mucho": 'mucho.mp4',
"música": 'musica.mp4',
"nadie": 'nadie.mp4',
"necesitar": 'necesitar.mp4',
"negocio": 'negocio.mp4',
"negro": 'negro.mp4',
"niño": 'niño.mp4',
"no": 'no.mp4',
"nosotros": 'nosotros.mp4',
"noticias": 'noticias.mp4',
"novia": 'novia.mp4',
"novio": 'novio.mp4',
"nuevo": 'nuevo.mp4',
"número": 'numero.mp4',
"obvio": 'obvio.mp4',
"octubre": 'octubre.mp4',
"oficina": 'oficina.mp4',
"oportunidad": 'oportunidad.mp4',
"otro": 'otro.mp4',
"padre": 'padre.mp4',
"pajaro": 'pajaro.mp4',
"pan": 'pan.mp4',
"papá": 'papa.mp4',
"pequeño": 'pequeño.mp4',
"perdón": 'perdon.mp4',
"perro": 'perro.mp4',
"pesado": 'pesado.mp4',
"pie": 'pie.mp4',
"pierna": 'pierna.mp4',
"policía": 'policia.mp4',
"precio": 'precio.mp4',
"preguntar": 'preguntar.mp4',
"problema": 'problema.mp4',
"profesor": 'profesor.mp4',
"puerta": 'puerta.mp4',
"querer": 'querer.mp4',
"quejarse": 'quejarse.mp4',
"quiza": 'quiza.mp4',
"raro": 'raro.mp4',
"rapido": 'rapido.mp4',
"regalo": 'regalo.mp4',
"regresar": 'regresar.mp4',
"reír": 'reir.mp4',
"respuesta": 'respuesta.mp4',
"romper": 'romper.mp4',
"ruido": 'ruido.mp4',
"restaurante": 'restaurante.mp4',
"sábado": 'sabado.mp4',
"sed": 'sed.mp4',
"semana": 'semana.mp4',
"septiembre": 'septiembre.mp4',
"siempre": 'siempre.mp4',
"solo": 'solo.mp4',
"sólo": 'solo.mp4',
"subir": 'subir.mp4',
"sucio": 'sucio.mp4',
"suficiente": 'suficiente.mp4',
"también": 'tambien.mp4',
"tarde": 'tarde.mp4',
"tarea": 'tarea.mp4',
"tarjeta": 'tarjeta.mp4',
"televisión": 'television.mp4',
"tímido": 'timido.mp4',
"todo": 'todo.mp4',
"tomar": 'tomar.mp4',
"tío": 'tio.mp4',
"triste": 'triste.mp4',
"trabajar": 'trabajar.mp4',
"tú": 'tu.mp4',
"tu": 'tu.mp4',
"último": 'ultimo.mp4',
"ubicar": 'ubicar.mp4',
"ustedes": 'ustedes.mp4',
"vaso": 'vaso.mp4',
"ventana": 'ventana.mp4',
"verdad": 'verdad.mp4',
"verde": 'verde.mp4',
"vergüenza": 'verguenza.mp4',
"vida": 'vida.mp4',
"viejo": 'viejo.mp4',
"viento": 'viento.mp4',
"viernes": 'viernes.mp4',
"vivo": 'vivo.mp4',
"volver": 'volver.mp4',
"whatsapp": 'whatsapp.mp4',
"wifi": 'wifi.mp4',
"yo": 'yo.mp4',
"youtube": 'youtube.mp4'
}

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Traductor a LSM")
root.geometry("620x480")
root.configure(bg="#F0F0F0")  # Cambiar el color de fondo

# Etiqueta de título
title_label = tk.Label(root, text="Para hacer la traducción de tu voz a LSM, primero presiona "
                                  "'Iniciar grabación' y una vez tengas la grabación, presiona "
                                  "'Traducir'", font=("Arial", 18), wraplength=500)
title_label.pack(pady=10)

# Cargar el ícono del micrófono
microphone_image = Image.open("microphone_gray.png")
microphone_image = microphone_image.resize((30, 30),  Image.LANCZOS)
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