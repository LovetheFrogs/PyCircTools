from PyCircTools import NotTruthValue, And, Xor, Or
from PyCircTools.Exceptions.OperatorsExceptions import NotCorrectAdder


class Adder:
    def __init__(self, full=False):
        self.A = False
        self.B = False
        self.carryOut = False
        self.output = False
        self.full = full
        if full:
            self.carryIn = False

    def get_A(self):
        return self.A

    def get_B(self):
        return self.B

    def get_carryOut(self):
        return self.carryOut

    def get_output(self):
        return self.output

    def get_carryIn(self):
        if not self.full:
            raise NotCorrectAdder('get_carryIn', False)

        return self.carryOut

    def set_A(self, value):
        if type(value) is not bool:
            raise NotTruthValue

        self.A = value
        self.__calculate_output()
        return self

    def set_B(self, value):
        if type(value) is not bool:
            raise NotTruthValue

        self.B = value
        self.__calculate_output()
        return self

    def set_carryIn(self, value):
        if not self.full:
            raise NotCorrectAdder('set_carryIn', False)

        if type(value) is not bool:
            raise NotTruthValue

        self.carryIn = value
        self.__calculate_output()
        return self

    def convert(self):
        if not self.full:
            self.full = not self.full
            self.carryIn = False
            self.__calculate_output()
        else:
            self.full = not self.full
            self.__delattr__(self.carryIn)
            self.__calculate_output()

        return self

    def __calculate_output(self):
        if not self.full:
            self.carryOut = And().set_input(0, self.A).set_input(1, self.B).get_output()
            self.output = Xor().set_input(0, self.A).set_input(1, self.B).get_output()

            return self

        self.carryOut = Or(3).set_input(0, And().set_input(0, self.A).set_input(1, self.B).get_output())\
            .set_input(1, And().set_input(0, self.A).set_input(1, self.carryIn).get_output())\
            .set_input(2, And().set_input(0, self.B).set_input(1, self.carryIn).get_output())\
            .get_output()

        self.output = Xor(3).set_input(0, self.A).set_input(1, self.B).set_input(2, self.carryIn)

        return self
