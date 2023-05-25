'''Module to creatre a room.'''

import random

from Coord import Coord
import Map as mp
import theGame

class Room():
    """A rectangular room in the map"""

    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

    def __repr__(self):
        return "[" + str(self.c1) + ", " + str(self.c2) + "]"

    def __contains__(self, coord):
        return self.c1.x <= coord.x <= self.c2.x and self.c1.y <= coord.y <= self.c2.y

    def intersect(self, other):
        """Test if the room has an intersection with another room"""
        sc3 = Coord(self.c2.x, self.c1.y)
        sc4 = Coord(self.c1.x, self.c2.y)
        return self.c1 in other or self.c2 in other or sc3 in other or sc4 in other or other.c1 in self

    def center(self):
        """Returns the coordinates of the room center"""
        return Coord((self.c1.x + self.c2.x) // 2, (self.c1.y + self.c2.y) // 2)

    def randCoord(self):
        '''Returns a random position in the room.'''
        pos_x = random.randint(min(self.c1.x, self.c2.x), max(self.c1.x, self.c2.x))
        pos_y = random.randint(min(self.c1.y, self.c2.y), max(self.c1.y, self.c2.y))
        return Coord(pos_x, pos_y)

    def randEmptyCoord(self, map):
        """A random coordinate inside the room which is free on the map."""
        coord = self.randCoord()
        while map.get(coord) != mp.Map.ground or coord == self.center():
            coord = self.randCoord()
        return coord

    def decorate(self, map):
        """Decorates the room by adding a random equipment and monster."""
        map.put(self.randEmptyCoord(map), theGame.theGame().randEquipment())
        map.put(self.randEmptyCoord(map), theGame.theGame().randMonster())