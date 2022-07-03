from PyCircTools.Latches import DLatch


def test_DLatch():
    errors = []
    latch = DLatch()

    if latch.get_Q() and not latch.get_Qp():
        errors.append("Outputs at start value test not passed!")

    if latch.set_D(True).get_Q() and not latch.get_Qp():
        errors.append("Outputs changed when enable is still False!")
