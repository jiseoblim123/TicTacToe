# players = [1, 0]

# choice = 1
# for i in range(10):
#     current_player = choice+1
#     print(current_player)
#     choice = players[choice]







# import itertools

# player_choice = itertools.cycle([1, 2])

# for i in range(10):
#     print(next(player_choice))










# iterable: a thing we can iterate over
# iterator: a special object with next() method.

x = [1, 2, 3, 4] # iterable.

import itertools

n = itertools.cycle(x) # iterator! ...also iterable

y = iter(x) # iterator! ...also iterable

next(y)

for i in y:
    print(i)