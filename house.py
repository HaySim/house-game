import tkinter as tk

def callback():
    print("Clicked")

# Create a new window object and storing its reference in root variable:
root = tk.Tk()
root.title("House Game")

# Create a canvas of a fixed size attached to root:
canvas = tk.Canvas(root, width = 1500, height = 900)
canvas.pack()

# Store id of text object:
txt_id = canvas.create_text(250,150, font="Times 100", text="_ _ _ _ _")

# Rename text value:
canvas.itemconfig(txt_id, text = "Hi") 



canvas.create_line(0, 0, 100, 100)

btn = tk.Button(master = root, command = callback, text = "A", font = "Times 100")
btn.place(x = 30 , y = 600)


root.mainloop()