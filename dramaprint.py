import sys
import time

class Dramaprint:
    """The class for dramatic printing"""
  
    def __init__(self, delay=0.05): # default delay is 0.05
        self.delay = delay

    def setDelay(self, delay):
        # sets self.delay to argument `delay`
        self.delay = delay

    def print(self, *args, sep=' ', end='\n', soundPath=None):
        """
        Dramatically prints text to the console, like print() but slower & cooler.
        
        Parameters:
            args        — multiple strings or values to print
            sep         — separator between arguments (default: space)
            end         — what to print at the end (default: newline)
            soundPath   — a string pointing to a path to a sound you would like to play after a character is typed (default: None)
        
        Also the delay is set on creating object or by setDelay
        """

        output = sep.join(str(arg) for arg in args) + end
        for char in output:
            sys.stdout.write(char)
            sys.stdout.flush() # flush immediately to terminal
            time.sleep(self.delay) # apply delay
            if soundPath: # TODO: Not Completed

# Example use:
# Umcomment for testing:
# printObj = Dramaprint()
# print = printObj.print
# print('Hello World!')
# printObj.setDelay(0.1) 
# print('Hello Again!')    Now the output should be slower
