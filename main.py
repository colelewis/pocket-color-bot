from random import randint
import webcolors

def RandomRGBTriple():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def main():
    print(RandomRGBTriple())

if __name__=="__main__":
    main()