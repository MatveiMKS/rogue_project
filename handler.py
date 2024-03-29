''' Handler module for the game.'''

import Coord
import Creature as cr
import theGame
from visuel import interact

def heal(creature, strength):
    """Heal the creature by strength points"""
    new_hp = creature.hp + strength
    if new_hp > creature.hp_max:
        creature.hp = creature.hp_max
        theGame.theGame().addMessage(f"The {creature.name} is fully healed")
    else:
        creature.hp += strength
        theGame.theGame().addMessage(f"The {creature.name} is healed for {strength} points")
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

def shoot(hero, power, damage, direction):
    """Shoots a projectile at the creature"""
    for i in range(1, power+1):
        pos = throw(direction, i, theGame.theGame()._floor.pos(hero))
        print(pos)
        if pos in theGame.theGame()._floor:
            obj = theGame.theGame()._floor.get(pos)
            if isinstance(obj, cr.Creature):
                obj.hp -= damage
                theGame.theGame().addMessage(f"The {hero.name} shoots the {obj.description()} for {str(damage)} damage")
                death = obj.isDead()
                if death:
                    hero.xp += obj.strength * 2
                    hero.level_up()
                return True

def askDirection(layout):
    """Ask the user for a direction"""
    directions = {'z' if layout == 'f' else 'w': Coord.Coord(0, -1),
                  'q' if layout == 'f' else 'a': Coord.Coord(-1, 0),
                  's': Coord.Coord(0, 1),
                  'd': Coord.Coord(1, 0)}

    direction = None
    while direction not in directions:
        print("Which direction? (direction keys)")
        direction = interact()
        print(direction)
    return directions[direction]
