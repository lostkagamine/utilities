# The random string generator, modulified. (c) ry00001/ry00000 2017
import random, string
def genstring(s, e):
    a = ""
    for i in range(s, e):
        a = a + random.choice(string.ascii_letters)
    return a
