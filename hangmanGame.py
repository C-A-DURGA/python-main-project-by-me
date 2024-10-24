import tkinter as tk
from tkinter import messagebox
import random

# List of words to guess
word_list = ["python", "hangman", "computer", "programming", "developer", "keyboard", "software"]

# Function to initialize the game
def start_game():
    global word, guessed_word, attempts
    word = random.choice(word_list).lower()
    guessed_word = ['_' for _ in word]
    attempts = 6
    update_display()

# Function to check guessed letter
def guess_letter():
    global attempts
    letter = entry_letter.get().lower()
    
    if len(letter) != 1 or not letter.isalpha():
        messagebox.showwarning("Invalid Input", "Please enter a single letter.")
        return

    entry_letter.delete(0, tk.END)
    
    if letter in guessed_word:
        messagebox.showinfo("Already Guessed", "You already guessed this letter!")
        return
    
    if letter in word:
        for i, char in enumerate(word):
            if char == letter:
                guessed_word[i] = letter
        update_display()
    else:
        attempts -= 1
        label_attempts.config(text=f"Attempts Left: {attempts}")
        if attempts == 0:
            messagebox.showinfo("Game Over", f"Sorry, you lost! The word was '{word}'.")
            start_game()

    if "_" not in guessed_word:
        messagebox.showinfo("Congratulations", "You guessed the word!")
        start_game()

# Function to update display with guessed word and remaining attempts
def update_display():
    label_word.config(text=" ".join(guessed_word))
    label_attempts.config(text=f"Attempts Left: {attempts}")

# Initialize Tkinter window
window = tk.Tk()
window.title("Hangman Game")
window.geometry("400x400")
window.resizable(False, False)

# Title label
label_title = tk.Label(window, text="Hangman Game", font=("Arial", 18))
label_title.pack(pady=20)

# Display word to guess
label_word = tk.Label(window, text="_ _ _ _ _ _ _", font=("Arial", 16))
label_word.pack(pady=10)

# Attempts left
label_attempts = tk.Label(window, text="Attempts Left: 6", font=("Arial", 12))
label_attempts.pack(pady=10)

# Input for guessing a letter
label_input = tk.Label(window, text="Guess a letter:", font=("Arial", 12))
label_input.pack()

entry_letter = tk.Entry(window, width=5, font=("Arial", 14))
entry_letter.pack(pady=5)

# Button to submit the guessed letter
btn_guess = tk.Button(window, text="Submit Guess", command=guess_letter, font=("Arial", 12), bg="#4CAF50", fg="white")
btn_guess.pack(pady=10)

# Button to restart the game
btn_restart = tk.Button(window, text="Restart Game", command=start_game, font=("Arial", 12), bg="#008CBA", fg="white")
btn_restart.pack(pady=10)

# Start the game
start_game()

# Start the Tkinter loop
window.mainloop()
