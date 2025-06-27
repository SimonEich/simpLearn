from .helper import choose_file, back_Button, create_button, create_label, destroy_widgets

def add_words_screen(self)->None: 
    destroy_widgets(self.root)
    back_Button(self)
    
    create_label(self.root, "Add Words", 0.5, 20, 30)  # Title
    create_button(self, 'Add from List', 'Add from List', lambda: self.data.add_listdata_db(file_path=choose_file()), 0.5, 120)
    create_button(self, 'Add Voca', 'Add Voca', lambda:add_voca_screen(self), 0.5, 170)
    create_button(self, 'Show Voca', 'Show Voca', lambda: self.data.print_all_words_and_stats(), 0.5, 220) #list_screen(self)


    
def add_voca_screen(self)->None:
    destroy_widgets(self.root)
    back_Button(self)
    
    create_label(self.root, "Voca", 0.5, 125, 30)  # Title
    
def list_screen(self)->None:
    destroy_widgets(self.root)
    back_Button(self)
    
    create_label(self.root, "List", 0.5, 125, 30)  # Title
    
    
    
    