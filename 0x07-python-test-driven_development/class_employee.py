#!/usr/bin/python3

class Employee:

    raise_amt = 1.05

    def __init __(self, first, last, pay):
        self.first_n = first
        self.last_n = last
        self.pay_n = pay

    @property
    def email(self):
        return f'{self.first_n}{self.last_n}@email.com'

    @property
    def fullname(self):
        return f'{self.first_n} {self.last_n}'

    def apply_raise(self):
        self.pay_n = int(self.pay * self.raise_amt)

