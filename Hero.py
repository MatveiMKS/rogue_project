''' Contains hero class'''

from Coord import Coord
from Creature import Creature
from Equipment import Equipment
#from Map import Map
import theGame
import random

class Hero(Creature):
    """The hero of the game.
        Is a creature. Has an inventory of elements. """

    armory = {'leather helmet' : ['head', 1], 'leather chest' : ['chest', 2], 'leather legs' : ['legs', 2], 'leather boots' : ['boots', 1],
             'iron helmet' : ['head', 2], 'iron chest' : ['chest', 4], 'iron legs' : ['legs', 4], 'iron boots' : ['boots', 2],
             'steel helmet' : ['head', 3], 'steel chest' : ['chest', 6], 'steel legs' : ['legs', 6], 'steel boots' : ['boots', 3]}

    weapons = {'barehands': 2,'dagger': 3, 'axe': 4, 'sword': 5, 'longsword': 6, 'greatsword': 7,}

    def __init__(self, name="Hero", hp=10, abbrv="@", strength=2):
        Creature.__init__(self, name, hp, abbrv, strength)
        self._inventory = []
        self.armor = 0
        self.armors = {'head' : ['head', 0],
                       'chest' : ['chest', 0],
                       'legs' : ['chest', 0],
                       'boots' : ['boots', 0],}
        self.xp = 0
        self.level = 1
        self.hp_max = 10
        self.money = 0
        self.equipments = 'barehands'
        self.sens = 'z'

    def gain_money(self, amount, elem):
        ''' adds money to hero'''
        self.money += amount
        self._inventory.remove(elem)

    def level_up(self):
        ''' checks if hero can level up and does so'''
        if self.xp >= self.level * 10:
            self.level += 1
            self.xp = 0
            self.hp_max += 2
            self.hp += 2
            theGame.theGame().addMessage(f"The {self.name} levels up to level {self.level}")
            return True
        return False

    def description(self):
        """Description of the hero"""
        return Creature.description(self) + str(self._inventory) + f' Equipiments: {str(self.equipments)}' + f' Armor: {str(self.armor)}'
    
    def is_full(self):
        ''' checks if inventory is full'''
        inv_size = self.level * 2 if self.level * 2 < 10 else 10
        if len(self._inventory) >= inv_size:
            return True
        return False

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
        if self.is_full():
            raise ValueError('Inventory is full')
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

    def drop(self,elem):
        """Drops a piece of equipment"""
        self.checkEquipment(elem)
        if elem not in self._inventory:
            raise ValueError('Equipment ' + elem.name + 'not in inventory')
        self._inventory.remove(elem)

        hero_pos = theGame.theGame()._floor.pos(self)
        for direction in [Coord(0,1), Coord(0,-1), Coord(1,0), Coord(-1,0)]:
            if theGame.theGame()._floor.is_ground(hero_pos + direction):
                theGame.theGame()._floor.put(hero_pos + direction, elem)
                return
        return

    def meet(self, other):
        """The creature is encountered by an other creature.
            The other one hits the creature. Return True if the creature is dead."""
        damage = other.strength - self.armor
        crit = random.randint(1, 10)
        if damage > 0:
            self.hp -= damage if crit != 10 else damage * 2
            if crit == 10:
                theGame.theGame().addMessage(f"The {other.name} lands a critical hit on the {self.name}")
            theGame.theGame().addMessage(f"The {other.name} hits the {self.name}"
                                         f"for {damage if crit != 10 else damage*2} damage")
        else:
            if crit == 10:
                theGame.theGame().addMessage(f"The {other.name} pierces through the {self.name}'s armor"
                                             f"The {other.name} hits the {self.name} "
                                             f"for {str(other.strength)} damage")
                self.hp -= other.strength
            else:
                theGame.theGame().addMessage(f"The {self.description()} blocks the {other.name}'s attack")
        if self.hp > 0:
            return False
        return True
