import random

class Quote:
    def __init__(self):
        self.quotes = [
            "The only way to do great work is to love what you do.",
            "Success is not final; failure is not fatal.",
            "It always seems impossible until it's done.",
            "Your time is limited, so don't waste it living someone else's life."
        ]

    def get_random_quote(self):
        return random.choice(self.quotes)

    def add_quote(self, new_quote):
        self.quotes.append(new_quote)
        
