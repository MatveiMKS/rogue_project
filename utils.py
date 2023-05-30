def _find_getch():
   """Single char input, only works only on mac/linux/windows OS terminals"""
   try:
       import termios
   except ImportError:
       # Non-POSIX. Return msvcrt's (Windows') getch.
       import msvcrt
       return lambda: msvcrt.getch().decode('utf-8')
   # POSIX system. Create and return a getch that manipulates the tty.
   import sys, tty
   def _getch():
       fd = sys.stdin.fileno()
       old_settings = termios.tcgetattr(fd)
       try:
           tty.setraw(fd)
           ch = sys.stdin.read(1)
       finally:
           termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
       return ch
   return _getch

def getch2():
    '''Single char input, only works only on mac/linux/windows OS terminals'''
    try:
        import termios
        # POSIX system. Create and return a getch that manipulates the tty.
        import sys, tty
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    except ImportError:
        # Non-POSIX. Return msvcrt's (Windows') getch.
        import msvcrt
        return msvcrt.getch().decode('utf-8')

def sign(x):
    if x > 0:
        return 1
    return -1

def min_cost(dico):
    """Returns the element with the lowest cost"""
    cle_mini = list(dico.keys())[0]
    mini = dico[cle_mini]
    for el in dico:
        if dico[el][0] + dico[el][1] < mini[0] + mini[1]:
            cle_mini = el
    return cle_mini
