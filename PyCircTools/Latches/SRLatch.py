from  PyCircTools.Exceptions.CircuitToolsExceptions import NotTruthValue
from PyCircTools.LogicGates import And, Nor


class SRLatch:
    """
    SR Latch module. Takes 3 inputs (R, S and Enable).
    """
    def __init__(self):
        """
        SRLatch class constructor. Initialises all inputs and outputs to False.
        """
        self.R = False
        self.S = False
        self.enable = False
        self.Q = False
        self.Qp = False

    def get_R(self):
        """
        Method get_R gets the value of the R input.

        :return: Value of the gate's R input.
        :rtype: bool
        """
        return self.R

    def get_S(self):
        """
        Method get_S gets the value of the S input.

        :return: Value of the gate's S input.
        :rtype: bool
        """
        return self.S

    def get_enable(self):
        """
        Method get_enable gets the value of enable input.

        :return: Value of the gate's enable input.
        :rtype: bool
        """
        return self.enable

    def get_Q(self):
        """
        Method get_Q gets the value of the Q output.

        :return: Value of the gate's Q output.
        :rtype: bool
        """
        return self.Q

    def get_Qp(self):
        """
        Method get_Qp gets the value of the Qp output.

        :return: Value of the gate's Qp output.
        :rtype: bool
        """
        return self.Qp

    def set_R(self, value):
        """
        Method set_R sets the value of the R input to the bool value.

        :param value: Desired value of the gate's R input.
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
        Method set_S sets the value of the S input to the bool value.

        :param value: Desired value of the gate's S input.
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

        :param value: Desired value of the gate's Enable input.
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
        and_r = And().set_input(0, self.R).set_input(1, self.enable)
        and_s = And().set_input(0, self.S).set_input(1, self.enable)

        nor_r = Nor().set_input(0, and_r.get_output()).set_input(1, self.Qp)
        nor_s = Nor().set_input(0, and_s.get_output()).set_input(1, self.Q)

        self.Q = nor_r.get_output()
        self.Qp = nor_s.get_output()

        return self
