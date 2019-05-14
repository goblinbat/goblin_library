menulist = []

class Menu:
    def __init__(self, idnum, name, desc, ingredients, price):
        self.idnum = idnum
        self.name = name
        self.desc = desc
        self.ingredients = ingredients
        self.price = price
    
    def __repr__(self):
        return self.name


class MenuRepo:
    def add_item(idnum, name, desc, ingredients, price):
        new = Menu(idnum, name, desc, ingredients, price)
        menulist.append(new)
    
    def view_menu():
        return menulist
    
    def delete_menu_item(name):
        for item in menulist:
            if name == item.name:
                index = menulist.index(item)
                del menulist[index]
                return True
