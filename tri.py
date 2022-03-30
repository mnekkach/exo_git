"""
Exo pour trier des matrices
"""
from operator import *

a = [
("Clement",14, 16),
("Charle", 12, 15),
("Oriane", 14, 18),
("Thomas", 11, 12),
("Damien", 12, 13)
]

print a

"""
tri des tuples de la liste a
"""
print sorted(a)

"""
tri des tuples de la liste a
par rapport à la 3eme colonne
"""
print sorted(a, key = lambda colonnes : colonnes[2])

"""
tri des tuples de la liste a
par rapport à la 3eme colonne
en utilsant itemgetter
"""
print sorted(a, key = itemgetter(2))

"""
tri des tuples de la liste a
par rapport à la 2eme et la 3eme colonne
en utilsant itemgetter
"""
print sorted(a, key = itemgetter(1,2))

#END
