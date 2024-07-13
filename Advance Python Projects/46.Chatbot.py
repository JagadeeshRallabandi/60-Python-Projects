import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')  # Make sure NLTK data is downloaded

# Define patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created using NLTK.",]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!", "I'm fine, thank you! How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's okay, no problem.", "No worries.",]
    ],
    [
        r"I am fine",
        ["Great to hear that! How can I assist you today?",]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye! Have a nice day."]
    ],
]

reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# Create the Chatbot
def chatbot():
    print("Hi, I'm a chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
