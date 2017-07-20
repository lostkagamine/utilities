import sys, string, random
a = 0
try:
    while True:
        stdin = sys.stdin.readline()
        stdin.replace("a", random.choice(string.ascii_letters))
        print(stdin)
except KeyboardInterrupt:
    sys.stdout.flush()
    pass
print(a)