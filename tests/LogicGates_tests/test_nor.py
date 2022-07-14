from PyCircTools.LogicGates import Nor


def test_or_gate():
    norGate = Nor()
    norGate_overload = Nor()

    assert not (bool)(norGate.get_output()), ("False and False not passed!")

    norGate.set_input(0, True)
    assert not (bool)(norGate.get_output()),("True and False not passed!")

    norGate_overload[0] = True
    assert not (bool)(norGate_overload.get_output()),("True and False not passed!")

    norGate.set_input(1, True)
    assert not (bool)(norGate.get_output()),("True and True not passed!")

    norGate_overload[1] = True
    assert not (bool)(norGate_overload.get_output()),("True and True not passed!")

    norGate.add_input()
    assert norGate.get_numOfInputs() == 3,("Input adding not passed!")

    norGate2 = Nor(3)
    assert (norGate2.get_numOfInputs()) == 3,("Multiple inputs when building not passed!")

    assert not (bool)(norGate2.set_input(0, True).set_input(1, True).get_output()),("True and True and False not passed!")

    norGate2.remove_input()
    assert norGate2.get_numOfInputs() == 2,("Removing item not passed!")

    assert not (bool)(norGate2.get_output()),("Testing output after removing input not passed!")

    print("No errors in NOR gate...")

if __name__ == "__main__":
    test_or_gate()
