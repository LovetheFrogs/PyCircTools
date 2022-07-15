from PyCircTools import Not, NotControlList, WrongSize
from PyCircTools.Operators.Adder import *


class Conversor:
    """
    Module conversor is used to convert any input from pure binary to two's complement.
    """
    def __init__(self, length=4):
        """
        Constructor of the Conversor class. Needs the length of the number you want to have converted. (defaults to 4).

        :param length: Lenght of the number to convert
        :type length: int
        """
        self.input = [False] * length
        self.length = length
        self.output = [None]
        self.__calculate_output()

    def get_input(self):
        """
        Method get_input gets the input of the conversor.

        :return: List containing the input value.
        :rtype: list
        """
        return self.input

    def get_length(self):
        """
        Method get_length gets the length of the conversor input.

        :return: Length of the number that can be converted.
        :rtype: int
        """
        return self.length

    def get_output(self):
        """
        Method get_output gets the output of the conversor.

        :return: List containing the output values.
        :rtype: list
        """
        return self.output

    def set_input(self, values):
        """
        Method set_input sets the input of the conversor to the list of bools 'values'

        :param values: List of bools containing the values of the input
        :type values: list
        :raises NotControlList: raised when a list is not of type bool or is not a list at all
        :raises WrongSize: raised when the list does not have the required size
        """
        if type(values) is not list:
            raise NotControlList

        for val in values:
            if type(val) is not bool:
                raise NotControlList

        if len(values) > self.length:
            raise WrongSize(len(values), self.length)

        self.input = values
        self.__calculate_output()
        return self

    def __calculate_output(self):
        """
        Method __calculate_output calculates the desired output of the coversor by calling the __build method.
        """
        inverted = []

        for val in self.input:
            inverted.append(Not().set_input(val).get_output)
        self.output = self.__build(inverted)

        return self

    def __build(self, inverted):
        """
        Method __build creates a list with the needed adders to convert the number to two's complement.

        :param inverted: Input of the gate inverted.
        :type inverted: list
        :return: List containing the output.
        :rtype: list
        """
        addrs = []
        for i in range(self.length):
            if i == 0:
                addrs.append(Adder().set_A(inverted[i]).set_B(True))
            else:
                addrs.append(Adder(True).set_carryIn(addrs[i - 1].get_carryOut()).set_A(inverted[i]))

        return addrs
