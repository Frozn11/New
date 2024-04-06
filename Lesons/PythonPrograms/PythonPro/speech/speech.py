import speech_recognition as sr 
import random, time


easy = ["dairy", "mouse", "computer"]

medium = ["programming", "algorithm", "developer"]

hard = ["neural network", "machine learning", "artificial intelligence"]



def speech():
    mic = sr.Microphone()
    recog = sr.Recognizer()

    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        print('Говорите:')
        audio = recog.listen(audio_file)
        return recog.recognize_google(audio, language='en-EN')


def difficulty(difficultyWhat):

    match difficultyWhat:
        case "easy":
            wordis = random.choice(easy)
            return wordis
        case "medium":
            wordis = random.choice(medium)
            return wordis
        case "hard":
            wordis = random.choice(hard)
            return wordis
        
difficultyWhat = input("какой сложность? (easy/medium/hard)")    

print(difficulty(difficultyWhat))



def play_game():
    speechis = speech()
    wordis = difficulty(difficultyWhat)
    
    
    if wordis == speechis.lower():
        print("good")
        print(f"you say {speechis} word is {wordis}")
    else:
        print("not good")
        print(f"you say {speechis} word is {wordis}")
    

play_game()


