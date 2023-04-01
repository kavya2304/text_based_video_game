# text_based_video_game
This is a text based video game created using python.

Kavyasri Thalluri (kthallur@stevens.edu)

>>URL: https://github.com/kavya2304/text_based_video_game.git

>>An estimate of how many hours you spent on the project: 
15-25 hours

>>A description of how you tested your code: 
I have manually checked , covering all the cases that I wrote meaning all verbs and extensions , writing unit tests for the same and with the gradescope too.

>>Any bugs or issues you could not resolve:
There are no bugs that I could not resolve in the code.

>>An example of a difficult issue or bug and how you resolved:
I didnt face any difficult issue in my code but I tried doing "help" extension along with the other 3 extensions, to do that I had to redo what I did so it is little difficult but I am just submitting the other 3 extensions which I initially implemented.

>>A list of the three extensions you’ve chosen to implement, with appropriate detail on them for the CAs to evaluate them (i.e., what are the new verbs/features, how do you exercise them, where are they in the map)
The three extensions I have chosen are:
1)DROP
2)Winning/losing
3)A new Verb- Abracadabra (like an example given in Interactions)

1.DROP: 
The drop verb is the opposite of get, and you can only drop if you have some inventory. If you have something, it will be dropped into the room meaning it will be added to room's items and it will be removed from the inventory.

2.Winning/losing condition: 
I have a room called Black room in the map,if you enter that room with wand or potion you will win the game otherwise you will lose the game.
I have introduced an attribute in the map for a room which is "items_person_should_have" as a list and the list has some items.
If a person enters a room and it has this items_person_should_have list, I will check the inventory of person if he has any of the items that matches things in items_person_should_have , then they will win otherwise they lose.
for example:
{"name": "A black room",
  "desc": "You are in shady room with bright black walls.",
  "exits": { "south": 5, "west": 2 },
  "items": ["magicbook"],
  "items_player_should_have":["wand","potion"]
 }
  
 

3.Abracadabra verb: 
I have introduced a new attribute for one of the room in the map as old_lady which is a list and has some items in that.
If a person enters that room which has old_lady , command prompt will prompt us asking to use abracadabra to get a surprise item which may help in winning the game. The abracadabra verb will randomly chose one item from the old_lady list and add that to person's inventory.
for example:
{"name": "A white room", 
  "desc": "This room is simple, too, but with white walls.",
  "exits": { "west": 0, "south": 4 },
  "items": ["bat"],
  "old_lady":["wand","potion","invisible_cloak"]
 }







