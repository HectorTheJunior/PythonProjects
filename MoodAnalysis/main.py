from textblob import TextBlob
from dataclasses import dataclass


@dataclass
class Mood:
    emoji: str
    sentiment: float


def get_mood(input_text: str, *, sensitivity: float):

    polarity: float = TextBlob(input_text).sentiment.polarity

    friendly_threshold: float = sensitivity
    unfriendly_threshold: float = -sensitivity

    if polarity >= friendly_threshold:
        return Mood('😊', polarity)
    elif polarity <= unfriendly_threshold:
        return Mood("😒", polarity)
    else:
        return Mood("😐", polarity)


def run():
    print("Enter some text to get a sentiment analysis:")
    while True:
        user_input: str = input('You:')
        if user_input == 'exit':
            break
        else:
            mood: Mood = get_mood(user_input, sensitivity=0.2)
            print(f"Bot: {mood.emoji} ({mood.sentiment})")


run()
