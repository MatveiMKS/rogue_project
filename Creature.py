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

    def description(self):
        """Description of the creature"""
        return f"{Element.description(self)} ({str(self.hp)})"

    def meet(self, other):
        """The creature is encountered by an other creature.
            The other one hits the creature. Return True if the creature is dead."""
        crit = random.randint(0, 10)
        damage = other.strength
        self.hp -= damage if crit != 10 else 0 if crit == 0 else damage * 2
        if crit == 10:
            theGame.theGame().addMessage(f"The {other.name} lands a critical hit on the {self.name}")
            theGame.theGame().addMessage(f"The {other.name} hits the {self.name}"
                                         f" for {damage * 2} damage")
        elif crit == 0:
            theGame.theGame().addMessage(f"The {other.name} misses the {self.name}")
        else:
            theGame.theGame().addMessage(f"The {other.name} hits the {self.name}"
                                         f" for {damage} damage")

        if self.hp > 0:
            if self.name == "Boss":
                # could be replaced by the function teleport in handler but causes circular import
                room = theGame.theGame()._floor.randRoom()
                destination = room.randEmptyCoord(theGame.theGame()._floor)
                theGame.theGame()._floor.rm(theGame.theGame()._floor.pos(self))
                theGame.theGame()._floor.put(destination, self)
            return False
        other.xp += self.strength * 2
        other.level_up()
        return True

    def kill(self):
        """ Insta kill a creature """
        self.hp = 0
        return True

    def isDead(self):
        """Return True if the creature is dead"""
        print('Here')
        if self.hp <= 0:
            theGame.theGame().addMessage("The " + self.name + " is dead")
            theGame.theGame()._floor.rm(theGame.theGame()._floor.pos(self))
            return True
