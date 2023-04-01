import random

class Room:
    def __init__(self, name, desc, exits,items=[],items_player_should_have=None,old_lady=None):
        self.name = name
        self.desc = desc
        self.items = items
        self.exits = exits
        self.items_player_should_have=items_player_should_have
        self.old_lady=old_lady

    def get_exit(self, direction):
        return self.exits.get(direction)
    
    def get_item(self,item):
        if item in self.items:
            return item 
        return None
    
    def get_surprise(self):
        if self.old_lady:
            sup= random.choice(self.old_lady)
            return sup
        return False
        
    def add_item(self, item):
        self.items.append(item)
        # print(self.items)

    def remove_item(self, item):
        self.items.remove(item)




  

