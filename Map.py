''' Map module'''

from Coord import Coord
from Hero import Hero
from Room import Room
from Element import Element
from Creature import Creature
from utils import sign, min_cost

import random

class Map():
    """A map of a game floor.
        Contains game elements."""

    ground = '.'  # A walkable ground cell
    # four direction user keys
    dir = {'z': Coord(0, -1),
           's': Coord(0, 1),
           'd': Coord(1, 0),
           'q': Coord(-1, 0)}  
    empty = ' '  # A non walkable cell

    def __init__(self, size=15, hero=None):
        self._mat = []
        self._elem = {}
        self._rooms = []
        self._roomsToReach = []

        for _ in range(size):
            self._mat.append([Map.empty] * size)
        if hero is None:
            hero = Hero()
        self._hero = hero
        self.generateRooms(7)
        self.reachAllRooms()
        self.put(self._rooms[0].center(), hero)
        for r in self._rooms:
            r.decorate(self)

    def addRoom(self, room):
        """Adds a room in the map."""
        self._roomsToReach.append(room)
        for y in range(room.c1.y, room.c2.y + 1):
            for x in range(room.c1.x, room.c2.x + 1):
                self._mat[y][x] = Map.ground

    def findRoom(self, coord):
        """If the coord belongs to a room, returns the room elsewhere returns None"""
        for r in self._roomsToReach:
            if coord in r:
                return r
        return None

    def intersectNone(self, room):
        """Tests if the room shall intersect any room already in the map."""
        for r in self._roomsToReach:
            if room.intersect(r):
                return False
        return True

    def dig(self, coord):
        """Puts a ground cell at the given coord.
            If the coord corresponds to a room, considers the room reached."""
        self._mat[coord.y][coord.x] = Map.ground
        r = self.findRoom(coord)
        if r:
            self._roomsToReach.remove(r)
            self._rooms.append(r)

    def corridor(self, cursor, end):
        """Digs a corridors from cursor to end, 
        first vertically, then horizontally."""
        d = end - cursor
        self.dig(cursor)
        while cursor.y != end.y:
            cursor = cursor + Coord(0, sign(d.y))
            self.dig(cursor)
        while cursor.x != end.x:
            cursor = cursor + Coord(sign(d.x), 0)
            self.dig(cursor)

    def reach(self):
        """Makes more rooms reachable.
            Start from one random reached room, and dig a corridor to an unreached room."""
        roomA = random.choice(self._rooms)
        roomB = random.choice(self._roomsToReach)

        self.corridor(roomA.center(), roomB.center())

    def reachAllRooms(self):
        """Makes all rooms reachable.
            Start from the first room, repeats @reach until all rooms are reached."""
        self._rooms.append(self._roomsToReach.pop(0))
        while len(self._roomsToReach) > 0:
            self.reach()

    def randRoom(self) -> Room:
        """A random room to be put on the map."""
        c1 = Coord(random.randint(0, len(self) - 3), random.randint(0, len(self) - 3))
        c2 = Coord(min(c1.x + random.randint(3, 8), len(self) - 1),
                   min(c1.y + random.randint(3, 8), len(self) - 1))
        return Room(c1, c2)

    def generateRooms(self, amount):
        """Generates rooms and adds them if non-intersecting."""
        for _ in range(amount):
            room = self.randRoom()
            if self.intersectNone(room):
                self.addRoom(room)

    def __len__(self):
        return len(self._mat)

    def __contains__(self, item):
        ''' Checks if an item is in the map.
            If the item is a Coord, checks if the coord are in the map.'''
        if isinstance(item, Coord):
            return 0 <= item.x < len(self) and 0 <= item.y < len(self)
        return item in self._elem

    def __repr__(self):
        res = ""
        for lignes in self._mat:
            for colonnes in lignes:
                res += str(colonnes)
            res += '\n'
        return res

    def checkCoord(self, coord):
        """Check if the coordinates coord is valid in the map."""
        if not isinstance(coord, Coord):
            raise TypeError('Not a Coord')
        if not coord in self:
            raise IndexError('Out of map coord')

    def checkElement(self, elem):
        """Check if elem is an Element."""
        if not isinstance(elem, Element):
            raise TypeError('Not a Element')

    def put(self, coord, elem):
        """Puts an element elem at the coordinates coord."""
        self.checkCoord(coord)
        self.checkElement(elem)
        if self._mat[coord.y][coord.x] != Map.ground:
            raise ValueError('Incorrect cell')
        if elem in self._elem:
            raise KeyError('Already placed')
        self._mat[coord.y][coord.x] = elem
        self._elem[elem] = coord

    def get(self, coord):
        """Returns the object at the coordinates coord"""
        self.checkCoord(coord)
        return self._mat[coord.y][coord.x]

    def pos(self, elem):
        """Returns the coordinates of an element in the map """
        self.checkElement(elem)
        return self._elem[elem]

    def rm(self, coord):
        """Removes the element at the coordinates c"""
        self.checkCoord(coord)
        del self._elem[self._mat[coord.y][coord.x]]
        self._mat[coord.y][coord.x] = Map.ground

    def move(self, elem, way):
        """Moves the element e in the direction way."""
        orig = self.pos(elem)
        dest = orig + way
        if dest in self:
            if self.get(dest) == Map.ground:
                self._mat[orig.y][orig.x] = Map.ground
                self._mat[dest.y][dest.x] = elem
                self._elem[elem] = dest
            elif self.get(dest) != Map.empty and self.get(dest).meet(elem) and self.get(dest) != self._hero:
                self.rm(dest)

    def find_path(self, elem):
        """Find a path from a monster to the hero."""
        opened = {self.pos(elem): (0, self.pos(elem).distance(self.pos(self._hero)))}
        closed = {}
        current = self.pos(elem)

        while current != self.pos(self._hero):
            print(current)
            current = min_cost(opened)
            closed[current] = opened[current]
            del opened[current]
            
            if self.get(current) == self._hero:
                break

            for way in [Coord(0, 1), Coord(0, -1), Coord(1, 0), Coord(-1, 0)]:
                next_place = current + way # next cell to be checked

                next_cost_org = closed[current] + 1  # cost of the next cell
                next_cost_end = next_place.distance(self.pos(self._hero)) # heuristic cost of the next cell

                next_cost = next_cost_org + next_cost_end # total cost of the next cell

                if next_place in self and self.get(next_place) == Map.ground and not next_place in closed:
                    if not next_place in opened or opened[next_place][0] + opened[next_place][1] > next_cost:
                        cost_org = next_cost_org
                        cost_end = next_cost_end
                        current = next_place
                        opened[current] = (cost_org, cost_end)

    def moveAllMonsters(self):
        """Moves all monsters in the map.
            If a monster is at distance lower than 6 from the hero, the monster advances."""
        print(type(self._hero))
        hero_pos = self.pos(self._hero)
        for elem in self._elem:
            elem_pos = self.pos(elem)
            if isinstance(elem, Creature) and elem != self._hero and elem_pos.distance(hero_pos) < 6:
                elem_dir_hero = elem_pos.direction(hero_pos) # direction the monster should go
                if self.get(elem_pos + elem_dir_hero) in [Map.ground, self._hero]:
                    self.move(elem, elem_dir_hero)