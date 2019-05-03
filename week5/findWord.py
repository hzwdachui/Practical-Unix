#!/usr/bin/env python
import sys
import os

def find_word(filename, key):
    count = 0
    #open a file for reading
    file = open(filename, 'r')
    # read file
    file_str = file.read()
    # and then split up the string based on whitespace
    words = file_str.split()

    # find_word
    for word in words:
        if word.lower() == key or word.lower().__contains__(key):
                count += 1
                # print(word)
    file.close()
    return count

def main():
    if len(sys.argv) != 3:
        print("wrong parameters")
        sys.exit(1)
    
    filename = sys.argv[1]
    key = sys.argv[2]
    count = find_word(filename, key)
    print(count)

# Standard boilerplate to call main().
if __name__ == '__main__':
    main()