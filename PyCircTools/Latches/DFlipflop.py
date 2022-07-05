from PyCircTools.Exceptions.CircuitToolsExceptions import NotTruthValue
from PyCircTools.LogicGates import And, Nor, Not


class DFlipflop:
    """
    D-Flipflop module. Takes 2 inputs (Data and Clock).
    """
    def __init__(self):
        """
        DFlipflop class constructor. Initialises all inputs and outputs to False, except Qp.
        """
        self.D = False
        self.clock = False
        self.Q = False
        self.Qp = True

    def get_D(self):
        """
        Method get_D gets the value of the Data input.

        :return: Value of the latch's Data input.
        :rtype: bool
        """
        return self.D

    def get_enable(self):
        """
        Method get_enable gets the value of the clock input.

        :return: Value of the latch's Enable input.
        :rtype: bool
        """
        return self.clock

    def get_Q(self):
        """
        Method get_Q returns the value of the Q output.

        :return: Value of the latch's Q output.
        :rtype: bool
        """
        return self.Q

    def get_Qp(self):
        """
        Method get_Qp returns the value of the Qp output.

        :return: Value of the latch's Qp output.
        :rtype: bool
        """
        return self.Qp

    def set_D(self, value):
        """
        Method set_D sets the value of the Data input to the bool value.

        :param value: Desired value of the latch's Data input.
        :type value: bool
        :raises NotTruthValue: Raised when a variable type is not bool.
        """
        if type(value) is not bool:
            raise NotTruthValue

        self.D = value
        self.__calculate_output()
        return self

    def set_enable(self, value):
        """
        Method set_enable sets the value of Clock to the bool value.

        :param value: Desired value of the latch's Clock input.
        :type value: bool
        :raises NotTruthValue: Raised when a variable type is not bool.
        """
        if type(value) is not bool:
            raise NotTruthValue

        self.clock = value
        self.__calculate_output()
        return self

    def __calculate_output(self):
        """
        Method __calculate_output calculates the output of both the Q and Qp signals.
        """
        if not self.clock:
            return self
        else:
            and_d = And().set_input(0, self.clock).set_input(1, self.D)
            not_d = Not().set_input(self.D)
            and_not_d = And().set_input(0, not_d.get_output()).set_input(1, self.clock)

            if not self.D:
                self.Q = Nor().set_input(0, and_not_d.get_output()).set_input(1, self.Qp).get_output()
                self.Qp = Nor().set_input(0, and_d.get_output()).set_input(1, self.Q).get_output()
            else:
                self.Qp = Nor().set_input(0, and_d.get_output()).set_input(1, self.Q).get_output()
                self.Q = Nor().set_input(0, and_not_d.get_output()).set_input(1, self.Qp).get_output()

        return self
