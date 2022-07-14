from PyCircTools.Exceptions.CircuitToolsExceptions import NotTruthValue


class Not:
    """
    Not logic gate. Only has 1 input and more inputs can not be added.
    """
    def __init__(self):
        """
        Not class constructor method.
        """
        self.input = True
        self.output = self.__calculate_output()

    def get_input(self):
        """
        Method get_input is used to get value of the input of the gate.

        :return: Returns the value of the input.
        :rtype: bool
        """
        return self.input

    def get_output(self):
        """
        Method get_output is used to get the output of the gate.

        :return: Output of the gate.
        :rtype: bool
        """
        return self.output

    def set_input(self, value):
        """
        Method set_input sets the input of the gate to the desired value.

        :param value: Desired value of the input.
        :type value: bool
        :raises NotTruthValue: Raised when value's type is not bool.
        """
        if type(value) is not bool:
            raise NotTruthValue

        self.input = value
        self.__calculate_output()
        return self

    def __calculate_output(self):
        self.output = not self.input
 
