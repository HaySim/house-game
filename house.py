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

# Create a new window object and storing its reference in root variable:
root = tk.Tk()
root.title("House Game")

# Create a canvas of a fixed size attached to root:
canvas = tk.Canvas(root, width = 1650, height = 950)
canvas.pack()

# Store id of text object:
txt_id = canvas.create_text(1000,150, font = "Times 120", text = "_ _ _ _ _")

# Rename text value:
#canvas.itemconfig(txt_id, text = "Hi") 


draw_house(1)
draw_house(2)
draw_house(3)
draw_house(4)
draw_house(5)
draw_house(6)
draw_house(7)




place_buttons()

root.mainloop()