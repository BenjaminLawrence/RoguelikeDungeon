from entity import Entity

# Creation of Player Character
player = Entity(char="@", color=(255, 255, 255), name="Player", blocks_movement=True)

# Creation of Enemies
orc = Entity(char="o", color=(63, 127, 63), name="Orc", blocks_movement=True)
troll = Entity(char="T", color=(0, 127, 0), name="Troll", block_movement=True)
