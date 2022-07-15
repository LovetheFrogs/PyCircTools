from PyCircTools import And, Or, Mux2to1, Mux4to1, NotTruthValue, NotControlList, WrongSize
from PyCircTools.Operators import Adder, Subtractor


class Alu:
    """
    Alu module. Has 3 inputs, A (first operand), B (second operand) and Operation (control signal;
    it is a list of size 2 of bools) all initialised to False. This control signal is used to select the solution
    needed. The following lines explain which signal selects which operation.
    False, False -> A and B
    True, False -> A or B
    False, True -> A + B
    True, True -> A - B
    Note that the less significant value is the 0th position of the list and so on.
    """
    def __init__(self):
        """
        Constructor of the ALU module. For reference on how this class works, use help(Alu). It is used to build an Alu
        with opCode = 00, A and B = False.
        """
        self.A = False
        self.B = False
        self.Operation = [False, False]
        self.CarrySel = self.Operation[0]
        self.conj = And()
        self.disj = Or()
        self.adder = Adder()
        self.sub = Subtractor()
        self.mux = Mux4to1()
        self.carrSel = Mux2to1()
        self.output = self.mux.get_output()
        self.carryOut = self.carrSel.get_output()
        self.__cal_modules()

    def get_A(self):
        """
        Method get_A returns the value of the A input.

        :return: Value of the first operator (A input).
        :rtype: bool
        """
        return self.A

    def get_B(self):
        """
        Method get_B returns the value of the B input.

        :return: Value of the second operator (B input).
        :rtype: bool
        """
        return self.B

    def get_op(self):
        """
        Method get_op returns the list of control signals Operation.

        :return: List of control signals of the ALU.
        :rtype: list
        """
        return self.Operation

    def get_output(self):
        """
        Method get_output returns the output of the ALU.

        :return: Result of the operation.
        :rtype: bool
        """
        return self.output

    def get_carryOut(self):
        """
        Method get_carryOut returns the value of the carryOut signal. Useful in adding and subtracting.

        :return: Value of the output carry.
        :rtype: bool
        """
        return self.carryOut

    def set_A(self, value):
        """
        Sets the value of the A input signal.

        :param value: Value of the A signal.
        :type value: bool
        :raises NotTruthValue: Raised when value's type is not bool.
        """
        if type(value) is not bool:
            raise NotTruthValue

        self.A = value
        self.__cal_modules()
        return self

    def set_B(self, value):
        """Sets the value of the B input signal.

        :param value: Value of the B signal.
        :type value: bool
        :raises NotTruthValue: Raised when value's type is not bool.
        """
        if type(value) is not bool:
            raise NotTruthValue

        self.B = value
        self.__cal_modules()
        return self

    def set_op(self, op_code):
        """
        Method set_A sets the value of the Operation control signal. It also sets the value of the CarrySel signal.

        :param op_code: List of operation codes. Must be a list of bool values.
        :type op_code: list
        :raises NotControlList: raised when a list of operation codes is not of type bool or is not a list at all
        :raises WrongSize: raised when the list of operation codes does not have the required size
        """
        if type(op_code) is not list:
            raise NotControlList

        for val in op_code:
            if type(val) is not bool:
                raise NotControlList

        if len(op_code) != 2:
            raise WrongSize(len(op_code), 2)

        # CarrySel control signal's value is the same as the less significant input from op_code.
        self.Operation = op_code
        self.CarrySel = op_code[0]
        self.__cal_modules()
        return self

    def __cal_modules(self):
        """
        Private method __cal_modules calculates the inputs and outputs of each module inside the ALU, as well as the
        ALU's output and carryOut.
        """
        self.conj.set_input(0, self.A).set_input(1, self.B)
        self.disj.set_input(0, self.A).set_input(1, self.B)
        self.adder.set_A(self.A).set_B(self.B)
        self.sub.set_A(self.A).set_B(self.B)

        for count, value in enumerate(self.Operation):
            self.mux.set_set(count, value)

        self.mux.set_input(0, self.conj.get_output()).set_input(1, self.disj.get_output())\
            .set_input(2, self.adder.get_output()).set_input(3, self.sub.get_output())
        self.output = self.mux.get_output()

        self.carrSel.set_set(self.CarrySel)
        self.carrSel.set_input(0, self.adder.get_carryOut()).set_input(1, self.sub.get_carryOut())
        self.carryOut = self.carrSel.get_output()

        return self
