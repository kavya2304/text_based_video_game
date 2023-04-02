import argparse
import json
from game_state import GameState

class Command:
    def __init__(self, verb, args):
        self.verb = verb
        self.args = args
        
def parse_command(input_string):
        words = input_string.strip().lower().split()
        verb = words[0]
        args = words[1:] 
        return Command(verb, args)
    
def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument("loop_map", help="JSON file containing the game map")
    # args = parser.parse_args()
    # with open(args.loop_map, "r") as f:
    #     map_data = json.load(f)
    # # print(map_data)   
    f=open('loop_map.json')
    map_data = json.load(f)
     
    game_state = GameState(map_data)
    room = game_state.get_current_room()
    print('>',room.name,'\n')
    print(room.desc,'\n')
    if room.items:
        print('Items:',' '.join(room.items),'\n')
    print('Exits:', ' '.join(room.exits.keys()),'\n')

    while not game_state.is_game_over:
        
        try:
             input_str = input('What would you like to do? ')
             command = parse_command(input_str)
             game_state.execute_command(command)
        except EOFError as e:  #use ctrl+z for EOF error if ctrl+D did not work
                print('Use \'quit\' to exit')


#     print('Game over!')    

if __name__ == "__main__":
    main()
    
    

