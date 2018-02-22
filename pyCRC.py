# pyCRC.py - Python3.6 based cyclic redundancy checker and builder
import sys
import time

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
    print("| 3. Quit                             |")
    print("+-------------------------------------+")
    option = int(input("OPTION: "))

    if(option == 1):
        data = input("Please input the data you would like to encode: ")
        key = input("Please input the generator polynomial you would like to use in binary form: ")
        remainder = CRC(key,data)

        data_list = list(data)
        data_list = list(map(int, data_list))

        encoded_data = data_list + remainder
        encoded_data = ''.join(str(encoded_data))

        print(">> Encoded Data: " + str(encoded_data))

    elif(option == 2):
        data = input("Please input the data you would like to check: ")
        key = input("Please input the generator polynomial you used to generate the data: ")
        verify = verifyCRC(key,data)

        if(verify == True):
            print(">> Data is ok :)")
        else:
            print(">> Data is NOT ok :( ")

    elif(option == 3):
        print(">> Until Next Time!")
        time.sleep(2)
        sys.exit(0)
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
    print(">> Ready for lift-off....")


    while(len(working_data) > 0):
        if(shift_register[0] == 1):

            shift_register.append(working_data.pop(0))

            print(">> Computing XOR on: " + str(shift_register) + " using key: " + str(key))

            shift_register = computeCRC(key,shift_register)
            shift_register.pop(0)

            print("SHIFT REGISTER: " + str(shift_register) + " WORKING_DATA: " '' + str(working_data))

        elif(shift_register[0] != 1):
            shift_register.append(working_data.pop(0))
            shift_register.pop(0)

            print("SHIFT REGISTER: " + str(shift_register) + " WORKING_DATA: " '' + str(working_data))

        else:
            print("!! Error (CRC): Unhandled Exception: ")

    print(">> Remainder is: " + str(shift_register))

    return shift_register

def computeCRC(key,shift_register):
    print("#################### START XOR CALCULATION ####################")
    for index in range(0,len(shift_register)):
        print("XOR: Comparing key value: " + str(key[index]) + " and shift_register value: " + str(shift_register[index]))
        if int(shift_register[index]) == int(key[index]):

            shift_register[index] = 0
        elif int(shift_register[index]) != int(key[index]):
            shift_register[index] = 1
        else:
            print("!! Error (computeCRC): Unhandled Exception: ")
    print("XOR: New Shift Register Computed: " + str(shift_register))
    print("##################### END XOR CALCULATION #####################")
    return shift_register

def verifyCRC(key,data):

    remainder = CRC(key,data)

    if sum(remainder) == 0:
        return True
    else:
        return False

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