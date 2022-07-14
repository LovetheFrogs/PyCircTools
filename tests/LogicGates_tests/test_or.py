from PyCircTools.LogicGates import Or


def test_or_gate():
    errors = []
    orGate = Or()
    orGate_overload = Or()
    
    assert not (bool)(orGate.get_output()), ("False and False not passed!")

    orGate.set_input(0, True)
    assert (bool)(orGate.get_output()), ("True and False not passed!")

    orGate_overload[0] = True
    assert (bool)(orGate.get_output()), ("True and False not passed!")

    orGate.set_input(1, True)
    assert (bool)(orGate.get_output()), ("True and True not passed!")

    orGate_overload[1] = True
    assert (bool)(orGate.get_output()), ("True and True not passed!")

    orGate.add_input()
    assert orGate.get_numOfInputs() == 3, ("Input adding not passed!")

    orGate2 = Or(3)
    assert orGate2.get_numOfInputs() == 3, ("Multiple inputs when building not passed!")

    assert (bool)(orGate2.set_input(0, True).set_input(1, True).get_output()),("True and True and False not passed!")

    orGate2.remove_input()
    assert orGate2.get_numOfInputs() == 2, ("Removing item not passed!")

    assert (bool)(orGate2.get_output()), ("Testing output after removing input not passed!")

    print("No errors in OR gate...")

if __name__ == "__main__":
    test_or_gate()