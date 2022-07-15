from PyCircTools import NotTruthValue, NotControlList, WrongSize


class Extender:
    """
    Extender module acts as a sign extender. It makes the output be the input with its most significant bit repeated. It
    can be used for both, two's complement and pure binary.
    """
    def __init__(self, into=2, out=4, pure=True):
        """
        Constructor method creates an extender from into bits to out bits. The default is pure binary, but it can be
        used for two's complement by specifying pure=False.

        :param into: Number of inputs.
        :type into: int
        :param out: Number of bits of the output.
        :type out: int
        :param pure: Used to know if the input is in pure binary or two's complement.
        :type pure: bool
        """
        self.numInto = into
        self.numOut = out
        self.pure = pure
        self.input = [False] * into
        self.output = self.__calculate_output()

    def get_numIn(self):
        """
        Method get_numIn gets the number of inputs.

        :return: Number of input signals of the extender.
        :rtype: int
        """
        return self.numInto

    def get_numOut(self):
        """
        Method get_numOut gets the number of output signals.

        :return: Number of output signals of the extender.
        :rtype: int
        """
        return self.numOut

    def get_input(self):
        """
        Method get_input gets the input to extend.

        :return: A list containing the input.
        :rtype: list
        """
        return self.input

    def get_output(self):
        """
        Method get_output gets the extended output.

        :return: A list containing the output.
        :rtype: list
        """
        return self.output

    def get_pure(self):
        """
        Method get_pure gets whether an input is expressed in pure binary or two's complement.

        :return: True if input is in pure binary, False otherwise.
        :rtype: bool
        """
        return self.pure

    def set_input(self, values, pure=True):
        """
        Method set_input is used to set the input of the extender to a certain list of values.

        :param values: List of boolean values for the input of the extender
        :type values: list
        :param pure: Indicates if the list is expressed in pure binary. Defaults to True.
        :type pure: bool
        :raises NotTruthValue: Raised when value's type is not bool.
        :raises NotControlList: raised when the contents of the input are not of type bool or is not a list at all
        :raises WrongSize: raised when the list for the input does not have the required size
        """
        if type(pure) is not bool:
            raise NotTruthValue

        if type(values) is not list:
            raise NotControlList

        for item in values:
            if type(item) is not bool:
                raise NotControlList

        if len(values) != self.numInto:
            raise WrongSize(len(values), self.numInto)

        self.input = values
        self.__set_pure(pure)
        self.output == self.__calculate_output()

        return self

    def __set_pure(self, value):
        """
        Private method __set_pure is used internally to set the value of the self.pure attribute.

        :param value: Desired value of the 'pure' attribute
        :type value: bool
        """
        if type(value) is not bool:
            raise NotTruthValue

        self.pure = value
        return self

    def __calculate_output(self):
        """
        Private method __calculate_output gets the expected output for the input introduced.

        :return: Desired output of the extender.
        :rtype: list
        """
        output = []
        if self.pure:
            for i in range(self.numOut):
                if i < self.numInto:
                    output.append(self.input[i])
                else:
                    output.append(False)

        else:
            for i in range(self.numOut):
                if i < self.numInto:
                    output.append(self.input[i])
                else:
                    output.append(self.input[self.numInto - 1])

        return output
