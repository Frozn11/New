from speech import speech
from random import choice


levels = {
    "easy": ["dairy", "mouse", "computer"],
    "medium": ["programming", "algorithm", "developer"],
    "hard": ["neural network", "machine learning", "artificial intelligence"]
}

def play_game(level):
    words = levels.get(level, [])
    if not words:
        print("нет")
        return
    
    score = 0
    num_attempts = 3

    for _ in range(len(words)):
        random_word = choice(words)
        print(f"say this word {random_word}")
        recog_word = speech()
        print(recog_word)

        if random_word == recog_word:
            print("correct")
            score += 1
        else:
            print(f"rong the word is {random_word}")



    print(f"the game end your score: {score}/{len(words)}")

selected_level = input("какой сложность? (easy/medium/hard): ").lower()
play_game(selected_level)