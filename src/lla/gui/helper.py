from tkinter import Button, Label, filedialog
from typing import Callable
import tkinter as tk
import random



def create_button(self, name_Button: str, text: str, command: Callable[[], None], x: float, y: int) -> None:
    """
    Create a button and place it on the window.
    
    Args:
        name_Button: Name used to store the button as an attribute.
        text: Text displayed on the button.
        command: Function to be called when the button is clicked.
        x: Relative horizontal position (0 to 1).
        y: Absolute vertical position in pixels.
    """
    button = Button(self.root, text=text, width=14, font=("Arial", 14), command=command)
    button.place(relx=x, y=y, anchor="n")
    setattr(self, name_Button, button)

def create_label(root, text, relx: float, y: int, size) -> None:    
    text_var = tk.StringVar(value=text)
    label = Label(root, textvariable=text_var, font=("Arial", size, "bold"))
    label.place(relx=relx, y=y, anchor="n")

def back_Button(self)->None:
    create_button(self, 'back_button', 'Back', lambda: self.start_screen(), 0.2, 20)

def destroy_widgets(root):
    for widget in root.winfo_children():
        widget.destroy()

def choose_file():
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=(("Text and CSV files", "*.txt *.csv"),)
    )
    return file_path

def getting_word(self)->None:
    
    print('adding 10 or 1 Word')
    state=self.data.has_any_true_state()
    
    if state == False:
        self.data.states_to_true(10)
    elif state == True:
        print('one more true')
        self.data.states_to_true(1)
        
def list_repeat_data(self)->None:
    
    print('list repeat data')
    difficult_words = self.data.get_words_with_wrong_answers()
    i = random.randint(0, len(difficult_words)-1)
    
    i_one = i
    i_two = i
    
    while i == i_one or i == i_two or i_one == i_two:
        i_one = random.randint(0, len(difficult_words) - 1)
        i_two = random.randint(0, len(difficult_words) - 1)
    
    
    word_one = difficult_words[i_one][2]
    word_two = difficult_words[i_two][2]
    word = difficult_words[i]
    
    training_data = word + (word_one, word_two)
    
    
    return training_data
    
        
def list_training_data(self)->list:
    true_state=self.data.get_all_tue_state()
    print(f'Actual learning: {len(true_state)}')
    i = random.randint(0, len(true_state) - 1)
    
    i_one = i
    i_two = i
    
    while i == i_one or i == i_two or i_one == i_two:
        i_one = random.randint(0, len(true_state) - 1)
        i_two = random.randint(0, len(true_state) - 1)
    
    
    word_one = true_state[i_one][2]
    word_two = true_state[i_two][2]
    word = true_state[i]
    
    training_data = word + (word_one, word_two)
    #print(training_data)
    
    
    return training_data

def level_check(self)->None:
    if self.right == 3 or self.right == 6 or self.right == 9:
        print('level up')
        getting_word(self)
