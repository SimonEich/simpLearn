from db.db import DB
from gui.gui import GUI

db_name = 'cards.db'


if __name__ == "__main__":
    
    
    data = DB(db_name)
    gui = GUI(data)
    
    gui.root.mainloop()
    
    