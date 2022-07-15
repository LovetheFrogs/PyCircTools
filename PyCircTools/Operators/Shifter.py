from PyCircTools import DFlipflop, NotTruthValue, NotControlList, WrongSize
# Copy is used to generate a copy of input so that it is not deleted when calculating output.
import copy


class Shifter:
    """
    Shifter module. Used to shift the position of the inputs left or right a given number of positions.
    """
    def __init__(self, num=4, pos=1, dirs=False):
        """
        Constructor of the Shifter module. Takes three arguments, num, pos and dir. It defaults to a shifter with 4
        inputs that moves 1 position to the left.

        :param num: Number of inputs of the shifter.
        :type num: int
        :param pos: Number of positions the shifter will move the input.
        :type pos: int
        :param dirs: Direction the shifter moves (Defaults to False which is shift right. True is shift left).
        :type dirs: bool
        """
        self.num_of_inputs = num
        self.positions = pos
        self.D = dirs
        self.input = [False] * num
        self.clock = False
        self.output = self.__calculate_output()

    def get_numOfInputs(self):
        """
        Method get_numOfInputs returns the number of inputs of the shifter.

        :return: Number of inputs of the shifter.
        :rtype: int
        """
        return self.num_of_inputs

    def get_positions(self):
        """
        Method get_positions returns the number of positions the shifter moves.

        :return: Number of positions to shift.
        :rtype: int
        """
        return self.positions

    def get_D(self):
        """
        Method get_D returns the direction of the shifter.

        :return: Direction the shifter moves.
        :rtype: bool
        """
        return self.D

    def get_input(self):
        """
        Method get_input returns the input of the shifter.

        :return: Input of the shift register in form of a list.
        :rtype: list
        """
        return self.input

    def get_output(self):
        """
        Method get_output returns the output of the shifter.

        :return: Output of the shift register in the form of a list.
        :rtype: list
        """
        return self.output

    def get_clock(self):
        """
        Method get_clock returns the value of the clock.

        :return: Value of the clock.
        :rtype: bool
        """
        return self.clock

    def set_D(self, value):
        """
        Method set_D is used to set the direction the shifter moves, being False -> shift right and True -> shift left.

        :param value: New value of the D attribute.
        :type value: bool
        :raises NotTruthValue: Raised when value's type is not bool.
        """
        if type(value) is not bool:
            raise NotTruthValue

        self.D = value
        self.output = self.__calculate_output()
        return self

    def set_clock(self, value):
        """
        Method set_clock is used to set the value of the clock.

        :param value: New value of the clock attribute.
        :type value: bool
        :raises NotTruthValue: Raised when value's type is not bool.
        """
        if type(value) is not bool:
            raise NotTruthValue

        self.clock = value
        self.output = self.__calculate_output()
        return self

    def set_input(self, values):
        """
        Method set_input is used to set the input of the shifter to a list of bool.

        :param values: List of values for the input.
        :type values: list
        :raises NotControlList: raised when a list of ovalues is not a list of bool or is not a list at all
        :raises WrongSize: raised when the list of values does not have the required size
        """
        if type(values) is not list:
            raise NotControlList

        for val in values:
            if type(val) is not bool:
                raise NotControlList

        if len(values) > self.num_of_inputs:
            raise WrongSize(len(values), self.num_of_inputs)

        self.input = values
        self.output = self.__calculate_output()
        return self

    def __calculate_output(self):
        """
        Method __calculate_output is gets the value of the output of the shifter, depending on its direction, number of
        positions to move and number of inputs. It uses the copy.copy method to create copies of the input and output
        and avoid replacing the original values when not intended. The same method is used for both directions and all
        possible combinations of number of inputs and positions to shift.

        :return: Output the shifter will have.
        :rtype: list
        """
        output = [False] * self.num_of_inputs
        if self.clock:
            output = copy.copy(self.input)
            for _ in range(self.positions):
                inp = copy.copy(output)
                if not self.D:
                    for i in range(self.num_of_inputs):
                        if i == 0:
                            output[i] = DFlipflop().set_D(inp[self.num_of_inputs - 1]).set_enable(True).get_Q()
                        else:
                            output[i] = DFlipflop().set_D(inp[i - 1]).set_enable(True).get_Q()

                else:
                    for i in range(self.num_of_inputs):
                        if i == self.num_of_inputs - 1:
                            output[i] = DFlipflop().set_D(inp[0]).set_enable(True).get_Q()
                        else:
                            output[i] = DFlipflop().set_D(inp[i + 1]).set_enable(True).get_Q()

        return output
