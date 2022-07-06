from PyCircTools import NotTruthValue, Xor, Not


class TFlipflop:
    """
    T-Flipflop module. Takes 2 inputs (T and Clock).
    """
    def __init__(self):
        """
        TFlipflop class constructor. Initialises all inputs and outputs to False.
        """
        self.T = False
        self.clock = False
        self.Q = False
        self.Qp = False

    def get_T(self):
        """
        Method get_T gets the value of the T input.

        :return: Value of the flip-flop's T input.
        :rtype: bool
        """
        return self.T

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

    def set_T(self, value):
        """
        Method set_T sets the value of the T input to the bool value.

        :param value: Desired value of the flip-flop's T input.
        :type value: bool
        :raises NotTruthValue: Raised when a variable type is not bool.
        """
        if type(value) is not bool:
            raise NotTruthValue

        self.T = value
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

            self.Q = Xor().set_input(0, self.T).set_input(1, q_aux).get_output()
            self.Qp = Not().set_input(self.Q).get_output()

            return self
