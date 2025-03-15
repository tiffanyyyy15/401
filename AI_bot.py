responses = {
    "hello": "Hey there! How can I assist you today?",
    "hi": "Hello! What would you like to talk about?",
    "how are you?": "I'm just a bunch of code, but thanks for asking! How about you?",
    "what is ai?": "AI stands for Artificial Intelligence, which is the simulation of human intelligence in machines.",
    "who is gilo?": "Gilo is a curious learner passionate about technology and programming.",
    "what is java?": "Java is a powerful programming language used for building various applications, from web to mobile.",
    "who created java?": "Java was created by James Gosling and released by Sun Microsystems in 1995.",
    "thank you": "You're welcome! Feel free to ask me anything else.",
    "thanks": "Glad I could help! Let me know if you need more assistance."
}


def get_bot_response(user_input):
    return responses.get(user_input, "I don't understand. Can you say that again?")


def main():
    print("This is a mini AI Chat Bot!!")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("Bot: Thanks have a nice day. Bye!")
            break

        bot_response = get_bot_response(user_input)
        print("Bot: " + bot_response)


if __name__ == "__main__":
    main()
