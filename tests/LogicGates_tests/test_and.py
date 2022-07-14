from PyCircTools.LogicGates import And


def test_and_gate():
    andGate = And()
    andGate_overload = And()

    assert (bool)(andGate.get_output()), "False and False not passed!"

    andGate.set_input(0, True)
    assert (bool)(andGate.get_output()) == False, ("True and False not passed!")

    andGate_overload[0] = True
    assert (bool)(andGate_overload.get_output()) == False, ("True and False not passed! - Overload")

    andGate.set_input(1, True)
    assert (bool)(andGate.get_output()) == True, ("True and True not passed!")

    andGate_overload[1] = True
    assert (bool)(andGate_overload.get_output()) == True, ("True and True not passed! - Overload")


    andGate.add_input()
    assert (andGate.get_numOfInputs() == 3), ("Input adding not passed!")

    andGate2 = And(3)
    andGate2_overload = And(3)
    assert andGate2.get_numOfInputs() == 3 or andGate2_overload.get_numOfInputs() == 3, ("Multiple inputs when building not passed!")

    assert (bool)(andGate2.set_input(0, True).set_input(1, True).get_output()) == False, ("True and True and False not passed!")

    andGate2_overload[0] = True
    andGate2_overload[1] = True
    assert (bool)(andGate2_overload.get_output()) == False, ("True and True and False not passed! - Overload")

    andGate2.remove_input()
    assert andGate2.get_numOfInputs() == 2, ("Removing item not passed!")

    assert (bool)(andGate2.get_output()), ("Testing output after removing input not passed!")

    print("No errors in AND gate...")

if __name__ == "__main__":
    test_and_gate()
