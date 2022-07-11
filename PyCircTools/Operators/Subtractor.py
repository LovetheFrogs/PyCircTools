from PyCircTools import Adder, Not, NotTruthValue


class Subtractor(Adder):
    """
    Subtractor module. Inherits from Adder class because it just needs to negate the 'B' input.
    """
    def __init__(self, full=False):
        """
        Subtractor class constructor. Calls the Adder constructor and then changes the value of the 'B' input.

        :param full: Defaults to False. Used to specify if the type of adder used. (False -> Half-adder, True -> Full-adder).
        :type full: bool
        """
        super().__init__(full)
        self.B = Not().set_input(self.B).get_output()

    def set_B(self, value):
        """
        Method set_B needs to be overridden in order to set the 'B' input to the negation of the value so that it can
        subtract.

        :param value: Desired value of the adder's second summand.
        :type value: bool
        :raises NotTruthValue: Raised when a variable type is not bool.
        """
        if type(value) is not bool:
            raise NotTruthValue

        self.B = Not().set_input(value).get_output()
        super()._calculate_output()
        return self
