#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    length = []

    try:
        for i in range(len(my_list_1)):
            try:
                length.append(my_list_1[i] / my_list_2[i])
            except ZeroDivisionError:
                length.append(0)
                print("division by 0")
            except TypeError:
                length.append(0)
                print("wrong type")
    except Exception as e:
        print(e)
    finally:
        return length
    if len(my_list_1) != len(my_list_2):
        print("out of range")
