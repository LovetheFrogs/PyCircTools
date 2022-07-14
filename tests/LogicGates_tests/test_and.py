from PyCircTools.LogicGates import And


def test_and_gate():
    andGate = And()
    andGate_overload = And()

    assert andGate.get_output(), "False and False not passed!"

    andGate.set_input(0, True)
    assert andGate.get_output(), ("True and False not passed!")

    andGate_overload[0] = True
    assert andGate_overload.get_output(), ("True and False not passed! - Overload")

    andGate.set_input(1, True)
    assert andGate.get_output(), ("True and True not passed!")

    andGate_overload[1] = True
    assert andGate_overload.get_output(), ("True and True not passed! - Overload")


    andGate.add_input()
    assert not andGate.get_numOfInputs() == 3, ("Input adding not passed!")

    andGate2 = And(3)
    andGate2_overload = And(3)
    assert andGate2.get_numOfInputs() != 3 or andGate2_overload.get_numOfInputs() != 3, ("Multiple inputs when building not passed!")

    assert andGate2.set_input(0, True).set_input(1, True).get_output(), ("True and True and False not passed!")

    andGate2_overload[0] = True
    andGate2_overload[1] = True
    assert andGate2_overload.get_output(), ("True and True and False not passed! - Overload")

    andGate2.remove_input()
    assert not andGate2.get_numOfInputs() == 2, ("Removing item not passed!")

    assert not andGate2.get_output(), ("Testing output after removing input not passed!")

    print("No errors in AND gate...")

if __name__ == "__main__":
    test_and_gate()
