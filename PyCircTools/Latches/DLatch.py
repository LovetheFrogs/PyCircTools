from PyCircTools.Exceptions.CircuitToolsExceptions import NotTruthValue
from PyCircTools.LogicGates import And, Nor, Not


class DLatch:
    def __init__(self):
        self.D = False
        self.enable = False
        self.Q = False
        self.Qp = False

    def get_D(self):
        return self.D

    def get_enable(self):
        return self.enable

    def get_Q(self):
        return self.Q

    def get_Qp(self):
        return self.Qp

    def set_D(self, value):
        self.D = value
        self.__calculate_output()
        return self

    def set_enable(self, value):
        self.enable = value
        self.__calculate_output()
        return self

    def __calculate_output(self):
        and_d = And().set_input(0, self.enable).set_input(1, self.D)
        not_d = Not().set_input(self.D)
        and_not_d = And().set_input(0, not_d.get_output()).set_input(1, self.enable)

        nor_d = Nor().set_input(0, and_d.get_output()).set_input(1, self.Q)
        nor_not_d = Nor().set_input(0, and_not_d.get_output()).set_input(1, self.Qp)

        self.Q = nor_not_d.get_output()
        self.Qp = nor_d.get_output()

        return self
