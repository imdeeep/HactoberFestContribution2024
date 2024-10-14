import random

quotes = [
    "The best way to predict the future is to invent it. - Alan Kay",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "Get busy living or get busy dying. - Stephen King",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "In the end, we will remember not the words of our enemies, but the silence of our friends. - Martin Luther King Jr.",
]

def get_random_quote():
    return random.choice(quotes)

if __name__ == "__main__":
    print(get_random_quote())
