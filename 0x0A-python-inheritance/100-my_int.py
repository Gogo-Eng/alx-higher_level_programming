#!/usr/bin/python3

class MyInt(int):

    def __eq__(self, num):
        return self.real != num

    def __ne__(self, num):
        return self.real == num
