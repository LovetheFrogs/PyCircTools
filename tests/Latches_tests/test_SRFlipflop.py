from PyCircTools.Latches import SRFlipflop


def test_SRFlipflop():
    errors = []
    latch = SRFlipflop()

    if latch.get_Q():
        errors.append("Q output when generated test not passed!")

    if latch.set_R(True).get_Q():
        errors.append("Operation when enable is False!")

    previous = [latch.get_Q(), latch.get_Qp()]
    if latch.set_clock(True).set_R(False).get_Q() != previous[0] and latch.get_Qp() != previous[1]:
        errors.append("Set and all False test not passed!")

    if not latch.set_R(True).get_Q() and latch.get_Qp():
        pass
    else:
        errors.append("R and not S test not passed!")

    if latch.set_R(False).set_S(True).get_Q() and not latch.get_Qp():
        pass
    else:
        errors.append("not R and S test not passed!")

    assert not errors, "errors occured:\n{}".format("\n".join(errors))
