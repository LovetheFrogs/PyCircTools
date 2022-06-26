from CTools.LogicGates import And, Nor


class SRLatch:
    def __init__(self):
        self.R = False
        self.S = False
        self.enable = False
        self.Q = False
        self.Qp = False

    def get_R(self):
        return self.R

    def get_S(self):
        return self.S

    def get_enable(self):
        return self.enable

    def get_Q(self):
        return self.Q

    def get_Qp(self):
        return self.Qp

    def set_R(self, value):
        self.R = value
        self.__calculate_output()
        return self

    def set_S(self, value):
        self.S = value
        self.__calculate_output()
        return self

    def set_enable(self, value):
        self.enable = value
        self.__calculate_output()
        return self

    def __calculate_output(self):
        and_r = And().set_input(0, self.R).set_input(1, self.enable)
        and_s = And().set_input(0, self.S).set_input(1, self.enable)

        nor_r = Nor().set_input(0, and_r.get_output()).set_input(1, self.Qp)
        nor_s = Nor().set_input(0, and_s.get_output()).set_input(1, self.Q)

        self.Q = nor_r.get_output()
        self.Qp = nor_s.get_output()

        return self
