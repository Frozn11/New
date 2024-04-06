import speech_recognition as sr 


def speech():

    mic = sr.Microphone()
    recog = sr.Recognizer()

    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
#        print('Говорите:')
        audio = recog.listen(audio_file)
        return recog.recognize_google(audio, language='ru-RU')


#print(speech())


