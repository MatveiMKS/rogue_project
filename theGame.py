''' Contains the function theGame, which is a singleton of the Game class.'''

from Game import Game

def theGame(game=Game()):
    """Game singleton"""
    return game
