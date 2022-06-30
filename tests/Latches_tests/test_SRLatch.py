from PyCircTools.Latches import SRLatch


def test_SRLatch():
    errors = []
    latch = SRLatch()

    if latch.get_Q():
        errors.append("Q output when generated test not passed!")

    if latch.set_R(True).get_Q():
        errors.append("Operation when enable is False!")

    if not latch.set_enable(True).set_R(False).get_Q() and not latch.get_Qp():
        pass
    else:
        errors.append("Set and all False test not passed!")

    if not latch.set_R(True).get_Q() and latch.get_Qp():
        pass
    else:
        errors.append("R and not S test not passed!")

    if latch.set_R(False).set_S(True).get_Q() and not latch.get_Qp():
        pass
    else:
        errors.append("not R and S test not passed!")

    if latch.set_R(True).get_Q() and latch.get_Qp():
        pass
    else:
        errors.append("R and S test not passed!")

    assert not errors, "errors occured:\n{}".format("\n".join(errors))
