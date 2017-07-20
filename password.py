# The Password Brute-Forcing Machine
# (c) ry00001/ry00000 2017 / (c) Anthony Hartup 2014
from modules import strgen
import sys, os, random, string
print("""
The Password Brute-Forcing Machine
(c) ry00001/ry00000 2017 / (c) Anthony Hartup 2014
http://github.com/ry00000/Utilities / https://anthscomputercave.com/tutorials/code/pwc.html

This software is provided "as is". No warranty will be provided.

TL;DR: I'm not responsible if this file messes up your computer (Which it shouldn't).
""")
pw = raw_input("Enter a password. >")

characters = string.ascii_letters + string.digits

guesses = []
quota = 0

# if len(pw) > 3:
#     print("Password length can't be more than 3.")
#     sys.exit(1)

def crack(pw):
    status = "ongoing"
    count = 0
    while status == "ongoing":
        global count
        char = [random.choice(characters) for i in range(len(pw))]
        guess = [char[i] for i in range(len(char))]
        sguess = "".join(guess)
        if sguess == pw:
            # print("Password cracked!: ", guess, ",", pw)
            status = "finished"
            count += 1
            #print(sguess)
            #print(count)
            break
        else:
            count += 1
    return count



try:
    print("Now cracking your input... This may take a long time. Things are happening, don't close the console window.")
    result = crack(pw)
    print("Cracked: {} guesses".format(result))

except KeyboardInterrupt:
    print("Program manually stopped by user. Final count: " + str(count))