from colorama import Fore, Style, init
import time

init(autoreset=True)

# ===========================
# Welcome Banner
# ===========================

print(Fore.CYAN + "╔══════════════════════════════════════════════════════╗")
print(Fore.CYAN + "║                  🤖 RULEBOT AI                      ║")
print(Fore.CYAN + "║             Rule-Based AI Chatbot                  ║")
print(Fore.CYAN + "╚══════════════════════════════════════════════════════╝")

print()
print(Fore.MAGENTA + "🧠 AI Type      : " + Fore.WHITE + "Rule-Based")
print(Fore.GREEN + "💻 Built With   : " + Fore.WHITE + "Python")
print(Fore.YELLOW + "👩‍💻 Created By  : " + Fore.WHITE + "Wajeeha")
print(Fore.CYAN + "📌 Version      : " + Fore.WHITE + "1.0")

print(Fore.CYAN + "\n" + "─" * 55)

print(Fore.YELLOW + "Initializing RuleBot...")
time.sleep(0.5)

print(Fore.YELLOW + "Loading Knowledge Base...")
time.sleep(0.5)

print(Fore.YELLOW + "Activating Rule Engine...")
time.sleep(0.5)

print(Fore.GREEN + "✓ RuleBot is online and ready to chat!")

print(Fore.CYAN + "─" * 55)

# ===========================
# Get User Name
# ===========================

name = input(Fore.BLUE + "\n👤 Please enter your name: ")

print(Fore.GREEN + f"\n🤖 Hello, {name}! Nice to meet you 😊")
# print(Fore.GREEN + "How can I help you today?")

print(Fore.CYAN + "─" * 55)

# ===========================
# Chatbot Loop
# ===========================

while True:

    user = input(Fore.BLUE + f"\n👤 {name}: ").lower().strip()

    # Greeting responses

    if user == "assalam u alaikum":
        print(Fore.GREEN + f"🤖 RuleBot: Wa Alaikum Assalam, {name}! How can I assist you today? 😊")

    elif user == "hi" or user == "hello" or user == "hey":
        print(Fore.GREEN + f"🤖 RuleBot: Hello {name}! How can I assist you today? 😊")

    elif user == "how are you":
        print(Fore.CYAN + "🤖 RuleBot: I am just a chatbot, but I'm functioning well! How about you? 😊")

    elif user == "what is your name":
        print(Fore.YELLOW + "🤖 RuleBot: I am RuleBot. I am a rule-based AI chatbot designed to assist you with your queries. 😊")

    elif user == "who created you":
        print(Fore.MAGENTA + "🤖 RuleBot: I was created by Wajeeha using Python as a Rule-Based AI Chatbot project. 😊")

    elif user == "what can you do":
        print(Fore.CYAN + "🤖 RuleBot: I can answer basic questions about AI, Python, greetings, and provide simple rule-based responses.")

    elif user == "who are you":
        print(Fore.YELLOW + "🤖 RuleBot: I am RuleBot, a simple Rule-Based chatbot built using Python. I can answer basic questions and have a friendly chat with you! 😊")

    # AI Related

    elif user == "what is ai":
        print(Fore.GREEN + "🤖 RuleBot: AI stands for Artificial Intelligence. It enables machines to perform tasks that normally require human intelligence.")

    elif user == "what is python":
        print(Fore.BLUE + "🤖 RuleBot: Python is a popular programming language used for AI, web development, automation, and data science.")

    # Help

    elif user == "help":
        print(Fore.CYAN + "🤖 RuleBot: You can ask me about AI, Python, greetings, or type 'bye' to exit.")

    # Thanks

    elif user == "thank you" or user == "thanks":
        print(Fore.GREEN + "🤖 RuleBot: You're welcome! Happy to help. 😊")

    # Greetings

    elif user == "good morning":
        print(Fore.YELLOW + f"🤖 RuleBot: Good Morning, {name}! Have a wonderful day! ☀️")

    elif user == "good afternoon":
        print(Fore.YELLOW + f"🤖 RuleBot: Good Afternoon, {name}! 😊")

    elif user == "good evening":
        print(Fore.MAGENTA + f"🤖 RuleBot: Good Evening, {name}! 🌇")

    elif user == "good night":
        print(Fore.MAGENTA + f"🤖 RuleBot: Good Night, {name}! Sleep well and sweet dreams. 🌙")

    # Exit

    elif user == "bye" or user == "by" or user == "exit" or user == "quit":

        print(Fore.GREEN + "\n" + "═" * 55)
        print(Fore.GREEN + f"🤖 RuleBot: Goodbye {name}! 👋")
        print(Fore.GREEN + "Thank you for chatting with me.")
        print(Fore.GREEN + "Have a wonderful day! 😊")
        print(Fore.GREEN + "═" * 55)

        break

    # Unknown Input

    else:
        print(Fore.RED + "🤖 RuleBot: I'm sorry, I didn't understand that.")
        print(Fore.YELLOW + "💡 Try asking about AI, Python, greetings, or type 'help'.")