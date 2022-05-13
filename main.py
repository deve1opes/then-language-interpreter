from glyphs import *

inputName = input("Input name:")
listedName = list(inputName)
print(listedName)
glyphsTrans(listedName)
print(listedName)

# Monitor len keyword behavior
print(len(listedName))

# This section is to joining the list
s = ''
joined = s.join(listedName)
print(joined)
