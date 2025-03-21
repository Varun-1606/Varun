def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if 'hello' in user_input or 'hi' in user_input:
        return 'Hello! How can I assist you today?'
    
    # Asking about the chatbot
    elif 'who are you' in user_input or 'what are you' in user_input:
        return 'I am a simple chatbot designed to help you!'
    
    # Asking about time
    elif 'time' in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime('%H:%M:%S')
        return f'The current time is {current_time}.'

    # Asking for help
    elif 'help' in user_input:
        return 'Sure! I can assist you with general questions. Ask away!'
    
    # Farewell
    elif 'bye' in user_input or 'goodbye' in user_input:
        return 'Goodbye! Have a great day!'
    
    # Default response
    else:
        return "I am sorry, I didn't understand that. Can you please rephrase?"

# Chat loop
def chat():
    print("Chatbot: Hello! Type 'exit' to end the chat.")
    while True:
        user_input = input('You: ')
        if user_input.lower() == 'exit':
            print('Chatbot: Goodbye!')
            break
        response = chatbot_response(user_input)
        print(f'Chatbot: {response}')

if __name__ == "__main__":
    chat()
