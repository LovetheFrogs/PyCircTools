from CTools.LogicGates import Nor


def test_or_gate():
    errors = []
    norGate = Nor.Nor()

    if not norGate.get_output():
        errors.append("False and False not passed!")

    norGate.set_input(0, True)
    if norGate.get_output():
        errors.append("True and False not passed!")

    norGate.set_input(1, True)
    if norGate.get_output():
        errors.append("True and True not passed!")

    norGate.add_input()
    if not norGate.get_numOfInputs() == 3:
        errors.append("Input adding not passed!")

    norGate2 = Nor.Nor(3)
    if not norGate2.get_numOfInputs() == 3:
        errors.append("Multiple inputs when building not passed!")

    if norGate2.set_input(0, True).set_input(1, True).get_output():
        errors.append("True and True and False not passed!")

    norGate2.remove_input()
    if not norGate2.get_numOfInputs() == 2:
        errors.append("Removing item not passed!")

    if norGate2.get_output():
        errors.append("Testing output after removing input not passed!")

    assert not errors, "errors occured:\n{}".format("\n".join(errors))
