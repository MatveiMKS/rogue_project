''' Contains the Equipment class.'''

from Element import Element
import theGame

class Equipment(Element):
    """A piece of equipment"""

    def __init__(self, name, abbrv="", usage=None):
        Element.__init__(self, name, abbrv)
        self.usage = usage

    def meet(self, hero):
        """Called when the hero meets an element."""
        if hero.is_full():
            theGame.theGame().addMessage("Your inventory is full.")
            return False
        hero.take(self)
        theGame.theGame().addMessage("You pick up a " + self.name)
        return True

    def use(self, creature):
        """Uses the piece of equipment. Has effect on the hero according usage.
            Return True if the object is consumed."""
        if self.usage is None:
            theGame.theGame().addMessage("The " + self.name + " is not usable")
            return False
        else:
            theGame.theGame().addMessage("The " + creature.name + " uses the " + self.name)
            return self.usage(self, creature)
