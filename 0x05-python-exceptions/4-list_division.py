#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    length = []
    #list_length = len(length)
    try:
        for i in range(list_length):
            try:
                length.append(my_list_1[i] / my_list_2[i])
            except ZeroDivisionError:
                length.append(0)
                print("division by 0")
            except TypeError:
                length.append(0)
                print("wrong type")
            except IndexError:
                length.append(0)
                print("out of range")
    except Exception as e:
        print(e)
    finally:
        #if len(my_list_1) != len(my_list_2):
         #    print("out of range")
    
        return length
