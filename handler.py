''' Handler module for the game.'''

import Coord
import Creature as cr
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

def throw(direction, power, start_pos):
    """Returns the position of the thrown object"""
    pos_x = start_pos.x + direction.x * power
    pos_y = start_pos.y + direction.y * power
    pos = Coord.Coord(pos_x, pos_y)
    return pos

def shoot(hero, direction, power, damage):
    """Shoots a projectile at the creature"""
    for i in range(power):
        pos = throw(direction, i, theGame.theGame()._floor.pos(hero))
        if isinstance(theGame.theGame()._floor.get(pos), cr.Creature)):
            theGame.theGame()._floor.get(pos).hp -= damage
            return True