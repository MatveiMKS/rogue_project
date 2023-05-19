''' Game module'''

import random, copy

from Equipment import Equipment
from Creature import Creature
from Coord import Coord
from Hero import Hero
from Map import Map
from Stairs import Stairs
from handler import heal, teleport, throw
from utils import getch2
import theGame

class Game(object):
    """ Class representing game state """

    # available equipments w/ their probabilities and actions / effects
    # the key is the probability of the equipment to appear (higher key = lower probability)
    equipments = {0: [Equipment("potion", "!", usage=lambda self, hero: heal(hero))],
                  1 : [Equipment("gold", "o")],
                  2: [Equipment("bow", usage=lambda self, hero: throw(1, True))],
                  3: [Equipment("portoloin", "w", usage=lambda self, hero: teleport(hero, False))]
                  }

    monsters = {0: [Creature("Goblin", 4), Creature("Bat", 2, "W")],
                1: [Creature("Ork", 6, strength=2), Creature("Blob", 10)],
                5: [Creature("Dragon", 20, strength=3)]}

    #available actions w/ their key
    _actions = { 'z': lambda h: theGame.theGame()._floor.move(h, Coord(0, -1)),
                'q': lambda h: theGame.theGame()._floor.move(h, Coord(-1, 0)),
                's': lambda h: theGame.theGame()._floor.move(h, Coord(0, 1)),
                'd': lambda h: theGame.theGame()._floor.move(h, Coord(1, 0)),
                'i': lambda h: theGame.theGame().addMessage(h.fullDescription()),
                'k': lambda h: h.kill(),
                'u': lambda h: h.use(theGame.theGame().select(h._inventory)),
                ' ': lambda h: None,
                'h': lambda hero: theGame.theGame().addMessage("Available actions : " + str(list(Game._actions.keys()))),
                'b': lambda hero: theGame.theGame().addMessage("I am " + hero.name)
                }

    def __init__(self, level=1, hero=None):
        self._level = level
        self._messages = []
        self._hero = hero if hero else Hero()
        # if hero == None:
        #     hero = Hero()
        # self._hero = hero
        # check here if problem w/ hero
        self._floor = None

    def buildFloor(self):
        """Creates a map for the current floor."""
        self._floor = Map(hero=self._hero)
        self._floor.put(self._floor._rooms[-1].center(), Stairs())
        self._level += 1

    def addMessage(self, msg):
        """Adds a message in the message list."""
        self._messages.append(msg)

    def readMessages(self):
        """Returns the message list and clears it."""
        s = ''
        for m in self._messages:
            s += m + '. '
        self._messages.clear()
        return s

    def randElement(self, collect):
        """Returns a clone of random element from a collection using exponential random law."""
        var_exp = random.expovariate(1 / self._level)
        for rarity in collect:
            if rarity <= var_exp:
                items = collect[rarity]
        return copy.copy(random.choice(items))

    def randEquipment(self):
        """Returns a random equipment."""
        return self.randElement(Game.equipments)

    def randMonster(self):
        """Returns a random monster."""
        return self.randElement(Game.monsters)

    def select(self, inventory):
        ''' Select an item from an inventory'''
        print("Choose item> " + str([str(inventory.index(item)) + ": " + item.name for item in inventory]))
        key_press = getch2()
        if key_press.isdigit() and int(key_press) in range(len(inventory)):
            return inventory[int(key_press)]

    def play(self):
        """Main game loop"""
        self.buildFloor()
        print("--- Welcome Hero! ---")
        while self._hero.hp > 0:
            print()
            print(self._floor)
            print(self._hero.description())
            print(self.readMessages())
            key_press = getch2()
            print(key_press in Game._actions)
            if key_press in Game._actions:
                Game._actions[key_press](self._hero)
            self._floor.moveAllMonsters()
        print("--- Game Over ---")
