

# Akhbaar padhke sunaao
# Import packages
import requests
import json
import pyttsx3



engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.



if __name__ == '__main__':
    # speak("News for today.. Lets begin")
    urls = [] #ADD URL HERE
    for url in urls:
        news = requests.get(url).text
        news_dict = json.loads(news)
        arts = news_dict['articles']
        for article in arts:
            speak(article['title'])
            speak("  ")
            speak(article['description'])
            print(article['title'])
            speak("Moving on to the next news..Listen Carefully")

    speak("Thanks for listening...")
