class MyInt(int):
    
    def __eq__(self, num):
        return super().__eq__(num)#.real if isinstance(num, complex) else num)
    
    def __ne__(self, num):
        return super().__ne__(num)#.real if isinstance(num, complex) else num)


my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)
