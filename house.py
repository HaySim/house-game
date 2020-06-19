import tkinter as tk

def callback():
    print("Clicked")

def button_click(btn):
    print(btn["text"])

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


# Create a new window object and storing its reference in root variable:
root = tk.Tk()
root.title("House Game")

# Create a canvas of a fixed size attached to root:
canvas = tk.Canvas(root, width = 1650, height = 950)
canvas.pack()

# Store id of text object:
txt_id = canvas.create_text(250,150, font = "Times 100", text = "_ _ _ _ _")

# Rename text value:
canvas.itemconfig(txt_id, text = "Hi") 



canvas.create_line(0, 0, 100, 100)

place_buttons()



root.mainloop()