import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I'm a chatbot created with Python.", "You can call me PyBot."]
    ],
    [
        r"how are you ?",
        ["I'm doing great, thank you!", "I'm good! What about you?"]
    ],
    [
        r"sorry (.*)",
        ["No problem", "It's okay", "Don't worry"]
    ],
    [
        r"i'm (.*) (good|fine|okay|ok)",
        ["That's great to hear!", "Nice!"]
    ],
    [
        r"(.*) your name ?",
        ["My name is PyBot.", "I'm a Python chatbot."]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye!"]
    ]
]

chatbot = Chat(pairs, reflections)

print("Hi! I'm a chatbot. Type 'quit' to exit.")
chatbot.converse()

