import tkinter as tk
from PIL import Image, ImageTk
import random

# =============================================================================
#                              ROCK PAPER SCISSORS
# =============================================================================
# A simple GUI game where the user plays rock-paper-scissors against the
# computer. Uses Tkinter for the interface and Pillow to handle images.
# Implements a light theme UI with scoring and game logic.
# =============================================================================


# -----------------------------------
#          GAME SETUP & CONSTANTS
# -----------------------------------

# Choices available for the game
choices = ["rock", "paper", "scissors"]

# Initial scores for user and computer
user_score = 0
computer_score = 0

# Light theme color scheme dictionary
theme = {
    "bg": "#f0f0f0",
    "fg": "#333333",
    "title_fg": "#1976d2",
    "win_fg": "#388e3c",
    "lose_fg": "#d32f2f",
    "tie_fg": "#0288d1",
    "button_bg": ["#64b5f6", "#81c784", "#e57373"],
    "button_active_bg": ["#42a5f5", "#66bb6a", "#ef5350"],
    "score_fg": "#555555"
}


# -----------------------------------
#           WINDOW SETUP
# -----------------------------------

# Initialize main Tkinter window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("520x460")


# -----------------------------------
#         IMAGE LOADING FUNCTION
# -----------------------------------

def load_image(filename):
    """
    Loads an image from a file and resizes it to 200x200 pixels.
    
    Args:
        filename (str): Path to the image file.
    
    Returns:
        ImageTk.PhotoImage: Tkinter-compatible image object.
    """
    img = Image.open(filename)
    img = img.resize((200, 200))
    return ImageTk.PhotoImage(img)


# Load images for rock, paper, and scissors choices
rock_img = load_image("rock.png")
paper_img = load_image("paper.png")
scissors_img = load_image("scissors.png")

# Dictionary to easily access images by choice name
images = {
    "rock": rock_img,
    "paper": paper_img,
    "scissors": scissors_img
}


# -----------------------------------
#          UTILITY FUNCTIONS
# -----------------------------------

def set_buttons_state(state):
    """
    Enable or disable all the choice buttons.
    
    Args:
        state (str): "normal" to enable buttons, "disabled" to disable.
    """
    rock_btn.config(state=state)
    paper_btn.config(state=state)
    scissors_btn.config(state=state)


def show_result(user_choice):
    """
    Determine the computer's choice, update UI elements to show choices,
    decide the winner, update scores, and re-enable buttons.
    
    Args:
        user_choice (str): The choice made by the user.
    """
    global user_score, computer_score

    # Computer randomly picks an option
    computer_choice = random.choice(choices)

    # Display user and computer images based on their choices
    user_image_label.config(image=images[user_choice])
    computer_image_label.config(image=images[computer_choice])

    # Update labels to show choices
    user_choice_label.config(text=f"You chose: {user_choice.capitalize()}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice.capitalize()}")

    # Decide winner and update the result label and scores accordingly
    if user_choice == computer_choice:
        result_label.config(text="It's a Tie!", fg=theme["tie_fg"])
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result_label.config(text="You Win!", fg=theme["win_fg"])
        user_score += 1
    else:
        result_label.config(text="Computer Wins!", fg=theme["lose_fg"])
        computer_score += 1

    # Update scoreboard with the latest scores
    score_label.config(text=f"Score: You {user_score} - {computer_score} Computer")

    # Re-enable buttons for the next round
    set_buttons_state("normal")


def play(user_choice):
    """
    Handles the user's button click.
    Shows user's choice immediately, displays 'thinking' message,
    disables buttons temporarily, and calls show_result after delay.
    
    Args:
        user_choice (str): The choice made by the user.
    """
    user_choice_label.config(text=f"You chose: {user_choice.capitalize()}")
    computer_choice_label.config(text="Computer is thinking...")
    result_label.config(text="")
    set_buttons_state("disabled")

    # Display user's choice image immediately
    user_image_label.config(image=images[user_choice])
    # Clear computer's image for suspense
    computer_image_label.config(image="")

    # Call show_result after 1.5 seconds delay
    root.after(1500, lambda: show_result(user_choice))


def apply_theme():
    """
    Apply the light theme colors to all widgets in the window.
    """
    root.config(bg=theme["bg"])
    title_label.config(bg=theme["bg"], fg=theme["title_fg"])
    button_frame.config(bg=theme["bg"])
    images_frame.config(bg=theme["bg"])

    user_choice_label.config(bg=theme["bg"], fg=theme["fg"])
    computer_choice_label.config(bg=theme["bg"], fg=theme["fg"])
    result_label.config(bg=theme["bg"])  # fg set dynamically on results
    score_label.config(bg=theme["bg"], fg=theme["score_fg"])

    # Style buttons with colors from theme dictionary
    rock_btn.config(
        bg=theme["button_bg"][0],
        fg="white",
        activebackground=theme["button_active_bg"][0],
        cursor="hand2"
    )
    paper_btn.config(
        bg=theme["button_bg"][1],
        fg="white",
        activebackground=theme["button_active_bg"][1],
        cursor="hand2"
    )
    scissors_btn.config(
        bg=theme["button_bg"][2],
        fg="white",
        activebackground=theme["button_active_bg"][2],
        cursor="hand2"
    )


# -----------------------------------
#         GUI WIDGET SETUP
# -----------------------------------

# Title label with large bold font at top
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Segoe UI", 28, "bold"))
title_label.pack(pady=(20, 10))

# Frame to hold the three choice buttons horizontally
button_frame = tk.Frame(root)
button_frame.pack(pady=15)

# Common button styles for cleaner code
button_style = {
    "font": ("Segoe UI", 14, "bold"),
    "width": 10,
    "bd": 0
}

# Rock choice button
rock_btn = tk.Button(button_frame, text="Rock", command=lambda: play("rock"), **button_style)
rock_btn.grid(row=0, column=0, padx=10)

# Paper choice button
paper_btn = tk.Button(button_frame, text="Paper", command=lambda: play("paper"), **button_style)
paper_btn.grid(row=0, column=1, padx=10)

# Scissors choice button
scissors_btn = tk.Button(button_frame, text="Scissors", command=lambda: play("scissors"), **button_style)
scissors_btn.grid(row=0, column=2, padx=10)

# Frame to hold user and computer images side-by-side
images_frame = tk.Frame(root)
images_frame.pack(pady=20)

# Label for user's chosen image, starting with rock by default
user_image_label = tk.Label(images_frame, image=rock_img)
user_image_label.grid(row=0, column=0, padx=50)

# Label for computer's chosen image, starts empty
computer_image_label = tk.Label(images_frame, image="")
computer_image_label.grid(row=0, column=1, padx=50)

# Label to show user's choice text
user_choice_label = tk.Label(root, text="", font=("Segoe UI", 14))
user_choice_label.pack()

# Label to show computer's choice or 'thinking...' text
computer_choice_label = tk.Label(root, text="", font=("Segoe UI", 14))
computer_choice_label.pack()

# Label to show game result (win/lose/tie)
result_label = tk.Label(root, text="", font=("Segoe UI", 20, "bold"))
result_label.pack(pady=15)

# Label to show the current score
score_label = tk.Label(root, text="Score: You 0 - 0 Computer", font=("Segoe UI", 16))
score_label.pack(pady=(0, 20))


# -----------------------------------
#             MAIN LOGIC
# -----------------------------------

# Apply the light theme colors initially
apply_theme()

# Start Tkinter event loop to run the app
root.mainloop()
