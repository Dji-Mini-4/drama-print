import sys, time, os
try:
    from playsound import playsound
    moduleExist = True
except ImportError:
    moduleExist = False
    
class Dramaprint:
    """The class for dramatic printing"""
  
    def __init__(self, delay=0.05): # default delay is 0.05
        self.delay = delay

    def setDelay(self, delay):
        # sets self.delay to argument `delay`
        self.delay = delay
        
    def playSound(self, soundPath):
        try:
            playsound(soundPath)
        except Exception as e:
            print('Runtime error occured when playing sound:')
            print(f'\033[1m{type(e).__name__}: {e}\033[0m')
            print('Please try again')
            sys.exit()
            
    def print(self, *args, sep=' ', end='\n', soundPath=None, soundPerLine=False):
        """
        Dramatically prints text to the console, like print() but slower & cooler.
        
        Parameters:
            *args                — multiple strings or values to print
            sep: str             — separator between arguments (default: space)
            end: str             — what to print at the end (default: newline)
            soundPath: str       — a string pointing to a path to a sound you would like to play after a character is typed (default: None)
            soundPerLine: bool   — a boolean; (would not make difference if soundPath is not provided) if False then sound plays after each char; if True then after each line. (defauld: False)
        Also the delay is set on creating object or by setDelay
        """
        sound = False
        # Enable sound playing if soundPath is provided
        if soundPath:
            if not os.path.isfile(soundPath):
                print('The file \033[1mdoesn\'t exist!\033[0m Try again :)')
                sys.exit()
            elif not moduleExist:
                print('You wanted to play sound, but the playsound module \033[1mdoesn\'t exist!\033[0m Try again :)')
                sys.exit()
            else:
                sound = True

        lines = (sep.join(str(arg) for arg in args) + end).splitlines(keepends=True)
        for line in lines:
            for char in line:
                sys.stdout.write(char)
                sys.stdout.flush() # flush immediately to terminal
                time.sleep(self.delay) # apply delay
                if sound and not soundPerLine:
                    self.playSound(soundPath)
            if sound and soundPerLine:
                # play it since it's a newline
                self.playSound(soundPath)
                
# Example use:
# Umcomment for testing:
# printObj = Dramaprint()
# print = printObj.print
# print('Hello World!')
# printObj.setDelay(0.1) 
# print('Hello Again!')    Now the output should be slower
