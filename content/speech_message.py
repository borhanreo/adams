import time

import pyttsx3
class SpeechMessage(object):
    def __init__(self):
        self.robot_name="adams"
        self.personal_description="I am robot"
    def init_speech(self):
        message = 'hi my name is '+self.robot_name
        self.spech_init(message,0,0.9)
        self.spech_init(" Thanks mister borhan for living me",0,0.9)
    def get_robot_name(self):
        return self.robot_name

    def spech(self,name):
        engine = pyttsx3.init()
        engine.say("Hello this is " + name)
        engine.setProperty('rate', 150)  # 120 words per minute
        engine.setProperty('volume', 0.9)
        engine.runAndWait()
        time.sleep(1)

    def spech_init(self,str, rate, volume):
        engine = pyttsx3.init()
        engine.say(str)
        engine.setProperty('rate', rate)  # 120 words per minute
        engine.setProperty('volume', volume)
        engine.runAndWait()
        time.sleep(1)