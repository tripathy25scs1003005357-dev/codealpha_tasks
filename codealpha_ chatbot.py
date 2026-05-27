def chatbot():
    print("ChatBot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("ChatBot: Hi! How can I help you?")

        elif user_input == "how are you":
            print("ChatBot: I'm fine, thanks for asking!")

        elif user_input == "what is your name":
            print("ChatBot: My name is CodeAlpha Bot.")

        elif user_input == "help":
            print("ChatBot: I can respond to greetings and simple questions.")

        elif user_input == "bye":
            print("ChatBot: Goodbye! Have a great day.")
            break

        else:
            print("ChatBot: Sorry, I don't understand that.")

# Run chatbot
chatbot()