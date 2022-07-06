from PyCircTools.Exceptions.MultiplexersExceptions import NonExistingInput, NonExistingControlSignal
from PyCircTools.Exceptions.CircuitToolsExceptions import NotTruthValue


class Mux4to1:
    """
    4 to 1 Multiplexer. Takes two bits as a Set input.
    """
    def __init__(self):
        """
        Mux4to1 class constructor method.
        """
        self.input = [False] * 4
        self.set = [False] * 2
        self.output = self.__calculate_output()

    def get_input(self, num):
        """
        Method get_input is used to get the value of input[num]

        :param num: Number of the input you want to get. It is a number from 0 to 3.
        :type num: int
        :raises NonExistingInput: Raised when a Multiplexer/Demultiplexer doesn't have the input asked for.
        :return: Value of the desired input (num).
        :rtype: bool
        """
        if num >= len(self.input) or num < 0:
            raise NonExistingInput(num)

        return self.input[num]

    def get_set(self, setNum):
        """
        Method get_set gets the value of the set[setNum] control signal.

        :param setNum: Number of the set control signal you want to get, either 0 or 1.
        :type setNum: int
        :raises NonExistingControlSignal: Raised when a Multiplexer/Demultiplexer doesn't have setNum control signal.
        :return: Value of the desired set control signal (setNum).
        :rtype: bool
        """
        if setNum >= len(self.set) or setNum < 0:
            raise NonExistingControlSignal

        return self.set[setNum]

    def get_output(self):
        """
        Method get_output gets the output of the 4 to 1 Multiplexer.

        :return: Value of the output.
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

    def set_set(self, setNum, value):
        """
        Method set_set sets the value of the set control signal to the desired truth value.

        :param setNum: Number of the set control signal selected.
        :type setNum: int
        :param value: Desired value of the set control signal.
        :type value: bool
        :raises NonExistingControlSignal: Raised when a Multiplexer/Demultiplexer doesn't have setNum control signal.
        :raises NotTruthValue: Raised when value's type is not bool.
        """
        if setNum >= len(self.set) or setNum < 0:
            raise NonExistingControlSignal(setNum)

        if type(value) is not bool:
            raise NotTruthValue

        self.set[setNum] = value
        self.output = self.__calculate_output()
        return self

    def __calculate_output(self):
        """
        Private method __calculate_output calculates the output signal using the 4-to-1 mux formula.

        :return: Value of the output signal.
        :rtype: bool
        """
        first_minterm = not self.set[0] and not self.set[1] and self.input[0]
        second_minterm = self.set[0] and not self.set[1] and self.input[1]
        third_minterm = not self.set[0] and self.set[1] and self.input[2]
        fourth_minterm = self.set[0] and self.set[1] and self.input[3]
        return first_minterm or second_minterm or third_minterm or fourth_minterm
