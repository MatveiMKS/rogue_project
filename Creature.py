''' Contains the Creature class, which is a subclass of Element.'''

from Element import Element
import theGame
import random

class Creature(Element):
    """A creature that occupies the dungeon.
        Has hit points and strength."""


    def __init__(self, name, hp, abbrv="", strength=1):
        Element.__init__(self, name, abbrv)
        self.hp = hp
        self.strength = strength
        self.equipments = 'barehands'
        self.xp = 0
        self.level = 0

    def description(self):
        """Description of the creature"""
        return f"{Element.description(self)} ({str(self.hp)})"

    def meet(self, other):
        """The creature is encountered by an other creature.
            The other one hits the creature. Return True if the creature is dead."""
        crit = random.randint(0, 10)
        damage = other.strength
        self.hp -= damage if crit != 10 else (damage * 2) if crit!= 0 else 0
        if crit == 10:
            theGame.theGame().addMessage(f"The {other.name} lands a critical hit on the {self.description()}")
            theGame.theGame().addMessage(f"The {other.name} hits the {self.description()} "
                                     f"for {damage * 2} damage")
        elif crit == 0:
            theGame.theGame().addMessage(f"The {other.name} misses the {self.description()}")
        else:
            theGame.theGame().addMessage(f"The {other.name} hits the {self.description()} "
                                         f"for {damage} damage")
        if self.hp > 0:
            return False
        other.xp += self.strength * 2
        if other.xp >= other.level * 10:
            other.level += 1
            other.xp = 0
            theGame.theGame().addMessage(f"The {other.name} levels up to level {other.level}")
        return True

    def kill(self):
        """ Insta kill a creature """
        self.hp = 0
        return True

    def isDead(self):
        """Return True if the creature is dead"""
        if self.hp <= 0:
            theGame.theGame().addMessage("The " + self.name + " is dead")
            theGame.theGame()._floor.rm(theGame.theGame()._floor.pos(self))
            return True
