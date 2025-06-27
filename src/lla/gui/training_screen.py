import random
from typing import Callable
from .helper import destroy_widgets, back_Button, create_label, create_button, list_training_data, level_check

y_button = 275




def training_screen(self)->None:
    destroy_widgets(self.root)
    back_Button(self)
    
    self.data.print_all_words_with_statistics()
    
    self.id_word, self.word, self.translation, self.sentence, self.right, self.wrong, self.word_one, self.word_two=list_training_data(self)
    
    if self.right<3:
        level = 1
        level_One(self, level, 'training')
    elif self.right>=3 and self.right<6:
        level = 2
        level_Two(self, level)
    elif self.right>=6 and self.right<9:
        level =3
        level_Three(self, level)
    elif self.right>=9 and self.right<13:
        level = 4
        level_Four(self, level)
    elif self.right>13:
        level = 5
        level_Five(self, level)

def repeat_screen(self, state)->None:
    destroy_widgets(self.root)
    back_Button(self)
    
    print(state)
    print('repeat screen')
    
    a =self.data.get_words_with_wrong_answers()
    print(a)

    level=0
    


def level_setup(self, level: int, command: Callable[[], None])->None:
    
    print(f'the actuall level is {level}')
    destroy_widgets(self.root)
    back_Button(self)
    
    self.total_words, self.words_with_high_right, self.num_state_true = self.data.statistic()
    


    
    if level !=0:       
        create_label(self.root, f"Level {level} ", 0.5, 20, 20)  # Title
    
    create_label(self.root, f"Total:{self.total_words}", 0.8, 60, 15)  # right
    create_label(self.root, f"Game:{self.num_state_true}", 0.8, 20, 15)  # right
    create_label(self.root, f"Passed:{self.words_with_high_right}", 0.8, 40, 15)  # wrong
    create_label(self.root, f"Right: {self.right}", 0.2, 60, 15)  # right
    create_label(self.root, f"Wrong: {self.wrong}", 0.2, 80, 15)  # right

    
    if level == 0:
        create_label(self.root, self.word, 0.5, 125, 30)  # Title
        
    
    if level == 1:
        print('level 1')
        create_label(self.root, self.word, 0.5, 125, 30)  # Title
        
    elif level == 2:
        create_label(self.root, self.word, 0.5, 125, 30)  # Title
        print('level setup if called level 2')
        create_label(self.root, self.sentence, 0.5,180,20)

        
    elif level == 3:
        print('level 3')
        create_label(self.root, self.word, 0.5, 125, 30)  # Title

     
    elif level == 4:
        print('level 4')
        create_label(self.root, self.translation, 0.5, 125, 30)  # Title



def level_One(self, level, state)->None:
    y = 275

    level_setup(self, level, None)
    

    number = random.randint(1, 3)
    
    if number == 1:
        option1 = self.translation
        option2 = self.word_one
        option3 = self.word_two
    elif number ==2:
        option1 = self.word_one 
        option2 = self.translation
        option3 = self.word_two
    elif number ==3:
        option1 = self.word_one   
        option2 = self.word_two
        option3 = self.translation


    create_button(self, 'option1', option1, lambda:level_one_check(self, option1, level, state), 0.2, y_button)
    create_button(self, 'option2', option2, lambda:level_one_check(self, option2, level, state), 0.5, y_button)
    create_button(self, 'option3', option3, lambda:level_one_check(self, option3, level, state), 0.8, y_button)
    
def level_one_check(self, option, level, state):
    print(str(option))
    
    print(state)
    
    if state == 'training':
        if option==self.translation:
            self.data.training_right(self.id_word)
            words_true_state=self.data.get_all_tue_state()
            level_check(self)
            print(f'tue state: {str(len(words_true_state))}')
            training_screen(self)
        else:
            print ('wrong')
            level_One_wrong(self, level)
    else:
        if option==self.translation:
            self.data.training_right_right_rep(self.id_word)
            words_true_state=self.data.get_all_tue_state()
            level_check(self)
            print(f'tue state: {str(len(words_true_state))}')
            training_screen(self)
        else:
            print ('wrong')
            level_One_wrong(self, level)
        
        
def level_One_wrong(self, level)->None:
    
    self.data.training_wrong(self.id_word)

    
    level_setup(self, level, None)
    create_label(self.root, self.translation, 0.5, 180, 30)
    create_button(self, 'Next', 'Next', lambda: training_screen(self), 0.5, y_button)
    

def right_wrong_buttons(self)->None:
    create_button(self, 'Wrong', 'Wrong', lambda: func_wrong(self), 0.25, y_button)
    create_button(self, 'Right', 'Right', lambda: func_right(self), 0.75, y_button)


def func_right(self)->None:
    self.data.training_right(self.id_word)
    words_true_state=self.data.get_all_tue_state()
    print(f'true state: {str(len(words_true_state))}')
    level_check(self)

    training_screen(self)
    

def func_wrong(self)->None:
    print('func wrong')
    self.data.training_wrong(self.id_word)
    training_screen(self)
    

def level_Two(self, level)->None:
    destroy_widgets(self.root)
    back_Button(self)
    

    level_setup(self, level, lambda: level_Two_check(self, level))
    create_button(self, 'Translate', 'Translate', lambda: level_Two_check(self, 2), 0.5, y_button)

    

def level_Two_check(self, level)->None:
    print('level 2 check')
    destroy_widgets(self.root)
    back_Button(self)
    
    level_setup(self, level, lambda: None)
    
    create_label(self.root, self.translation, 0.5, 220, 25)
    create_label(self.root, self.sentence, 0.5,180,20)

    right_wrong_buttons(self)
    
def level_Three(self, level)->None:
    
    destroy_widgets(self.root)
    back_Button(self)
    
            
    
    level_setup(self, level, lambda: level_Three_check(self))
    create_button(self, 'Translate', 'Translate', lambda: level_Three_check(self, 3), 0.5, y_button)

    
def level_Three_check(self, level)->None:
    destroy_widgets(self.root)
    back_Button(self)
    
    level_setup(self, level, command=None)
    
    create_label(self.root, self.translation, 0.5, 220, 25)
    
    right_wrong_buttons(self)
    
def level_Four(self, level)->None:
    
    destroy_widgets(self.root)
    back_Button(self)
    
    level_setup(self, level, lambda: level_Four_check(self))
    create_button(self, 'Translate', 'Translate', lambda: level_Four_check(self, 4), 0.5, y_button)

    
def level_Four_check(self, level)->None:
    destroy_widgets(self.root)
    back_Button(self)

    level_setup(self, level, command=None)
    
    create_label(self.root, self.word, 0.5, 220, 25)
    
    right_wrong_buttons(self)

    


def level_Five(self, level)->None:
    destroy_widgets(self.root)
    back_Button(self)
    

    create_label(self.root, 'Congratulation: You know a new word!', 0.5, 150, 25)
    create_button(self, 'Next', 'Next', None, 0.5, y_button)


