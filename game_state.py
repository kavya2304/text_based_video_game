import json
from room import Room
import sys
class GameState:
    def __init__(self, map_data, player_location=0, inventory=None):
        self.map_data = map_data
        self.player_location = player_location
        self.inventory = inventory or []
        self.is_game_over=False
 
    def get_current_room(self):
        return self.get_room(self.player_location)

    def get_room(self, room_idx):
        room_data = self.map_data[room_idx]
        #print(room_data)
        if "items_player_should_have" or "old_lady" or "items" in room_data:
            if "items" and "items_player_should_have" in room_data :
                return Room(room_data["name"],room_data["desc"],room_data["exits"],room_data["items"],room_data["items_player_should_have"],None)
    
            elif "items" in room_data:
                if "old_lady" in room_data:
                    return Room(room_data["name"],room_data["desc"],room_data["exits"],room_data["items"],None,room_data["old_lady"])
                else:
                    return Room(room_data["name"],room_data["desc"],room_data["exits"],room_data["items"])

        return Room(room_data["name"],room_data["desc"],room_data["exits"])

    def get_exit(self, room_idx, direction):
        room_data = self.map_data[room_idx]
        return room_data['exits'].get(direction)

    def get_inventory(self):
        return self.inventory

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def execute_command(self, command):
        verb = command.verb
        args = command.args
        # print(verb)

        if verb == 'go':
            if len(args)>0:
                direction = args[0]
                exit_idx = self.get_exit(self.player_location, direction)
            
                if exit_idx is None:
                    print('There\'s no way to go',direction,'\n')
                else:
                    self.player_location = exit_idx
                    roomg = self.get_current_room()
                    print('You go',direction,'\n')
                    # print('----------->>',roomg.items_player_should_have)
                    #for winning and loosing conditions
                    if  roomg.items_player_should_have is not None:
                        # print('-----x',self.inventory)
                        if any(item in roomg.items_player_should_have for item in self.inventory):
                            print('You can do the magic with help of Magicbook here,and escape from this adventure now,Hurrayyy,You Won the game!!')
                            sys.exit()
                        else:
                            print('You entered wrong room without needed items and the Witch killed you.You lost the game!!!')
                            sys.exit()
                    #Room details
                    print('>',roomg.name,'\n')
                    print(roomg.desc,'\n')
                    if roomg.items:
                        print('Items:',' '.join(roomg.items),'\n')
                    print('Exits:', ' '.join(roomg.exits.keys()),'\n')
                    # This is for abracadabra verb
                    if roomg.old_lady is not None:
                        print('Hey, there is a old-lady in this room who can grant you an item that helps you win the game,to get that say "ABRACADABRA"!!!!!!')
            else:
                print('Sorry, you need to \'go\' somewhere.','\n')
                
        elif verb == 'look':
            rm=self.get_current_room()
            print('>',rm.name,'\n')
            print(rm.desc,'\n')
            # print(rm.items)
            if rm.items:
                print('Items:',' '.join(rm.items),'\n')
            print('Exits:', ' '.join(rm.exits.keys()),'\n')
            
        elif verb == 'get':
            item_name = ' '.join(args)
            room = self.get_current_room()
            item = room.get_item(item_name)
            if item:
                room.remove_item(item)
                self.add_item(item)
                print('You pick up the',item,end='.\n')
            else:
                print('There\'s no',item_name,'anywhere.')

        elif verb == 'quit':
                print('Goodbye!')
                self.is_game_over=True

        elif verb == 'inventory':
            print('Inventory:')
            inv=self.get_inventory()
            if inv:
                print(' ','\n  '.join(inv),'\n')
            else:
                print('You\'re not carrying anything.')
        
        elif verb=='abracadabra':
            room2 = self.get_current_room()
            ite= room2.get_surprise()
            if ite:
                self.add_item(ite)   
                print('You got',ite,end='!!\n')
            else:
                print('You cant use abracadabra here!!')

        elif verb == 'drop':
            item_name = ' '.join(args)
            if item_name in self.inventory:
                self.remove_item(item_name)
                room = self.get_current_room()
                room.add_item(item_name)
                print('You drop the',item_name,end='.\n')
            else:
                print("You're not carrying that.")
        else:
            print("I don't understand.")

    # def is_game_over(self):
    #     return self.get_current_room().is_exit()


