Kavyasri Thalluri (kthallur@stevens.edu)

>>URL: https://github.com/kavya2304/text_based_video_game.git

>>An estimate of how many hours you spent on the project: 
20-35 hours

>>A description of how you tested your code: 
I have manually checked , covering all the cases that I wrote meaning all verbs and extensions , writing unit tests for the same and with the gradescope too.

>>Any bugs or issues you could not resolve:
There are no bugs that I could not resolve in the code.

>>An example of a difficult issue or bug and how you resolved:
I didnt face any difficult issue in my code but I tried doing "help" extension along with the other 3 extensions, to do that I had to redo what I did so it is little difficult but I am just submitting the other 3 extensions which I initially implemented.
I also faced issue with autograder spacing and newlines, which took my time.

>>A list of the three extensions you’ve chosen to implement, with appropriate detail on them for the CAs to evaluate them (i.e., what are the new verbs/features, how do you exercise them, where are they in the map)
The three extensions I have chosen are:
1)DROP
2)Winning/losing
3)A new Verb- Abracadabra (like an example given in Interactions)

1.DROP: 
-------
The drop verb is the opposite of get, and you can only drop if you have some inventory. If you have something, it will be dropped into the current room meaning it will be added to room's items and it will be removed from the inventory.
Example:

What would you like to do? go east
You go east.

> A red room

This room is fancy. It's red!

Items: rose

Exits: north west

What would you like to do? get rose
You pick up the rose.
What would you like to do? go west
You go west.

> A white room

You are in a simple room with white walls.

Exits: north east

What would you like to do? drop rose
You drop the rose.
What would you like to do? look
> A white room

You are in a simple room with white walls.

Items: rose

Exits: north east

What would you like to do? drop bat
You're not carrying that.

2.Winning/losing condition: 
--------------------------
I have a room called Black room in the map,if you enter that room with wand or potion you will win the game otherwise you will lose the game.
I have introduced an attribute in the map for a room which is "items_person_should_have" as a list and the list has some items.
If a person enters a room and it has items_person_should_have list, I will check the inventory of person if he has any of the items that matches things in items_person_should_have , then they will win otherwise they lose.
for example:
{"name": "A black room",
  "desc": "You are in shady room with bright black walls.",
  "exits": { "south": 5, "west": 2 },
  "items": ["magicbook"],
  "items_player_should_have":["wand","potion"]
 }

> A white room

This room is simple, too, but with white walls.

Items: bat

Exits: west south

Hey, there is a old-lady in this room who can grant you an item that helps you win the game,to get that say "ABRACADABRA"!!!!!!
What would you like to do? abracadabra
You got potion!!
What would you like to do? abracadabra
You got wand!!
What would you like to do? go south
You go south.

> A green room

This room is simple too, but with green walls.

Items: wand, potion

Exits: east north west

What would you like to do? go north
You go north.

> A red room

This room is fancy. It's red!

Exits: east south

What would you like to do? go east
You go east.

You can do the magic with help of Magicbook here,and escape from this adventure now,Hurrayyy,You Won the game!!

>For losing:

> A white room

This room is simple, too, but with white walls.

Items: bat

Exits: west south

Hey, there is a old-lady in this room who can grant you an item that helps you win the game,to get that say "ABRACADABRA"!!!!!!
What would you like to do? go south
You go south.

> A yellow room

This room is bright. It's yellow!

Items: banana, knife, ball

Exits: east north

What would you like to do? go east
You go east.

> A green room

This room is simple too, but with green walls.

Items: wand, potion

Exits: east north west

What would you like to do? go east
You go east.

You entered wrong room without needed items and the Witch killed you.You lost the game!!!
 

3.Abracadabra verb: 
-------------------
I have introduced a new attribute for one of the room in the map as old_lady which is a list and has some items in that.
If a person enters that room which has old_lady , command prompt will prompt us asking to use abracadabra to get a surprise item which may help in winning the game. The abracadabra verb will randomly chose one item from the old_lady list and add that to person's inventory.
for example:
{"name": "A white room", 
  "desc": "This room is simple, too, but with white walls.",
  "exits": { "west": 0, "south": 4 },
  "items": ["bat"],
  "old_lady":["wand","potion","invisible_cloak"]
 }

Example:
> A blue room

You are in a simple room with blue walls.

Items: apple

Exits: east

What would you like to do? go east
You go east.

> A white room

This room is simple, too, but with white walls.

Items: bat

Exits: west south

Hey, there is a old-lady in this room who can grant you an item that helps you win the game,to get that say "ABRACADABRA"!!!!!!
What would you like to do? abracadabra
You got potion!!
What would you like to do?





