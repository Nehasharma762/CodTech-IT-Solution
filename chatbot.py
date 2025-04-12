import nltk
from nltk.chat.util import Chat, reflections

# Download required NLTK data (for tokenizing and processing)
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    (r'hi|hello|hey', ['Hello! How can I help you today?', 'Hi there! How can I assist you?']),
    (r'what is your name?', ['I am a simple chatbot.', 'You can call me Chatbot!']),
    (r'how are you?', ['I am just a bot, but I am doing fine. How about you?', 'I am good, thanks for asking!']),
    (r'(.*) your favorite (.*)', ['My favorite thing is to help you!', 'I love assisting people with their questions.']),
    (r'quit', ['Goodbye! Have a nice day!', 'It was nice chatting with you. Goodbye!']),
    (r'(.*)', ['Sorry, I don\'t understand that. Can you ask something else?'])  # Default response for unknown input
]

# Create a chatbot with the defined patterns and responses
chatbot = Chat(pairs, reflections)

# Start the conversation with the chatbot
def chat():
    print("Hi! I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Bot:", response)

# Start chatting
chat()
