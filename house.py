import tkinter as tk
import random

words = ["CHIMNEY", "KITCHEN", "WARDROBE", "BATHROOM", "BEDROOM", "GARDEN", "SHOWER", "ALLOTMENT"]

tries = 0
MAX_TRIES = 7
# Changing the word
#the_word = [""]
the_word = list(random.choice(words))
guess_word = list(the_word)

canvas_ids = []
AZ_btn_ids = []
try_again_id = 0

# Change each character of guess_word to "_"
def to_underscore(guess_word):
    for index in range(len(guess_word)):
        guess_word[index] = "_"

    return guess_word

def add_spaces_guess_word(guess_word):

    guess_word_with_spaces = ""
    for index in range(len(guess_word)):
        guess_word_with_spaces = guess_word_with_spaces + " " + guess_word[index]
    return guess_word_with_spaces

def choose_word():
    global the_word
    global guess_word

    the_word = list(random.choice(words))
    guess_word = list(the_word)

    guess_word = to_underscore(guess_word)

    canvas.itemconfig(guess_word_id, text = guess_word)

# Logic for when player makes a guess: 
def button_click(btn):
    global the_word
    global guess_word
    global guess_word_with_spaces
    global tries
    global try_again_id, words

    btn["state"] = "disabled"

    char = btn["text"]

    correct_guess = False

    for index in range(len(the_word)):

        # If correct guess then reveal letter:
        if char == the_word[index]:
            guess_word = list(guess_word)
            guess_word[index] = char 
            correct_guess = True

    guess_word = ''.join(guess_word)  

    guess_word_with_spaces = add_spaces_guess_word(guess_word)
    canvas.itemconfig(guess_word_id, text = guess_word_with_spaces)

    if not correct_guess:
        tries = tries + 1
        draw_house(tries)

        tries_msg = "Attempt " + str(tries) + " of " + str(MAX_TRIES)
        canvas.itemconfig(tries_msg_id, text = tries_msg)

    if guess_word == "".join(the_word):
        for b in AZ_btn_ids:
            b["state"] = "disabled"

        you_win_txt_id = canvas.create_text(1100, 450, font = "Times 100", text = "YOU WIN!", fill = "green")

        canvas_ids.append(you_win_txt_id)

        btn = tk.Button(master = root, text = "NEW WORD" , font = "Times 100",\
                       foreground = "red" , width = 13, height = 1, command = try_again)
        btn.place(x = 790 , y = 530)

        try_again_id = btn

# Inserting letters A-Z:
def place_buttons():
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", \
               "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", \
               "U", "V", "W", "X", "Y", "Z"]

    delta_x = 0
    delta_y = 0

    num_letters_created_so_far = 0
    on_second_row = False

    for char in letters:
        btn = tk.Button(master = root, text = char, font = "Times 100", width = 2, height = 1)
            
        # Configure btn to call button_click() with btn's reference as an arguement:
        btn.configure(command = lambda button = btn: button_click(button))

        btn.place(x = 30 + delta_x , y = 680 + delta_y)
        delta_x = delta_x + 122

        num_letters_created_so_far = num_letters_created_so_far + 1
        if (num_letters_created_so_far > 12) and (not on_second_row):
            delta_x = 0 
            delta_y = 122
            on_second_row = True

        AZ_btn_ids.append(btn)

def try_again():
    global tries
    for id in canvas_ids:
        canvas.delete(id)
    tries = 0 
    tries_msg = "Attempt " + str(tries) + " of " + str(MAX_TRIES)
    canvas.itemconfig(tries_msg_id, text = tries_msg)

    choose_word()

    for btn in AZ_btn_ids:
        btn["state"] = "normal"

    try_again_id.destroy()

# Creating the shapes for the house (x1, y1, x2, y2):
def draw_house(life):
    global try_again_id

    some_id = 0
    # Draw large rectangle (main body of house): 
    if life == 1:
        some_id = canvas.create_rectangle(155, 250, 580, 635, fill = "", width = 3)
    # Draw triangle (for roof): 
    elif life == 2:
        points = [155, 250, 580, 250, 367, 100, 155, 250]
        some_id = canvas.create_polygon(points, fill = "", outline = "black",  width = 3)
    # Draw rectangle (for door)
    elif life == 3:
        some_id = canvas.create_rectangle(330, 470, 404, 635, fill = "", width = 3)
    # Draw rectangle (top left window):
    elif life == 4:
        some_id = canvas.create_rectangle(193, 300, 293, 400, width = 3)
    # Draw rectangle (top right window):
    elif life == 5:
        some_id = canvas.create_rectangle(442, 300, 542, 400, width = 3)
    # Draw rectangle (bottom left window):
    elif life == 6:
        some_id = canvas.create_rectangle(193, 500, 293, 600, width = 3)
    # Draw rectangle (bottom right window):
    elif life == 7:
        for b in AZ_btn_ids:
            b["state"] = "disabled"

        some_id = canvas.create_rectangle(442, 500, 542, 600, width = 3)
        btn = tk.Button(master = root, text = "NEW WORD" , font = "Times 100",\
                       foreground = "red" , width = 13, height = 1, command = try_again)
        btn.place(x = 790 , y = 450)

        try_again_id = btn

    canvas_ids.append(some_id)
        

guess_word = to_underscore(guess_word)

guess_word_with_spaces = add_spaces_guess_word(guess_word)

# Create a new window object and storing its reference in root variable:
root = tk.Tk()
root.title("House Game")

# Create a canvas of a fixed size attached to root:
canvas = tk.Canvas(root, width = 1650, height = 950)
canvas.pack()

# Store id of text object:
guess_word_id = canvas.create_text(1100,300, font = "Times 120", text = guess_word_with_spaces)

my_text = "CLICK a letter from A to Z"
canvas.create_text(828, 50, font = "Times 25", text = my_text)

tries_msg = "Attempt " + str(tries) + " of " + str(MAX_TRIES)
tries_msg_id = canvas.create_text(827, 100, font = "Times 20", fill = "red", text = tries_msg)



place_buttons()

root.mainloop()