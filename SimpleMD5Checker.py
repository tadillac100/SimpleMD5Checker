import hashlib
import os
import sys

def get_base_dir():
    return os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(get_base_dir(), 'wordlist.txt')) as f:
    wordlist = f.read().splitlines()
f.close()

for item in wordlist:
    if hashlib.md5(item).hexdigest() == '1ceab1f5b327682c7835e21b96711429':
        print "The phrase " + "'" + item + "'" + " is the code!"
        sys.exit()

print "No matches found."
