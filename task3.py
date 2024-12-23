import re
import tkinter as tk
from tkinter import ttk

def assess_password_strength(password):
    score = 0

    # Define criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'\\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?\":{}|<>]', password))

    # Calculate score
    if length_criteria:
        score += 1
    if uppercase_criteria:
        score += 1
    if lowercase_criteria:
        score += 1
    if number_criteria:
        score += 1
    if special_char_criteria:
        score += 1

    feedback = []

    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character (!@#$%^&*(),.?\":{}|<>).")

    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, score, feedback

def check_password():
    password = password_entry.get()
    strength, score, feedback = assess_password_strength(password)

    # Update strength label
    strength_label.config(text=f"Password Strength: {strength}", foreground="green" if strength == "Strong" else "orange" if strength == "Moderate" else "red")

    # Update feedback text
    feedback_text.set("\n".join(feedback))

def clear_fields():
    password_entry.delete(0, tk.END)
    strength_label.config(text="")
    feedback_text.set("")

# Create main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("600x500")
root.resizable(False, False)
root.configure(bg="white")

# Title label
title_label = tk.Label(root, text="Password Strength Checker", font=("Arial", 16, "bold"), bg="white", fg="black")
title_label.pack(pady=10)

# Password entry frame
password_frame = tk.Frame(root, bg="white")
password_frame.pack(pady=10)
password_label = tk.Label(password_frame, text="Enter Password:", font=("Arial", 12), bg="white")
password_label.pack(side="left", padx=5)
password_entry = ttk.Entry(password_frame, show="*", font=("Arial", 12), width=25)
password_entry.pack(side="left", padx=5)

# Check button
check_button = ttk.Button(root, text="Check Strength", command=check_password)
check_button.pack(pady=10)

# Strength label
strength_label = tk.Label(root, text="", font=("Arial", 12), bg="white")
strength_label.pack(pady=5)

# Feedback label
feedback_text = tk.StringVar()
feedback_label = tk.Label(root, textvariable=feedback_text, font=("Arial", 10), bg="white", fg="red", justify="left")
feedback_label.pack(pady=5)

# Clear button
clear_button = ttk.Button(root, text="Clear", command=clear_fields)
clear_button.pack(pady=10)

# Run the application
root.mainloop()

