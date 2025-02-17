import streamlit as st
from nltk.chat.util import Chat, reflections

# Define the pairs of patterns and responses
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is thecleverprogrammer, but you can just call me robot and I'm a chatbot .",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*)created(.*)",
        ["prakash created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['hyderabad, India',]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Cricket",]
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        ["Virat Kohli"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['our customer service will reach you']
    ],
]

# Initialize the Chat Bot
chat = Chat(pairs, reflections)

# Streamlit app layout
st.title("Chat with The Clever Programmer")
st.subheader("Hi, I'm thecleverprogrammer and I like to chat!")
st.write("Please type in the input box below to start a conversation. Type 'quit' to end the conversation.")

# Initialize session state for storing chat history
if 'history' not in st.session_state:
    st.session_state.history = []

# Function to process user input
def get_chat_response(user_input):
    response = chat.respond(user_input)
    return response if response else "Sorry, I don't understand that."

# Get user input from Streamlit text box
user_input = st.text_input("You: ", "")

if user_input:
    # Get chatbot response and update chat history
    response = get_chat_response(user_input)
    st.session_state.history.append(f"You: {user_input}")
    st.session_state.history.append(f"Bot: {response}")

# Display chat history
for message in st.session_state.history:
    st.write(message)

