from CTools.Exceptions.MultiplexersExceptions import NonExistingInput, NonExistingControlSignal
from CTools.Exceptions.CircuitToolsExceptions import NotTruthValue


class Mux16to1:
    def __init__(self):
        self.input = [False] * 16
        self.set = [False] * 4
        self.output = self.__calculate_output()

    def get_input(self, num):
        if num >= len(self.input) or num < 0:
            raise NonExistingInput(num)

        return self.input[num]

    def get_set(self, setNum):
        if setNum >= len(self.set) or setNum < 0:
            raise NonExistingControlSignal

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
        first = not self.set[3] and not self.set[2] and not self.set[1] and not self.set[0] and self.input[0]
        second = not self.set[3] and not self.set[2] and not self.set[1] and self.set[0] and self.input[1]
        third = not self.set[3] and not self.set[2] and self.set[1] and not self.set[0] and self.input[2]
        fourth = not self.set[3] and not self.set[2] and self.set[1] and self.set[0] and self.input[3]
        fifth = not self.set[3] and self.set[2] and not self.set[1] and not self.set[0] and self.input[4]
        sixth = not self.set[3] and self.set[2] and not self.set[1] and self.set[0] and self.input[5]
        seventh = not self.set[3] and self.set[2] and self.set[1] and not self.set[0] and self.input[6]
        eight = not self.set[3] and self.set[2] and self.set[1] and self.set[0] and self.input[7]
        ninth = self.set[3] and not self.set[2] and not self.set[1] and not self.set[0] and self.input[8]
        tenth = self.set[3] and not self.set[2] and not self.set[1] and self.set[0] and self.input[9]
        eleventh = self.set[3] and not self.set[2] and self.set[1] and not self.set[0] and self.input[10]
        twelfth = self.set[3] and not self.set[2] and self.set[1] and self.set[0] and self.input[11]
        thirteenth = self.set[3] and self.set[2] and not self.set[1] and not self.set[0] and self.input[12]
        fourteenth = self.set[3] and self.set[2] and not self.set[1] and self.set[0] and self.input[13]
        fifteenth = self.set[3] and self.set[2] and self.set[1] and not self.set[0] and self.input[14]
        sixteenth = self.set[3] and self.set[2] and self.set[1] and self.set[0] and self.input[15]

        return first or second or third or fourth or fifth or sixth or seventh or eight or ninth or tenth or eleventh \
            or twelfth or thirteenth or fourteenth or fifteenth or sixteenth
