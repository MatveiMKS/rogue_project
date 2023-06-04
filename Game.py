''' Game module'''

import random, copy

from Equipment import Equipment
from Creature import Creature
from Coord import Coord
from Hero import Hero
from Map import Map
from Stairs import Stairs
from handler import heal, teleport, shoot, askDirection
from const import elem_type
import theGame
import visuel
import pygame 


class Game():
    """ Class representing game state """

    # available equipments w/ their probabilities and actions / effects
    # the key is the probability of the equipment to appear (higher key = lower probability)
    equipments = {0: [Equipment("small potion", "!", usage=lambda self, hero: heal(hero, 3)),
                      Equipment("dagger", usage=lambda self, hero: hero.equip(self)),
                      Equipment("throwing knife", usage=lambda self, hero: shoot(hero, 4, 4, askDirection(theGame.theGame().layout))),
                      Equipment("gold", "o", usage=lambda self, hero: hero.gain_money(5, self))
                      ],

                  1: [
                      Equipment("sword", usage=lambda self, hero: hero.equip(self)),
                      Equipment("axe", usage=lambda self, hero: hero.equip(self))
                      ] + [Equipment(armor, usage=lambda self, hero: hero.suit_up(self)) for armor in Hero.armory],

                  2: [Equipment("medium potion", "?", usage=lambda self, hero: heal(hero, 5)),
                      Equipment("longsword", "L", usage=lambda self, hero: hero.equip(self))
                      ],

                  3: [Equipment("portoloin", "w", usage=lambda self, hero: teleport(hero, True)),
                      Equipment("big potion", "%", usage=lambda self, hero: heal(hero, 10))
                      ],
                  }

    monsters = {0: [Creature("Weak Goblin", 4, 'G'),
                    Creature("Weak Bat", 2, "W")],

                1: [Creature("Weak Ork", 6, 'O', strength=2),
                    Creature("Weak Blob", 10, 'B')],

                5: [Creature("Weak Dragon", 20, 'D', strength=3)]}

    mid_monsters = {0: [Creature("Goblin", 6, 'G', strength=2),
                        Creature("Bat", 3, "W")],

                    1: [Creature("Ork", 9, 'O', strength=3),
                        Creature("Blob", 15, 'B', strength=2)],

                    5: [Creature("Dragon", 30, 'D', strength=5)]}

    strong_monsters = {0: [Creature("Strong Goblin", 9, 'G', strength=3),
                           Creature("Strong Bat", 5, "W", strength=2)],

                        1: [Creature("Strong Ork", 13, 'O', strength=4),
                        Creature("Strong Blob", 20, 'B', strength=3)],

                        5: [Creature("Strong Dragon", 35, 'D', strength=8)]}

    #available actions w/ their key
    _actions = { 'z': lambda h: theGame.theGame()._floor.move(h, Coord(0, -1)),
                'q': lambda h: theGame.theGame()._floor.move(h, Coord(-1, 0)),
                's': lambda h: theGame.theGame()._floor.move(h, Coord(0, 1)),
                'd': lambda h: theGame.theGame()._floor.move(h, Coord(1, 0)),
                'a' : lambda h: theGame.theGame()._floor.move(h, Coord(-1,-1)), 
                'e' : lambda h: theGame.theGame()._floor.move(h, Coord(1,-1)),
                'x' : lambda h: theGame.theGame()._floor.move(h, Coord(1,1)), 
                'w' : lambda h: theGame.theGame()._floor.move(h, Coord(-1,1)),
                'i': lambda h: theGame.theGame().addMessage(h.fullDescription()),
                'k': lambda h: h.kill(),
                'u': lambda h: h.use(theGame.theGame().select(h._inventory)),
                ' ': lambda h: None,
                'h': lambda hero: theGame.theGame().addMessage("Available actions : " + str(list(Game._actions.keys()))),
                'b': lambda hero: theGame.theGame().addMessage("I am " + hero.name),
                'r': lambda h: h.drop(theGame.theGame().select(h._inventory))
                }

    _actions_wasd = { 'w': lambda h: theGame.theGame()._floor.move(h, Coord(0, -1)),
                    'a': lambda h: theGame.theGame()._floor.move(h, Coord(-1, 0)),
                    's': lambda h: theGame.theGame()._floor.move(h, Coord(0, 1)),
                    'd': lambda h: theGame.theGame()._floor.move(h, Coord(1, 0)),
                    'q' : lambda h: theGame.theGame()._floor.move(h, Coord(-1,-1)), 
                    'e' : lambda h: theGame.theGame()._floor.move(h, Coord(1,-1)),
                    'x' : lambda h: theGame.theGame()._floor.move(h, Coord(1,1)), 
                    'z' : lambda h: theGame.theGame()._floor.move(h, Coord(-1,1)),
                    'i': lambda h: theGame.theGame().addMessage(h.fullDescription()),
                    'k': lambda h: h.kill(),
                    'u': lambda h: h.use(theGame.theGame().select(h._inventory)),
                    ' ': lambda h: None,
                    'h': lambda hero: theGame.theGame().addMessage("Available actions : " + str(list(Game._actions_wasd.keys()))),
                    'b': lambda hero: theGame.theGame().addMessage("I am " + hero.name),
                    'r': lambda h: h.drop(theGame.theGame().select(h._inventory))
                    }
    _actions_wasd.update({
                        '0' : lambda h: h.use(h._inventory[0]) if len(h._inventory) > 0 else None,
                        '1' : lambda h: h.use(h._inventory[1]) if len(h._inventory) > 1 else None,
                        '2' : lambda h: h.use(h._inventory[2]) if len(h._inventory) > 2 else None,
                        '3' : lambda h: h.use(h._inventory[3]) if len(h._inventory) > 3 else None,
                        '4' : lambda h: h.use(h._inventory[4]) if len(h._inventory) > 4 else None,
                        '5' : lambda h: h.use(h._inventory[5]) if len(h._inventory) > 5 else None,
                        '6' : lambda h: h.use(h._inventory[6]) if len(h._inventory) > 6 else None,
                        '7' : lambda h: h.use(h._inventory[7]) if len(h._inventory) > 7 else None,
                        '8' : lambda h: h.use(h._inventory[8]) if len(h._inventory) > 8 else None,
                        '9' : lambda h: h.use(h._inventory[9]) if len(h._inventory) > 9 else None,
                    })
    
    def __init__(self, level=1, hero=None):
        self._level = level
        self._messages = []
        self._hero = hero if hero else Hero()
        self._floor = None
        self.layout = 'f'

    def change_layout(self):
        ''' Changes the layout'''
        layout = '0'
        while layout not in ['1' , '2']:
            self.addMessage("Choose your layout : 1 for AZERTY, 2 for QWERTY")
            layout = visuel.interact()
        if layout == '1':
            self.layout = 'f'
        else:
            self.layout = 'w'

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
            s += m + '. \n'
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
        return self.randElement(Game.monsters if self._level < 3
                                else Game.mid_monsters if self._level < 6
                                else Game.strong_monsters)

    def select(self, inventory):
        ''' Select an item from an inventory'''
        print("Choose item> " + str([str(inventory.index(item)) + ": " + item.name for item in inventory]))
        key_press = visuel.interact()
        if key_press.isdigit() and int(key_press) in range(len(inventory)):
            return inventory[int(key_press)]

    def play(self):
        running = True
        window, background = visuel.initialisation()
        self.change_layout()
        layout = self.layout
        if layout == 'f':
            actions = Game._actions
        else:
            actions = Game._actions_wasd
        """Main game loop"""
        self.buildFloor()
        visuel.afficher(self._floor, background, self._hero, elem_type)
        running = visuel.refresh(window, background)
        print("--- Welcome Hero! ---")

        level = 2
        print(self._level)
        sens = 'z' if layout == 'f' else 'w'
        while self._hero.hp > 0 and running:
            
            pygame.time.Clock().tick(60)
            pygame.display.flip()
            self._hero.sens = sens
            visuel.afficher(self._floor, background, self._hero, elem_type)
            running = visuel.refresh(window, background)
            if level != self._level:
                window, background = visuel.initialisation()
                visuel.afficher(self._floor, background, self._hero, elem_type)
                running = visuel.refresh(window, background)
                level += 1
            print()
            print(self._floor)
            print(self._hero.description())
            print(self.readMessages())
            key_press = visuel.interact()
            if key_press in actions:
                actions[key_press](self._hero)
            sens = key_press
            self._floor.moveAllMonsters()
        print("--- Game Over ---")
        