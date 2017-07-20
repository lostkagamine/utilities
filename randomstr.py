import random, string, sys
a = ""
start = sys.argv[1] if len(sys.argv) >= 2 else 100
end = sys.argv[2] if len(sys.argv) >= 3 else 1000
try:
    for i in range(random.randint(int(start),int(end))):
        a = a + random.choice(string.ascii_letters)
except ValueError:
    print("Oops, you made an oopsie with the arguments. Try again.")

print(a)

# Random String Generator - Python 3.6
# (c) ry00001 / ry00000 2017