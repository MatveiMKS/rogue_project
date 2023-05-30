''' Contains hero class'''

from Creature import Creature
from Equipment import Equipment
import theGame
import random

class Hero(Creature):
    """The hero of the game.
        Is a creature. Has an inventory of elements. """

    armory = {'leather helmet' : ['head', 1], 'leather chest' : ['chest', 2], 'leather legs' : ['legs', 2], 'leather boots' : ['boots', 1],
             'iron helmet' : ['head', 2], 'iron chest' : ['chest', 4], 'iron legs' : ['legs', 4], 'iron boots' : ['boots', 2],
             'steel helmet' : ['head', 3], 'steel chest' : ['chest', 6], 'steel legs' : ['legs', 6], 'steel boots' : ['boots', 3],}

    weapons = {'barehands': 0,'dagger': 3, 'axe': 4, 'sword': 5, 'longsword': 6, 'greatsword': 7,}

    def __init__(self, name="Hero", hp=10, abbrv="@", strength=2):
        Creature.__init__(self, name, hp, abbrv, strength)
        self._inventory = []
        self.armor = 0
        self.armors = {'head' : ['head', 0], 'chest' : ['chest', 0], 'legs' : ['chest', 0], 'boots' : ['boots', 0],}
        self.xp = 0
        self.level = 1

    def description(self):
        """Description of the hero"""
        return Creature.description(self) + str(self._inventory) + f' Equipiments: {str(self.equipments)}' + f' Armor: {str(self.armor)}'

    def fullDescription(self):
        """Complete description of the hero"""
        res = ''
        for e in self.__dict__:
            if e[0] != '_':
                res += '> ' + e + ' : ' + str(self.__dict__[e]) + '\n'
        res += '> INVENTORY : ' + str([x.name for x in self._inventory])
        return res

    def checkEquipment(self, obj):
        """Used to check if an object is a piece of equipment"""
        if not isinstance(obj, Equipment):
            raise TypeError('Not a Equipment')

    def take(self, elem):
        """Adds the equipment to inventory"""
        self.checkEquipment(elem)
        self._inventory.append(elem)

    def equip(self, elem):
        """Equips a piece of equipment"""
        if elem is None:
            return
        self.checkEquipment(elem)
        if elem not in self._inventory:
            raise ValueError('Equipment ' + elem.name + 'not in inventory')
        if elem.name in Hero.weapons:
            self.strength = Hero.weapons[elem.name]
            self.equipments = elem.name
            self._inventory.remove(elem)

    def suit_up(self, elem):
        ''' equips a piece of armor'''
        if elem is None:
            return
        self.checkEquipment(elem)
        if elem not in self._inventory:
            raise ValueError('Equipment ' + elem.name + 'not in inventory')
        if elem.name in Hero.armory:
            new_armor = Hero.armory[elem.name]
            self.armor -= self.armors[new_armor[0]][1] # remove old armor value
            self.armors[new_armor[0]] = new_armor # add new armor
            self.armor += new_armor[1] # add new armor value
            self._inventory.remove(elem)

    def use(self, elem):
        """Uses a piece of equipment"""
        if elem is None:
            return
        self.checkEquipment(elem)
        if elem not in self._inventory:
            raise ValueError('Equipment ' + elem.name + 'not in inventory')
        if elem.use(self):
            self._inventory.remove(elem)
            return
        
    def meet(self, other):
        """The creature is encountered by an other creature.
            The other one hits the creature. Return True if the creature is dead."""
        damage = other.strength - self.armor
        crit = random.randint(1, 10)
        if damage > 0:
            self.hp -= damage if crit != 10 else damage * 2
            if crit == 10:
                theGame.theGame().addMessage(f"The {other.name} lands a critical hit on the {self.description()}")
            theGame.theGame().addMessage(f"The {other.name} hits the {self.description()}"
                                         f"for {damage if crit != 10 else damage*2} damage")
        else:
            if crit == 10:
                theGame.theGame().addMessage(f"The {other.name} pierces through the {self.description()}'s armor"
                                             f"The {other.name} hits the {self.description()} "
                                             f"for {str(other.strength)} damage")
                self.hp -= other.strength
            else:
                theGame.theGame().addMessage(f"The {self.description()} blocks the {other.name}'s attack")
        if self.hp > 0:
            return False
        return True
