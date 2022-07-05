from PyCircTools.Latches import DFlipflop


def test_DFlipflop():
    errors = []
    latch = DFlipflop()

    if latch.get_Q() and not latch.get_Qp():
        errors.append("Outputs at start value test not passed!")

    if latch.set_D(True).get_Q() and not latch.get_Qp():
        errors.append("Outputs changed when enable is still False!")

    if not latch.set_enable(True).set_D(False).get_Q() and latch.get_Qp():
        pass
    else:
        errors.append("Data False does not give back expected output!")

    if latch.set_D(True).get_Q() and not latch.get_Qp():
        pass
    else:
        errors.append("Data True does not give back expected output!")

    assert not errors, "errors occured:\n{}".format("\n".join(errors))
