from PyCircTools import NotTruthValue, And, Xor, Or
from PyCircTools.Exceptions.OperatorsExceptions import NotCorrectAdder


class Adder:
    """
    Adder module. The constructor can be used to specify whether a half-adder or a full-adder is being created.
    """
    def __init__(self, full=False):
        """
        Adder class constructor.

        :param full: Defaults to False. Used to specify if the type of adder used. (False -> Half-adder, True -> Full-adder).
        :type full: bool
        """
        self.A = False
        self.B = False
        self.carryOut = False
        self.output = False
        self.full = full
        if full:
            self.carryIn = False

    def get_A(self):
        """
        Method get_A gets the value of the first summand.

        :return: Value of the first summand.
        :rtype: bool
        """
        return self.A

    def get_B(self):
        """
        Method get_A gets the value of the second summand.

        :return: Value of the second summand.
        :rtype: bool
        """
        return self.B

    def get_carryOut(self):
        """
        Method get_carryOut gets the value of the output carry.

        :return: Value of the output carry.
        :rtype: bool
        """
        return self.carryOut

    def get_output(self):
        """
        Method get_output gets the value of the sum.

        :return: Result of the sum.
        :rtype: bool
        """
        return self.output

    def get_carryIn(self):
        """
        Method get_carryIn gets the value of the input carry. It can only be used on a Full-adder object.

        :raises NotCorrectAdder: Raised when when a function is called and is not allowed for the instance of an adder used in.
        :return: Value of the input carry.
        :rtype: bool
        """
        if not self.full:
            raise NotCorrectAdder('get_carryIn', False)

        return self.carryOut

    def set_A(self, value):
        """
        Method set_A sets the value of the first summand to the bool value.

        :param value: Desired value of the adder's first summand.
        :type value: bool
        :raises NotTruthValue: Raised when a variable type is not bool.
        """
        if type(value) is not bool:
            raise NotTruthValue

        self.A = value
        self.__calculate_output()
        return self

    def set_B(self, value):
        """
        Method set_B sets the value of the second summand to the bool value.

        :param value: Desired value of the adder's second summand.
        :type value: bool
        :raises NotTruthValue: Raised when a variable type is not bool.
        """
        if type(value) is not bool:
            raise NotTruthValue

        self.B = value
        self.__calculate_output()
        return self

    def set_carryIn(self, value):
        """
        Method set_carryIn sets the value of the carry input to the bool value.

        :param value: Desired value of the adder's input carry.
        :type value: bool
        :raises NotCorrectAdder: Raised when when a function is called and is not allowed for the instance of an adder used in.
        :raises NotTruthValue: Raised when a variable type is not bool.
        """
        if not self.full:
            raise NotCorrectAdder('set_carryIn', False)

        if type(value) is not bool:
            raise NotTruthValue

        self.carryIn = value
        self.__calculate_output()
        return self

    def convert(self):
        """
        Method convert is used to transform a full-adder into a half-adder and vice-versa.
        """
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
        """
        Method __calculate_output is a private method which calculates the value of both carryOut and output signals.
        It is used for both full and half adders.
        """
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
