from PyCircTools.Exceptions.CircuitToolsExceptions import NotTruthValue
from PyCircTools.LogicGates import And, Nor


class SRLatch:
    """
    SR-Latch module. Takes 3 inputs (Reset, Set and Enable).
    """
    def __init__(self):
        """
        SRLatch class constructor. Initialises all inputs and outputs to False, except Qp.
        """
        self.R = False
        self.S = False
        self.enable = False
        self.Q = False
        self.Qp = True

    def get_R(self):
        """
        Method get_R gets the value of the Reset input.

        :return: Value of the latch's Reset input.
        :rtype: bool
        """
        return self.R

    def get_S(self):
        """
        Method get_S gets the value of the S input.

        :return: Value of the latch's Set input.
        :rtype: bool
        """
        return self.S

    def get_enable(self):
        """
        Method get_enable gets the value of enable input.

        :return: Value of the latch's Enable input.
        :rtype: bool
        """
        return self.enable

    def get_Q(self):
        """
        Method get_Q gets the value of the Q output.

        :return: Value of the latch's Q output.
        :rtype: bool
        """
        return self.Q

    def get_Qp(self):
        """
        Method get_Qp gets the value of the Qp output.

        :return: Value of the latch's Qp output.
        :rtype: bool
        """
        return self.Qp

    def set_R(self, value):
        """
        Method set_R sets the value of the Reset input to the bool value.

        :param value: Desired value of the latch's Reset input.
        :type value: bool
        :raises NotTruthValue: Raised when a variable type is not bool.
        """
        if type(value) is not bool:
            raise NotTruthValue

        self.R = value
        self.__calculate_output()
        return self

    def set_S(self, value):
        """
        Method set_S sets the value of the Set input to the bool value.

        :param value: Desired value of the latch's Set input.
        :type value: bool
        :raises NotTruthValue: Raised when a variable type is not bool.
        """
        if type(value) is not bool:
            raise NotTruthValue

        self.S = value
        self.__calculate_output()
        return self

    def set_enable(self, value):
        """
        Method set_enable sets the value of Enable to the bool value.

        :param value: Desired value of the latch's Enable input.
        :type value: bool
        :raises NotTruthValue: Raised when a variable type is not bool.
        """
        if type(value) is not bool:
            raise NotTruthValue

        self.enable = value
        self.__calculate_output()
        return self

    def __calculate_output(self):
        """
        Method __calculate_output calculates the value of both the Q and the Qp signal.
        """
        if not self.enable:
            return self
        else:
            and_r = And().set_input(0, self.R).set_input(1, self.enable)
            and_s = And().set_input(0, self.S).set_input(1, self.enable)

            self.Qp = Nor().set_input(0, and_s.get_output()).set_input(1, self.Q).get_output()
            self.Q = Nor().set_input(0, and_r.get_output()).set_input(1, self.Qp).get_output()

            return self
