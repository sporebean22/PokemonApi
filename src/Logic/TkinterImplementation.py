
from tkinter import *

class TkinterImplementation:
  def __init__(self, window_title, aspect_ratio):
    window = Tk()
    window.title(window_title)
    window.geometry(aspect_ratio)
    window.mainloop()

  def New_Label(text, grid_column, grid_row):
    new_label = Label(window, text=text)
    new_label.grid(column=grid_column, row=grid_row)

  def New_Input(input_width, grid_column, grid_row):
    new_input = Entry(window,width=input_width)
    new_input.grid(column=grid_column, row=grid_row)

  def clicked():
    label.configure(text="Button was clicked !!")

  def New_Button(button_text, button_command, grid_column, grid_row):
    new_button = Button(window, text=button_text, command=button_command)
    new_button.grid(column=2, row=0)
