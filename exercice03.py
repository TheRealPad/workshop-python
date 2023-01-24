from random import randint


def generateRandom(min, max):
    return randint(min, max)

if __name__ == "__main__":
    print(generateRandom(1, 100))