import random

def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the computer go to the doctor? Because it had a virus!",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why was the math book sad? Because it had too many problems.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ]
    return random.choice(jokes)

def chatbot():
    print("Hello! I'm your friendly joke bot 🤖. Ask me to tell you a joke or type 'exit' to quit.")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "exit":
            print("Chatbot: Bye! Hope you laughed today! 😄")
            break
        elif "joke" in user_input:
            print("Chatbot:", tell_joke())
        else:
            print("Chatbot: Sorry, I can only tell jokes right now. Just ask me for a joke!")

if __name__ == "__main__":
    chatbot()
