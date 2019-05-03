import sys
import os


def main():    
    for i in range(len(sys.argv)-1):
        # note that argv begin with 0, but 0 is the name of script
        # the argvs we input begin from 1
        index = i+1
        os.system("python findWord.py shakes.txt " + str(sys.argv[index]))
    
if __name__ == '__main__':
    main()
