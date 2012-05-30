from event.manager import EventManager
from event.hook.keyboard import KeyPressed
from event.hook.mouse import ButtonPressed
from event.hook.mouse import Moved

print "############# TEST EVENT MANAGER  #############"

def test_handler(a):
    print 'Bombs! +',a

e = EventManager()
print "Number of EventHooks in EventManager: %s"%len(e)
assert len(e) == 0
e[KeyPressed] += test_handler
e[KeyPressed] += KeyPressed.fire_blank
e[KeyPressed].fire('Test!')

print

print 'KeyPressed object? %s'%e[KeyPressed]
print 'ButtonPressed did not exist?',e[ButtonPressed]
for hook in e:
    print hook
    print e[hook].handlers

print 

e[KeyPressed].fire('Test!')
e[ButtonPressed].fire('Good morning!')

print 
print "Number of EventHooks in EventManager: %s"%len(e)
assert len(e) == 2
print 'Length of KeyPressed: %s'%len(e[KeyPressed])
assert len(e[KeyPressed]) == 2
print 'Length of ButtonPressed: %s'%len(e[ButtonPressed])
assert len(e[ButtonPressed]) == 2

print 

try: 
    e[ButtonPressed] -= test_handler
except ValueError, ve:
    print "Success caught: %s"%ve

e[KeyPressed] -= test_handler
print 'Length of KeyPressed after removing test_handler: %s'%len(e[KeyPressed])
print e[KeyPressed].handlers

print 

# Unnecessary
e[Moved] = Moved()
print "Number of EventHooks in EventManager: %s"%len(e)
assert len(e) == 3
print 'Content of EventManager:\n'
for hook in e:
    print hook
print "############# FINISHED TEST EVENT MANAGER  #############"