"""
General CTools exceptions.
"""


class CircuitToolsException(Exception):
    """
    Parent Exception class. All general CTools exceptions inherit from this class.
    """
    def __init__(self, msg="CircuitTools Exception."):
        self.msg = msg
        super().__init__(self.msg)


class NotTruthValue(CircuitToolsException):
    """
    NotTruthValue is an exception that raises when an input which is expected to be a truth value (either True or False)
    is of another data type.
    """
    def __init__(self, msg="Not a supported value 'True' or 'False'."):
        self.msg = msg
        super().__init__(self.msg)
        