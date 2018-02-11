# pyCRC.py - Python3.6 based cyclic redundancy check
print("+-------------------------------------+")
print("|          p y C R C . P Y            |")
print("| By: Sean McElhare (TheCrimsonCoder) |")
print("| https://github.com/thecrimsoncoder  |")
print("+-------------------------------------+")

def main():

    print("+-------------------------------------+")
    print("| What would you like to do:          |")
    print("| 1. Build CRC Code                   |")
    print("| 2. Verify CRC Code                  |")
    print("+-------------------------------------+")
    option = int(input("OPTION: "))

    if(option == 1):
        data = input("Please input the data you would like to check: ")
        key = input("Please input the CRC key you would like to use: ")
        buildCRC(key,data)

    elif(option == 2):
        print("Placeholder for verifyCRC")

def buildCRC(key,data):
    print("Building CRC Code for: " + data + " using " + key)

    # Number of bits that can be compared at a time
    keyLength = len(key)
    data = padZeros(data,keyLength)

def padZeros (data,power):
    print("Using CRC polynomial generator x^3 + x + 1")
    return True

def calculateDegree(key):

def calculatePoly(key):
    result = ""
    subtract = 1
    for x in key:
        if(x == 1):

        elif(x == 0):
        else:
            print("Error (calculatePoly) Unexpected Value: " + x)


def checkValue(dataInt, keyInt):
        if(dataInt == 0 and keyInt == 0):
                return 0
        elif(dataInt == 1 and keyInt == 0):
                return 1
        elif(dataInt == 0 and keyInt == 1):
                return 1
        elif(dataInt == 1 and keyInt == 1):
                return 0
        else:
            print("Error (checkValue): An unexpected value was given (frameInt: " + dataInt + " generatorInt : " + keyInt + ")")

main()