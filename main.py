import speech_recognition as sr
import webbrowser 
import pyttsx3
import musicLibrary
import requests
import google.generativeai as genai



recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "962f51b32e4340158e556674422433a2"




def speak(text):

    engine.say(text)
    engine.runAndWait()
    
def aiProcess(command):
    genai.configure(api_key="AIzaSyCCiUC5VY9wGtSLyoacU844awZbQ24bmTs")
    model = genai.GenerativeModel("gemini-1.5-flash",
    system_instruction = "you are a helpful assistant name jarvis that respond in short answers not more than 50 words without using * ")
    response = model.generate_content(command)
    return response.text
    

    

def processCommand(c):
    if "open twitter" in c.lower():
        webbrowser.open("https://x.com/home")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open formulaone" in c.lower():
        webbrowser.open("https://www.formula1.com/")    
    elif "open codechef" in c.lower():
        webbrowser.open("https://www.codechef.com/users/mayanksingh_x1")
    elif "hello" in c.lower():
        speak("hi how are you?")
    # elif "thanks" in c.lower():
    #     speak("your welcome..")    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()

            articles = data.get('articles', [])

            for article in articles:
                speak(article['title'])
    else:
        output = aiProcess(command)
        print(output)
        speak(output)



if __name__ == "__main__":
    speak("initializing Jaarvis..")
    while True:
        r = sr.Recognizer()
        

        print("recoginizing..")
        try:
            with sr.Microphone() as source:
                print("listening..")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("yes")
                with sr.Microphone() as source:
                    print("Jarvis is active..")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))        
