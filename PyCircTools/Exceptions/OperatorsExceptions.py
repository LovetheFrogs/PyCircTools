"""
PyCircTools Operators module Exceptions.
"""


class OperatorException(Exception):
    """
    OperatorException is the parent Exception class for all PyCircTools.Operators related Exceptions.
    """
    def __init__(self, msg="Operator Exception"):
        self.msg = msg
        super().__init__(self.msg)


class NotCorrectAdder:
    """
    NotCorrectAdder is raised when a function is called and is not allowed for the instance of an adder used in.
    """
    def __init__(self, method=None, addr_class=False):
        if method is None:
            self.msg = "Method not allowed for an instance of a " + get_adder_type(addr_class)
        else:
            self.msg = "Method " + method + " not allowed for an instance of " + get_adder_type(addr_class)


def get_adder_type(addr_class):
    """
    Method used to get the type of adder used.

    :param addr_class: Type of adder, either False for half-adder or True for full-adder.
    :type addr_class: bool
    :return: String containing the name of the adder.
    :rtype: str
    """
    if addr_class:
        return "Half-adder."
    else:
        return "Full-adder."
