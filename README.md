# Achieve Dramatic Printing!
---
Hello! This is a class that would provide a `print()` function (weird, huh) that would add extra delay after each character printed!
To use this as the normal print, simply override it like this:
```python
from dramaprint import Dramaprint # import the dramaprint object
printObj = Dramaprint()
print = printObj.print # strange, huh
print('Hello, World!') # now it would output it slowly
printObj.setDelay(0.02) # you can also change the delay
print('Hello Again!') # now it would output much faster!
```
Play around with it!
I found it quite useful in my projects  
Hope you'll have fun!

### Enjoy :)
