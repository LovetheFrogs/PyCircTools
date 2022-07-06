from PyCircTools import NotTruthValue
from PyCircTools.LogicGates import And, Or


class JKFlipflop:
    """
    JK-Flipflop module. Takes 3 inputs (J, K and Clock).
    """
    def __init__(self):
        """
        JKFlipflop class constructor. Initialises all inputs and outputs to False, except Qp.
        """
        self.K = False
        self.J = False
        self.clock = False
        self.Q = False
        self.Qp = False

    def get_K(self):
        """
        Method get_K gets the value of the K input.

        :return: Value of the flip-flop's K input.
        :rtype: bool
        """
        return self.K

    def get_J(self):
        """
        Method get_J gets the value of the J input.

        :return: Value of the flip-flop J input.
        :rtype: bool
        """
        return self.J

    def get_clock(self):
        """
        Method get_clock gets the value of clock input.

        :return: Value of the flip-flop's Clock input.
        :rtype: bool
        """
        return self.clock

    def get_Q(self):
        """
        Method get_Q gets the value of the Q output.

        :return: Value of the flip-flop's Q output.
        :rtype: bool
        """
        return self.Q

    def get_Qp(self):
        """
        Method get_Qp gets the value of the Qp output.

        :return: Value of the flip-flop's Qp output.
        :rtype: bool
        """
        return self.Qp

    def set_K(self, value):
        """
        Method set_K sets the value of the K input to the bool value.

        :param value: Desired value of the flip-flop's K input.
        :type value: bool
        :raises NotTruthValue: Raised when a variable type is not bool.
        """
        if type(value) is not bool:
            raise NotTruthValue

        self.K = value
        self.__calculate_output()
        return self

    def set_J(self, value):
        """
        Method set_J sets the value of the J input to the bool value.

        :param value: Desired value of the flip-flop's J input.
        :type value: bool
        :raises NotTruthValue: Raised when a variable type is not bool.
        """
        if type(value) is not bool:
            raise NotTruthValue

        self.J = value
        self.__calculate_output()
        return self

    def set_clock(self, value):
        """
        Method set_clock sets the value of Clock to the bool value.

        :param value: Desired value of the flip-flop's Clock input.
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
        Method __calculate_output calculates the value of both the Q and the Qp signal.
        """
        if not self.clock:
            return self
        else:
            q_aux = self.Q
            qp_aux = self.Qp

            and1 = And(3).set_input(0, self.J).set_input(1, qp_aux).set_input(2, self.clock)
            and2 = And(3).set_input(0, not self.K).set_input(1, q_aux).set_input(2, self.clock)

            self.Q = Or().set_input(0, and1.get_output()).set_input(1, and2.get_output()).get_output()
            self.Qp = not self.Q

            return self
