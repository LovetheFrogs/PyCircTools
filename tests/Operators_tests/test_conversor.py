from PyCircTools import Conversor


def test_conversor():
    conv = Conversor()
    assert conv.set_input([True, False, True, False]).get_output() == [True, True, False, True]

    _conv = Conversor(8)
    assert _conv.set_input([False, True, True, True, False, False, False]) == [False, False, False, False, True, True,
                                                                               True, True]
