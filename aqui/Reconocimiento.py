import webbrowser #libreria abrir web
import speech_recognition as sr    #libreria para reconocer
import pyttsx3 
import principal

inicializar = pyttsx3.init()
r= sr.Recognizer()
velocidad = 130  # voz lenta
#inicializar.setProperty('rate', velocidad)
nombre = "ancorvis"  # nombre del bot

def reconocimientovoz():
    with sr.Microphone() as source:
        print("Escuchando.......")
        #print("Lee lo Siguiente:   Los versos que se cantan en la bamba son de una temática muy amplia: se canta a las mujeres, las relaciones sentimentales en general y a situaciones graciosas que suceden en la vida del pueblo jarocho (natural de Veracruz). Aunque existen frases que aparecen en casi todas las versiones, la propia estructura del tema invita a introducir variantes personales e inclusive versos improvisados espontáneamente.")
        audio= r.listen(source)
       
        try:
           #text= r.recognize_google(audio) #convierte a texto lo que decimos en ingles
            text = r.recognize_google(audio,language='es-MX') #ckee el audio lo compara con la voz en español y lo convierte a texto
            print('has dicho: {}'.format(text)) #lo imprime y guarda pa comparar
            print("Has dicho: "+text)
       
            """depende  de lo que diga abre una direccion
            if "Bamba" in text:
                webbrowser.open('https://inteligencia-artificial.dev/formacion/')
            if "Noticias" in text:
                webbrowser.open('https://inteligencia-artificial.dev/formacion/')"""
            
            
#si no reconoce nada de nada imprime este mensaje
        except:
            print('No entendi we')