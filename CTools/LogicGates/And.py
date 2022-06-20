from CTools.Exceptions.CircuitToolsExceptions import NotTruthValue
from CTools.Exceptions.LogicGateExceptions import NonPositiveInput, NotAnInput


class And:
    """
    And logic gate. Can have any number of inputs greater or equal than 1.

    Attributes:
        input (List[bool]): List containing all the inputs for the gate.
        output (bool): Output for the current inputs of the gate.
        numOfInputs (int): Current number of inputs for the gate.
    """
    def __init__(self, inputNumber=2):
        """
        And class constructor method.
        :param inputNumber: Number of inputs for the gate. Defaults to two.
        """
        if inputNumber <= 0:
            raise NonPositiveInput

        self.input = self.__create_input(inputNumber)
        self.output = self.__calculate_output()
        self.numOfInputs = inputNumber

    def get_input(self, num):
        """
        Method get_input(num) is used to get the value of self.input[num].
        :param num: Position of the input you want to get the value of.
        :return:
        :raises NotAnInput
        """
        if num >= self.numOfInputs:
            raise NotAnInput

        return self.input[num]

    def get_output(self):
        """
        
        :return:
        """
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

    @staticmethod
    def __create_input(number):
        return [False] * number

    def __calculate_output(self):
        output = True
        for value in self.input:
            output = output and value
        self.output = output
        return self

    def add_input(self):
        self.input.append(False)
        self.numOfInputs += 1
        self.output = False
        return self

    def remove_input(self):
        self.input.pop()
        self.numOfInputs -= 1
        self.__calculate_output()
        return self
