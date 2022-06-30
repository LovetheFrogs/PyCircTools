from PyCircTools.Exceptions.MultiplexersExceptions import NonExistingInput
from PyCircTools.Exceptions.CircuitToolsExceptions import NotTruthValue


class Mux2to1:
    """
    2 to 1 Multiplexer. Takes one Set input.
    """
    def __init__(self):
        """
        Mux2to1 class constructor method.
        """
        self.input = [False, False]
        self.set = False
        self.output = self.__calculate_output()

    def get_input(self, num):
        """
        Method get_input is used to get the value of input[num]

        :param num: Number of the input you want to get, either 0 or 1.
        :type num: int
        :raises NonExistingInput: Raised when a Multiplexer/Demultiplexer doesn't have the input asked for.
        :return: Value of the desired input (num).
        :rtype: bool
        """
        if num >= len(self.input) or num < 0:
            raise NonExistingInput(num)

        return self.input[num]

    def get_set(self):
        """
        Method get_set gets the value of the set control signal.

        :return: Value of the set control signal.
        :rtype: bool
        """
        return self.set

    def get_output(self):
        """
        Method get_output gets the output of the 2 to 1 Multiplexer.

        :return: Value of the output
        :rtype: bool
        """
        return self.output

    def set_input(self, num, value):
        """
        Method set_input sets a certain input to the desired value, either True or False.

        :param num: Number of the input selected.
        :type num: int
        :param value: Desired value of the input.
        :type value: bool
        :raises NonExistingInput: raised when a Multiplexer/Demultiplexer doesn't have the input asked for.
        :raises NotTruthValue: Raised when value's type is not bool.
        """
        if num >= len(self.input) or num < 0:
            raise NonExistingInput(num)

        if type(value) is not bool:
            raise NotTruthValue

        self.input[num] = value
        self.output = self.__calculate_output()
        return self

    def set_set(self, value):
        """
        Method set_set sets the value of the set control signal to the desired truth value.

        :param value: Desired value of the set control signal.
        :type value: bool
        :raises NotTruthValue: Raised when value's type is not bool.
        """
        if type(value) is not bool:
            raise NotTruthValue

        self.set = value
        self.output = self.__calculate_output()
        return self

    def __calculate_output(self):
        """
        Private method __calculate_output calculates the output signal using the 2-to-1 mux formula.

        :return: Value of the output signal.
        :rtype: bool
        """
        return (self.input[0] and not self.set) or (self.input[1] and self.set)
