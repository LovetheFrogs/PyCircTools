from CTools.Exceptions.MultiplexersExceptions import NonExistingInput, NonExistingControlSignal
from CTools.Exceptions.CircuitToolsExceptions import NotTruthValue


class Mux4to1:
    def __init__(self):
        self.input = [False] * 4
        self.set = [False] * 2
        self.output = self.__calculate_output()

    def get_input(self, num):
        return self.input[num]

    def get_set(self, setNum):
        return self.set[setNum]

    def get_output(self):
        return self.output

    def set_input(self, num, value):
        if num >= len(self.input) or num < 0:
            raise NonExistingInput(num)

        if type(value) is not bool:
            raise NotTruthValue

        self.input[num] = value
        self.output = self.__calculate_output()
        return self

    def set_set(self, setNum, value):
        if setNum >= len(self.set) or setNum < 0:
            raise NonExistingControlSignal(setNum)

        if type(value) is not bool:
            raise NotTruthValue

        self.set[setNum] = value
        self.output = self.__calculate_output()
        return self

    def __calculate_output(self):
        first_minterm = not self.set[0] and not self.set[1] and self.input[0]
        second_minterm = self.set[0] and not self.set[1] and self.input[1]
        third_minterm = not self.set[0] and self.set[1] and self.input[2]
        fourth_minterm = self.set[0] and self.set[1] and self.input[3]
        return first_minterm or second_minterm or third_minterm or fourth_minterm
