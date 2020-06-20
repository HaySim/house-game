import tkinter as tk

tries = 0
# Changing the word
#the_word = [""]
the_word = list("HAYLEY")
guess_word = list(the_word)

# Change each character of guess_word to "_"
for index in range(len(guess_word)):
    guess_word[index] = "_"

def add_spaces_guess_word(guess_word):

    guess_word_with_spaces = ""
    for index in range(len(guess_word)):
        guess_word_with_spaces = guess_word_with_spaces + " " + guess_word[index]
    return guess_word_with_spaces

# Logic for when player makes a guess: 
def button_click(btn):
    global guess_word
    global guess_word_with_spaces
    global tries

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

    if tries >= 7:
        canvas.create_text(1120, 450, font = "Times 100", text = "You Lose!")

    if guess_word == "".join(the_word):
        canvas.create_text(1100, 450, font = "Times 100", text = "You Win!")

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


# Creating the shapes for the house (x1, y1, x2, y2):
def draw_house(life):
    # Draw large rectangle (main body of house): 
    if life == 1:
        canvas.create_rectangle(155, 250, 580, 635, fill = "", width = 3)
    # Draw triangle (for roof): 
    elif life == 2:
        points = [155, 250, 580, 250, 367, 100, 155, 250]
        canvas.create_polygon(points, fill = "", outline = "black",  width = 3)
    # Draw rectangle (for door)
    elif life == 3:
        canvas.create_rectangle(330, 470, 404, 635, fill = "", width = 3)
    # Draw rectangle (top left window):
    elif life == 4:
        canvas.create_rectangle(193, 300, 293, 400, width = 3)
    # Draw rectangle (top right window):
    elif life == 5:
        canvas.create_rectangle(442, 300, 542, 400, width = 3)
    # Draw rectangle (bottom left window):
    elif life == 6:
        canvas.create_rectangle(193, 500, 293, 600, width = 3)
    # Draw rectangle (bottom right window):
    elif life == 7:
        canvas.create_rectangle(442, 500, 542, 600, width = 3)

guess_word_with_spaces = add_spaces_guess_word(guess_word)

# Create a new window object and storing its reference in root variable:
root = tk.Tk()
root.title("House Game")

# Create a canvas of a fixed size attached to root:
canvas = tk.Canvas(root, width = 1650, height = 950)
canvas.pack()

# Store id of text object:
guess_word_id = canvas.create_text(1100,300, font = "Times 120", text = guess_word_with_spaces)

my_text = "Guess a letter from A to Z"
canvas.create_text(828,50, font = "Times 25", text = my_text)




place_buttons()

root.mainloop()