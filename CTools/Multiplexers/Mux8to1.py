from CTools.Exceptions.MultiplexersExceptions import NonExistingInput, NonExistingControlSignal
from CTools.Exceptions.CircuitToolsExceptions import NotTruthValue


class Mux8to1:
    """
    8 to 1 Multiplexeer. Takes three bits as Set input.
    """
    def __init__(self):
        """
        Mux8to1 class constructor method.
        """
        self.input = [False] * 8
        self.set = [False] * 3
        self.output = self.__calculate_output()

    def get_input(self, num):
        """
        Method get_input is used to get the value of input[num]

        :param num: Number of the input you want to get. It is a number from 0 to 7.
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

        :param setNum: Number of the set control signal you want to get, ranges from 0 to 3.
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
        Method get_output gets the output of the 8 to 1 Multiplexer.

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
        Private method __calculate_output calculates the output signal using the 8-to-1 mux formula.

        :return: Value of the output signal.
        :rtype: bool
        """
        first = not self.set[2] and not self.set[1] and not self.set[0] and self.input[0]
        second = not self.set[2] and not self.set[1] and self.set[0] and self.input[1]
        third = not self.set[2] and self.set[1] and not self.set[0] and self.input[2]
        fourth = not self.set[2] and self.set[1] and self.set[0] and self.input[3]
        fifth = self.set[2] and not self.set[1] and not self.set[0] and self.input[4]
        sixth = self.set[2] and not self.set[1] and self.set[0] and self.input[5]
        seventh = self.set[2] and self.set[1] and not self.set[0] and self.input[6]
        eight = self.set[2] and self.set[1] and self.set[0] and self.input[7]

        return first or second or third or fourth or fifth or sixth or seventh or eight
