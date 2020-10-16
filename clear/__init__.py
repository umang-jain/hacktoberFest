"""
implements a clear() function to clear the screen
uses the sys and os modules, so no third party modules are needed
"""
from sys import platform
from os import system

def clear():
   cmd = "cls" if platform == "win32" else "clear"
   system(cmd)