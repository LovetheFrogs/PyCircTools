from CTools.LogicGates import Nand


def test_and_gate():
    errors = []
    nandGate = Nand.Nand()

    if not nandGate.get_output():
        errors.append("False and False not passed!")

    nandGate.set_input(0, True)
    if not nandGate.get_output():
        errors.append("True and False not passed!")

    nandGate.set_input(1, True)
    if nandGate.get_output():
        errors.append("True and True not passed!")

    nandGate.add_input()
    if not nandGate.get_numOfInputs() == 3:
        errors.append("Input adding not passed!")

    nandGate2 = Nand.Nand(3)
    if not nandGate2.get_numOfInputs() == 3:
        errors.append("Multiple inputs when building not passed!")

    if not nandGate2.get_output():
        errors.append("Output when 3 inputs not passed!")

    if not nandGate2.set_input(0, True).set_input(1, True).get_output():
        errors.append("True and True and False not passed!")

    nandGate2.remove_input()
    if not nandGate2.get_numOfInputs() == 2:
        errors.append("Removing item not passed!")

    if nandGate2.get_output():
        errors.append("Testing output after removing input not passed!")

    if not nandGate2.set_input(0, False).get_output():
        errors.append("Testing output after removing input not passed!")

    assert not errors, "errors occured:\n{}".format("\n".join(errors))
