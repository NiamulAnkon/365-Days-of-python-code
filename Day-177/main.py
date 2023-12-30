import tkinter as tk
from tkinter import scrolledtext
import random

class ChatBotApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Chat Bot Application")
        self.master.geometry("600x400")

        self.chat_history = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=40, height=10)
        self.chat_history.pack(pady=10)

        self.user_input = tk.Entry(self.master, width=40)
        self.user_input.pack(pady=10)

        self.send_button = tk.Button(self.master, text="Send", command=self.send_user_input)
        self.send_button.pack(pady=10)

        self.responses = {
            "hello": ["Hello!", "Hi there!", "Greetings!"],
            "how_are_you": ["I'm doing well, thank you!", "I'm here and ready to help!"],
            "learn_greeting": ["To greet in the target language, say 'hello' or 'hi'!"],
            "learn_numbers": ["To learn numbers, say 'one', 'two', etc."],
        }

        self.chat_history.insert(tk.END, "Chatbot: Welcome! How can I help you?\n")

    def send_user_input(self):
        user_message = self.user_input.get().lower()
        self.chat_history.insert(tk.END, f"You: {user_message}\n")

        chatbot_response = self.get_chatbot_response(user_message)
        self.chat_history.insert(tk.END, f"Chatbot: {chatbot_response}\n")

        self.user_input.delete(0, tk.END)

    def get_chatbot_response(self, user_message):
        if "hello" in user_message:
            return random.choice(self.responses["hello"])
        elif "how are you" in user_message:
            return random.choice(self.responses["how_are_you"])
        elif "learn greeting" in user_message:
            return random.choice(self.responses["learn_greeting"])
        elif "learn numbers" in user_message:
            return random.choice(self.responses["learn_numbers"])
        else:
            return "I'm still learning. Let's keep it simple for now!"

if __name__ == "__main__":
    root = tk.Tk()
    chatbot_app = ChatBotApplication(root)
    root.mainloop()
