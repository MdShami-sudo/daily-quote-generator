import tkinter as tk
from tkinter import ttk
import datetime

class MotivationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Daily Motivation Quote Generator")
        self.root.geometry("400x200")

        self.quotes = {
            "Monday": "The future depends on what you do today. – Mahatma Gandhi",
            "Tuesday": "The only way to do great work is to love what you do. – Steve Jobs",
            "Wednesday": "Success is not the key to happiness. Happiness is the key to success. – Albert Schweitzer",
            "Thursday": "Don't watch the clock; do what it does. Keep going. – Sam Levenson",
            "Friday": "Keep your face always toward the sunshine—and shadows will fall behind you. – Walt Whitman",
            "Saturday": "You are never too old to set another goal or to dream a new dream. – C.S. Lewis",
            "Sunday": "Believe you can and you're halfway there. – Theodore Roosevelt"
        }

        self.current_day = datetime.datetime.now().strftime("%A")

        self.display_quote()

    def display_quote(self):
        quote = self.quotes.get(self.current_day, "Stay motivated!")

        quote_label = ttk.Label(self.root, text=quote, wraplength=350, font=("Helvetica", 14))
        quote_label.pack(pady=20)

        day_label = ttk.Label(self.root, text=f"Today is {self.current_day}", font=("Helvetica", 12))
        day_label.pack(pady=10)

def main():
    root = tk.Tk()
    app = MotivationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
