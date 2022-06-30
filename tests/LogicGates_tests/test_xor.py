from PyCircTools.LogicGates import Xor


def test_or_gate():
    errors = []
    xorGate = Xor.Xor()

    if xorGate.get_output():
        errors.append("False and False not passed!")

    xorGate.set_input(0, True)
    if not xorGate.get_output():
        errors.append("True and False not passed!")

    xorGate.set_input(1, True)
    if xorGate.get_output():
        errors.append("True and True not passed!")

    xorGate.add_input()
    if not xorGate.get_numOfInputs() == 3:
        errors.append("Input adding not passed!")

    xorGate2 = Xor.Xor(3)
    if not xorGate2.get_numOfInputs() == 3:
        errors.append("Multiple inputs when building not passed!")

    if xorGate2.set_input(0, True).set_input(1, True).get_output():
        errors.append("True and True and False not passed!")

    xorGate2.remove_input()
    if not xorGate2.get_numOfInputs() == 2:
        errors.append("Removing item not passed!")

    if xorGate2.get_output():
        errors.append("Testing output after removing input not passed!")

    assert not errors, "errors occured:\n{}".format("\n".join(errors))
