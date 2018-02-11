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
        data = input("Please input the data you would like to encode: ")
        key = input("Please input the CRC key you would like to use: ")
        buildCRC(key,data)

    elif(option == 2):
        print("Placeholder for verifyCRC")

def buildCRC(key,data):
    print("Building CRC Code for: " + data + " using " + key)

    print(calculatePoly(key))

def verifyCRC(key,data):
    return True

def padZeros (data,key):
    power = calculateDegree(key)

    for x in range(power):
        data = data + "0"

    return data

def calculateDegree(key):
    keyDegree = len(key)

    for x in key:
        if(int(x) == 1):
            break
        elif(int(x) == 0):
            keyDegree = keyDegree - 1
        else:
            print("Error (calculateDegree) Unexpected Value: " + x)

        return keyDegree

def calculatePoly(key):

    result = ""
    keyDegree = len(key) - 1

    for x in key:
        print("Checking: " + x)
        if (int(x) == 1):
            degree = "x^" + str(keyDegree) + " + "
            result = result + degree
            keyDegree = keyDegree - 1
        elif (int(x) == 0):
            keyDegree = keyDegree - 1
        else:
            print("Error (calculatePoly) Unexpected Value: " + x)

    return result


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