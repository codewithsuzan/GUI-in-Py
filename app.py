from tkinter import *
from time import time
import random as r

# Functions
def calculate_results():
    global start_time
    user_input = input_text.get("1.0", END).strip()  # Get user input from Text widget
    end_time = time()

    # Calculate speed
    time_taken = end_time - start_time
    speed = len(user_input) / time_taken  # Characters per second
    speed_wpm = (len(user_input) / 5) / (time_taken / 60)  # Words per minute

    # Calculate errors
    errors = 0
    for i in range(len(selected_sentence)):
        try:
            if selected_sentence[i] != user_input[i]:
                errors += 1
        except IndexError:
            errors += 1

    # Display results
    result_label.config(
        text=f"Speed: {round(speed_wpm)} WPM\nErrors: {errors}"
    )


def start_test():
    global start_time, selected_sentence
    start_time = time()  # Record start time
    selected_sentence = r.choice(test_sentences)  # Pick a random sentence
    sentence_label.config(text=selected_sentence)  # Show sentence
    result_label.config(text="")  # Clear previous results
    input_text.delete("1.0", END)  # Clear the text area


# Test sentences
test_sentences = [
    "The quick brown fox jumps over the lazy dog",
    "I love programming in Python",
    "Welcome to my GitHub repository",
]

# Tkinter GUI Setup
root = Tk()
root.title("Typing Speed Test")
root.geometry("600x400")
root.resizable(False, False)

# Widgets
Label(root, text="Typing Speed Test", font=("Helvetica", 18, "bold")).pack(pady=10)

sentence_label = Label(root, text="", font=("Helvetica", 14), wraplength=550, justify="center")
sentence_label.pack(pady=10)

input_text = Text(root, height=5, width=60, font=("Helvetica", 12))
input_text.pack(pady=10)

start_button = Button(root, text="Start Test", command=start_test, font=("Helvetica", 12), bg="lightblue")
start_button.pack(pady=5)


submit_button = Button(root, text="Submit", command=calculate_results, font=("Helvetica", 12), bg="lightgreen")
submit_button.pack(pady=5)

result_label = Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

# Run the Tkinter loop
root.mainloop()
