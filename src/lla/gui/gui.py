from .helper import destroy_widgets, create_button, create_label
from .training_screen import training_screen, repeat_screen
from .add_words_screen import add_words_screen

import tkinter as tk
from tkinter import Label

class GUI:
    
    def __init__(self, data):
        self.data = data
        self._gui_config()
        self.start_screen()
        
        
    def _gui_config(self) -> None:
        self.root = tk.Tk()
        self.root.geometry("600x400")
        self.root.title('Voca App')
        
    def start_screen(self) -> None:
        destroy_widgets(self.root)
        
        create_label(self.root, "Voca", 0.5, 125, 40)  # Title¨
        
        
        

        create_button(self, 'Training', 'Training', lambda:training_screen(self), 0.25, 275)
        create_button(self, 'Add Words', 'Add Words', lambda: add_words_screen(self), 0.75, 275)
        
        


