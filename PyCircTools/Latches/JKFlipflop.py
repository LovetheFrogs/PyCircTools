from PyCircTools import NotTruthValue
from PyCircTools.LogicGates import And, Nor


class JKFlipflop:
    def __init__(self):
        self.K = False
        self.J = False
        self.clock = False
        self.Q = False
        self.Qp = True

    def get_K(self):
        return self.K

    def get_J(self):
        return self.J

    def get_clock(self):
        return self.clock

    def get_Q(self):
        return self.Q

    def get_Qp(self):
        return self.Qp

    def set_K(self, value):
        if type(value) is not bool:
            raise NotTruthValue

        self.K = value
        self.__calculate_output()
        return self

    def set_J(self, value):
        if type(value) is not bool:
            raise NotTruthValue

        self.J = value
        self.__calculate_output()
        return self

    def set_clock(self, value):
        if type(value) is not bool:
            raise NotTruthValue

        self.clock = value
        self.__calculate_output()
        return self

    def __calculate_output(self):
        if not self.clock:
            return self
        else:
            and_k = And().set_input(0, self.K).set_input(1, self.clock)
            and_j = And().set_input(0, self.J).set_input(1, self.clock)

            self.Q = Nor().set_input(0, and_k.get_output()).set_input(0, self.Qp).get_output()
            self.Qp = Nor().set_input(0, and_j.get_ouput()).set_input(1, self.Q)

            return self
