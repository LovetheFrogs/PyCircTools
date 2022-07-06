from PyCircTools import NotTruthValue, Xor, Not


class TFlipflop:
    def __init__(self):
        self.T = False
        self.clock = False
        self.Q = False
        self.Qp = False

    def get_T(self):
        return self.T

    def get_clock(self):
        return self.clock

    def get_Q(self):
        return self.Q

    def get_Qp(self):
        return self.Qp

    def set_T(self, value):
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
        if not self.clock:
            return self
        else:
            q_aux = self.Q

            self.Q = Xor().set_input(0, self.T).set_input(1, q_aux).get_output()
            self.Qp = Not().set_input(self.Q)

            return self
