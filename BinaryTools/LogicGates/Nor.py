from BinaryTools.Exceptions.CircuitToolsExceptions import NotTruthValue
from BinaryTools.Exceptions.LogicGateExceptions import NonPositiveInput, NotAnInput


class Nor:
    def __init__(self, inputNumber=2):
        if inputNumber <= 0:
            raise NonPositiveInput

        self.input = self.__create_input(inputNumber)
        self.output = self.__calculate_output()
        self.numOfInputs = inputNumber

    def get_input(self, num):
        if num >= self.numOfInputs:
            raise NotAnInput

        return self.input[num]

    def get_output(self):
        return self.output

    def get_numOfInputs(self):
        return self.numOfInputs

    def set_input(self, num, value):
        if num >= self.numOfInputs:
            raise NotAnInput

        if type(value) is not bool:
            raise NotTruthValue

        self.input[num] = value
        self.__calculate_output()
        return self

    def add_input(self):
        self.input.append(False)
        self.numOfInputs += 1
        self.__calculate_output()
        return self

    def remove_input(self):
        self.input.pop()
        self.numOfInputs -= 1
        self.__calculate_output()
        return self

    def __calculate_output(self):
        output = False
        for value in self.input:
            output = output or value
        self.output = not output
        return self

    @staticmethod
    def __create_input(number):
        return [False] * number
