__author__ = "arahis93"
__version__ = "0.1"

import sys
import getopt 
import os

file = None

argv = sys.argv[1:]


try:
    opts, args = getopt.getopt(argv, "f:")
except Exception:
    print("Unknown command! Usage: 'digitlang -f [file]'")

for opt, arg in opts: 
    if opt in ['-f']:
        file = arg
    else:
        print("Unknown command! Usage: 'digitlang -f [file]'")


try:
    source = open(file, "r", encoding="utf-8").read().split()
except Exception:
    if file == None:
        source = ["67", "111", "109", "109", "97", "110", "100", "32", "110", "111", "116", "32", "102", "111", "117", "110", "100", "33"]
    else:
        source = ["70", "105", "108", "101", "32", "110", "111", "116", "32", "102", "111", "117", "110", "100", "33"]

pointer = 0
result = []

for i in range(len(source)):
    try:
        number = int(source[pointer])
    except Exception:
        result.clear()
        result.append(f"Critical syntaxis error! Unknown command '{source[pointer]}'!")
        break
    try:
        result.append(chr(number))
        pointer += 1
    except Exception:
        result.clear()
        result.append(f"Critical syntaxis error! The number '{number}' is too large or too little!")
        break

final_result = "".join(result)

print(final_result)
exit()
