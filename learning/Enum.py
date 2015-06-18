#### ways to simulate an enum

### approach 1: use class
class Seasons:
    Spring = 0
    Summer = 1
    Autumn = 2
    Winter = 3

print(Seasons.Spring)
print(Seasons.Summer)
print(Seasons.Autumn)
print(Seasons.Winter)

### approach 2: use function
def enum(*posargs, **keysarg):
    return type("Enum", (object,), dict(zip(posargs, xrange(len(posargs))), **keysarg))

Seasons2 = enum("Spring", "Summer", "Autumn", Winter=1)
print(Seasons2.Spring)

import collections
### approach 3: collections.namedtuple
Seasons3 = collections.namedtuple("Seasons3", "Spring Summer Autumn Winter")._make(range(4))
print(Seasons3.Spring)

