from BinaryTools.LogicGates import Not


def test_not_gate():
    errors = []
    notGate = Not.Not()

    if notGate.get_output():
        errors.append("True not passed!")

    if not notGate.set_input(False).get_output():
        errors.append("False not passed!")

    if notGate.get_input():
        errors.append("Get input method for False not passed!")

    if not notGate.set_input(True).get_input():
        errors.append("Get input method for True not passed!")
