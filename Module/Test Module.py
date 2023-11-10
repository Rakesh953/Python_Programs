import NumberPrograms
print(NumberPrograms.prime(3))
print(NumberPrograms.composite(8))

from NumberPrograms import prime as p   #Imported Single Function
print(p(3))

from NumberPrograms import prime as p ,perfect as pr  #Imported Multiple Function
print(pr(28))

import NumberPrograms
print(__name__,'__name__')

import NumberPrograms