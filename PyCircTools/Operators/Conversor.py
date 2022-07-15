from PyCircTools import Not, NotControlList
from PyCircTools.Operators.Adder import *


class Conversor:
    def __init__(self, length=4):
        self.input = [False] * length
        self.length = length
        self.output = [None]
        self.__calculate_output()

    def get_input(self):
        return self.input

    def get_length(self):
        return self.length

    def get_output(self):
        return self.output

    def set_input(self, values):
        if type(values) is not list:
            raise NotControlList

        for val in values:
            if type(val) is not bool:
                raise NotControlList

        self.input = values
        self.__calculate_output()
        return self

    def __calculate_output(self):
        inverted = []

        for val in self.input:
            inverted.append(Not().set_input(val).get_output)
        self.output = self.__build(inverted)

        return self

    def __build(self, inverted):
        addrs = []
        for i in range(self.length):
            if i == 0:
                addrs.append(Adder().set_A(inverted[i]).set_B(True))
            else:
                addrs.append(Adder(True).set_carryIn(addrs[i - 1].get_carryOut()).set_A(inverted[i]))

        return addrs
