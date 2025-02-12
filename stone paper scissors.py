import tkinter as tk
import random

def play(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    
    result = ''
    if user_choice == computer_choice:
        result = "It's a Draw!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        result = 'You Win!'
    else:
        result = 'You Lose!'
    
    label_result.config(text=f'Computer chose: {computer_choice}\n{result}')

# GUI Setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x400")

tk.Label(root, text="Choose one:", font=("Arial", 14)).pack(pady=20)

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Rock", font=("Arial", 12), command=lambda: play("Rock")).grid(row=0, column=0, padx=10)
tk.Button(frame, text="Paper", font=("Arial", 12), command=lambda: play("Paper")).grid(row=0, column=1, padx=10)
tk.Button(frame, text="Scissors", font=("Arial", 12), command=lambda: play("Scissors")).grid(row=0, column=2, padx=10)

label_result = tk.Label(root, text="", font=("Arial", 14), pady=20)
label_result.pack()

root.mainloop()
