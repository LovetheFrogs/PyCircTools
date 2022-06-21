"""
PyCircTools Multiplexer module Exceptions.
"""


class MultiplexerException(Exception):
    """
    MultiplexerException is the parent Exception class for all PyCircTools.Multiplexers related Exceptions
    """
    def __init__(self, msg="Multiplexer Exception"):
        self.msg = msg
        super().__init__(self.msg)


class NonExistingInput(MultiplexerException):
    """
    NonExistingInput is raised when a Multiplexer/Demultiplexer doesn't have the input asked for.
    """
    def __init__(self, requestedInput=None):
        if requestedInput is not None:
            self.msg = "Input " + str(requestedInput) + " does not exist."
        else:
            self.msg = "Input requested does not exist."
        super().__init__(self.msg)
