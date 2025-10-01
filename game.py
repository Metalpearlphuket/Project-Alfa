import tkinter as tk
import random

def roll_dice():
    dice_number = random.randint(1, 6)
    result_label.config(text=f"ผลการทอย: {dice_number}")

root = tk.Tk()
root.title("เกมทอยลูกเต๋า")

roll_button = tk.Button(root, text="ทอยลูกเต๋า", font=("Arial", 20), command=roll_dice)
roll_button.pack(pady=20)

result_label = tk.Label(root, text="ผลการทอย: -", font=("Arial", 24))
result_label.pack(pady=20)

root.mainloop()