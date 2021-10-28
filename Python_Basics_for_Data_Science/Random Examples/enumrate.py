'''The skills network explains that we can use enumerate in our loops. But doesn't really explain what it does. Let's find out.'''

colors = ['red', 'yellow', 'blue']

for i, color in enumerate(colors): # enumerate returns a pair. One value being the index, the other being the value of said index.
    print(i)
    print(color)