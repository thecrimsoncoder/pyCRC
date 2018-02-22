# pyCRC.py - Python3.6 based cyclic redundancy checker and builder
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
        key = input("Please input the generator polynomial you would like to use in binary form: ")
        CRC(key,data)

    elif(option == 2):
        print("Placeholder for verifyCRC")

    else:
        print("!! Error (main): Value is not accepted, Returning to menu....")
        main()

def CRC(key,data):
    print(">> Beginning CRC for: " + data + " using " + key + " as the generator key")

    poly_degree = calculateDegree(key)
    shift_register = [0] * poly_degree

    working_data = padZeros(data,key)
    working_data = list(working_data)
    working_data = list(map(int, working_data))


    print(">> Degree of generator key polynomial is: " + str(poly_degree))
    print(">> Initializing shift_register: " + str(shift_register))
    print(">> Preparing working_data: " + str(working_data))



    while(len(working_data) > 0):
        if(shift_register[0] == 1):

            # Testing ############################
            shift_register.append(working_data.pop(0))
            print("Computing XOR on: " + str(shift_register) + " using key: " + str(key))
            shift_register = computeCRC(key,shift_register)
            shift_register.pop(0)
            ######################################

            print(shift_register)
            print(working_data)

        elif(shift_register[0] != 1):
            shift_register.append(working_data.pop(0))
            shift_register.pop(0)

            print(shift_register)
            print(working_data)

        else:
            print("!! Error (CRC): Unhandled Exception: ")

    print("Remainder is: " + str(shift_register))


def computeCRC(key,shift_register):
    print("#################################################################")
    for index in range(0,len(shift_register)):
        print("Comparing key value: " + str(key[index]) + " and shift_register value: " + str(shift_register[index]))
        if int(shift_register[index]) == int(key[index]):

            shift_register[index] = 0
        elif int(shift_register[index]) != int(key[index]):
            shift_register[index] = 1
        else:
            print("!! Error (computeCRC): Unhandled Exception: ")
    print("NEW SHIFT REGISTER: " + str(shift_register))
    print("#################################################################")
    return shift_register

def verifyCRC(key,data):

    remainder = CRC(key,data)

    if remainder == 0:
        return True
    elif remainder != 0:
        return False
    else:
        print("!! Error (verifyCRC): Function remainder resulted in: " + str(remainder))

def padZeros (data,key):
    power = calculateDegree(key)

    print(">> Appending " + str(power) + " zeros to the end of " + str(data))

    for x in range(power):
        data = data + "0"

    return data

def calculateDegree(key):
    keyDegree = int(len(key))

    for x in key:
        if(int(x) == 1):
            break
        elif(int(x) == 0):
            keyDegree = keyDegree - 1
        else:
            print("!! Error (calculateDegree): Unexpected Value: " + x)

    keyDegree = keyDegree - 1

    return keyDegree

main()