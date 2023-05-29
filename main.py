import speech_recognition as sr ##speech recognition
import re
import contractions
import stanza
import cv2 ##opencv-phyton

r = sr.Recognizer()

# uso de microfono
with sr.Microphone(device_index=1) as source2:
    # obtencion de audio
    print("recording")
    # apagar microfo 2s despues de un silencio, en ruido ambiental
    r.adjust_for_ambient_noise(source2, duration=0.2)
    audio2 = r.listen(source2)
    print("done")

    # conversion voz -> txt
    MyText = r.recognize_google(audio2, language='es-MX')
    MyText = MyText.lower() ## en minusculas

    # Mostrar en consola
    print("Texto reconocido: \n" + MyText)


def remove_between_square_brackets(text):
    # Elimina los caracteres
    return re.sub('\[[^]]*\]', '', text)


def replace_contractions(text):
    # Reemplaza las contracciones por a version
    # extendida de las palabras
    return contractions.fix(text)


def denoise_text(text):
    text = remove_between_square_brackets(text)
    text = replace_contractions(text)
    return text


MyText = denoise_text(MyText)
print("Denoise: \n" + MyText)

# stanza.download("es")
##definimos el idioma----------#Definimos los procesos que se estaran utilizando
nlp = stanza.Pipeline(lang='es', processors='tokenize,mwt,pos,lemma,depparse')
# se maneja en formato de documento por lo tanto mandamos nuestra muestra
doc = nlp(MyText)

# Mostramos el documento para ver lo que se obtiene
#print(doc, '\n')
#print(doc.entities, '\n')
##Para obtener de forma pas consisa lo que necesitamos podemos visualizarlo de este modo
#print(*[f'Palabra: {word.text + " "}\tLemma: {word.lemma}\tPOS: {word.pos}' for sent in doc.sentences for word in
      #  sent.words], sep='\n')


##Obtenemos las palabras lemmatizadas
palabras=[f'{word.lemma}' for sent in doc.sentences for word in sent.words]
print(palabras)

##Creamos el diccionario
lsm = {"abeja": 'abeja.mp4',
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
       'terminar': 'terminar.mp4',}

for nom in palabras:
    nomVideo = lsm[nom]                 ##envio de palabras mediante lista
    print(nomVideo)##control
    video = cv2.VideoCapture(nomVideo)  ##obtener video del diccionario
    while video.isOpened():             ##reproduccion del video
        ret, imagen = video.read()
        if ret == False:                ##no hay mas cuadros
            break
        cv2.imshow('video', imagen)     ##reproduce el video a
        if cv2.waitKey(30)== ord('s'):  ##30 fps  con 's' como tecla de escape
            break








