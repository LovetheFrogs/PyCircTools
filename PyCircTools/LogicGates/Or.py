from PyCircTools.Exceptions.CircuitToolsExceptions import NotTruthValue
from PyCircTools.Exceptions.LogicGateExceptions import NonPositiveInput, NotAnInput


class Or:
    """
    Or logic gate. Can have any number of inputs greater or equal than 1.
    """
    def __init__(self, inputNumber=2):
        """
        Or class constructor method.

        :param inputNumber: Number of inputs for the gate. Defaults to two.
        :type inputNumber: int
        :raises NonPositiveInput: Raised when inputNumber is lower or equal to zero.
        """
        if inputNumber <= 0:
            raise NonPositiveInput

        self.input = self.__create_input(inputNumber)
        self.output = self.__calculate_output()
        self.numOfInputs = inputNumber

    def get_input(self, num):
        """
        Method get_input is used to get the value of input[num].

        :param num: Position of the input you want to get the value of.
        :type num: int
        :raises NotAnInput: Raised when the selected input does not exist.
        :return: Returns the value of the input num.
        :rtype: bool
        """
        if num >= self.numOfInputs:
            raise NotAnInput

        return self.input[num]
    
    def __getitem__(self, __num: int) -> bool:
        """
        Method overload to use [] operator to get the value of input[num].

        :param num: Position of the input you want to get the value of.
        :type num: int
        :raises NotAnInput: Raised when the selected input does not exist.
        :return: Returns the value of the input num.
        :rtype: bool
        """
        if __num >= self.numOfInputs:
            raise NotAnInput
        
        return self.input[__num]

    def get_output(self):
        """
        Method get_output is used to get the output of a logic gate.

        :return: Output of the gate.
        :rtype: bool
        """
        return self.output

    def get_numOfInputs(self):
        """
        Method get_numOfInputs is used to get the number of inputs of a logic gate.

        :return: Number of inputs
        :rtype: int
        """
        return self.numOfInputs

    def set_input(self, num, value):
        """
        Method set_input sets a certain input to the desired value, either True or False.

        :param num: Number of the input selected.
        :type num: int
        :param value: Desired value of the input.
        :type value: bool
        :raises NotAnInput: Raised when the selected input does not exist.
        :raises NotTruthValue: Raised when value's type is not bool.
        """
        if num >= self.numOfInputs:
            raise NotAnInput

        if type(value) is not bool:
            raise NotTruthValue

        self.input[num] = value
        self.__calculate_output()
        return self
    
    def __setitem__(self,__num: int,__value: bool) -> None:
        """
        Method that overloads [] operator to assign a certain input to the desired value, either True or False.

        :param num: Number of the input selected.
        :type num: int
        :param value: Desired value of the input.
        :type value: bool
        :raises NotAnInput: Raised when the selected input does not exist.
        :raises NotTruthValue: Raised when value's type is not bool.
        """
        if __num >= self.numOfInputs:
            raise NotAnInput

        if type(__value) is not bool:
            raise NotTruthValue

        self.input[__num] = __value
        self.__calculate_output()
        return self

    def add_input(self):
        """
        Method add_input adds a new input to a logic gate.
        """
        self.input.append(False)
        self.numOfInputs += 1
        self.__calculate_output()
        return self

    def remove_input(self, index=None):
        """
        Removes the last input of a logic gate. or a specific input given an index
        """
        if index == None:
            self.input.pop()
        else:
            if index > self.numOfInputs-1 or index < 0:
                raise NotAnInput
            self.input.pop(index)
            
        self.__calculate_output()
        self.numOfInputs -= 1
        return self


    def __calculate_output(self):
        output = False
        for value in self.input:
            output = output or value
        self.output = output

    @staticmethod
    def __create_input(number):
        return [False] * number
