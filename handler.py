''' Handler module for the game.'''

import theGame

def heal(creature, strength):
    """Heal the creature by strength points"""
    creature.hp += strength
    return True

def teleport(creature, unique):
    """Teleport the creature"""
    room = theGame.theGame()._floor.randRoom()
    destination = room.randEmptyCoord(theGame.theGame()._floor)
    theGame.theGame()._floor.rm(theGame.theGame()._floor.pos(creature))
    theGame.theGame()._floor.put(destination, creature)
    return unique

def throw(power, loss):
    """Throw an object"""
    pass